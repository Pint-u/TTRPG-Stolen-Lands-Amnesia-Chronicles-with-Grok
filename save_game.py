import base64
from zipfile import ZipFile
from io import BytesIO

# List core files
files = ['Journal.md', 'Inventory.md', 'World_NPCs.markdown', 'Character_Sheets.markdown']

# Read and print full content in code blocks
for file in files:
    try:
        with open(file, 'r') as f:
            content = f.read()
        print(f"```markdown\n# Full Content of {file}\n{content}\n```")
    except FileNotFoundError:
        print(f"Error: {file} not found.")

# Generate data URLs for download
for file in files:
    try:
        with open(file, 'r') as f:
            content = f.read()
        b64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')
        print(f"Data URL for {file}: data:text/markdown;base64,{b64}")
    except:
        pass

# Zip all files for large content (base64 zip to handle token limits)
zip_buffer = BytesIO()
with ZipFile(zip_buffer, 'w') as zip_file:
    for file in files:
        try:
            with open(file, 'r') as f:
                zip_file.writestr(file, f.read())
        except:
            pass
zip_b64 = base64.b64encode(zip_buffer.getvalue()).decode('utf-8')
print(f"Zip Data URL (download as game_save.zip): data:application/zip;base64,{zip_b64}")
if len(zip_b64) > 2000:  # Split for token limits
    for i in range(0, len(zip_b64), 2000):
        print(f"Zip Part {i//2000 + 1}: {zip_b64[i:i+2000]}")  # Concatenate parts manually