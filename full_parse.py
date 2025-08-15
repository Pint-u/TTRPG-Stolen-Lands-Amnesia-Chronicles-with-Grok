import pandas as pd
from io import StringIO
import re

# Load md (replace with open('testrun2.md').read() if uploaded)
md_content = """[Paste full testrun2.md text here for POC]"""

# Split into sections
sections = re.split(r'(📖 Title:|📊 Recap|👥 Party Status|💰 Gained/Lost Items)', md_content)
results = {}
response_num = 1
current_key = ''

def parse_table(text):
    try:
        text = '\n'.join(line for line in text.split('\n') if line.strip().startswith('|'))  # Filter to table lines only
        if not text:
            return '[]'
        df = pd.read_table(StringIO(text), sep='|', skipinitialspace=True, engine='python', header=None)
        df = df.iloc[:, 1:-1]
        headers = [col.strip() for col in df.iloc[0]]
        df = df.iloc[1:]
        df.columns = headers
        df = df[df.apply(lambda row: not all(str(x).strip() in ['', '---'] for x in row), axis=1)]
        df = df.apply(lambda col: col.str.strip() if col.dtype == 'object' else col)
        if df.empty or (headers[0] == 'Item' and any('No items gained or lost' in str(val) for val in df.get('Item', []))):
            return '[]'
        return df.to_json(orient="records")
    except Exception as e:
        return f'Error parsing: {str(e)}'

for section in sections:
    section = section.strip()
    if section in ['📊 Recap', '👥 Party Status', '💰 Gained/Lost Items']:
        current_key = f'Response {response_num} {section}'
    elif section and current_key:
        results[current_key] = parse_table(section)
        current_key = ''
    if '🔄' in section:  # New response on Automatic Updates
        response_num += 1

# Unescape for clean output
clean_results = {k: v.replace('\\', '') if isinstance(v, str) else v for k, v in results.items()}

print(json.dumps(clean_results, indent=2))