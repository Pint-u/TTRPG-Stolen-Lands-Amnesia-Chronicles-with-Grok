import re
import pandas as pd
import os
import snappy  # For optional compression; remove if not needed

def convert_journal_to_csv(input_path='Journal.md', output_path='Journal.csv', compress=False):
    """
    Converts Journal.md to CSV.
    Columns: Date, Time, Turn, Title, Description
    """
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        journal_md = f.read()

    dates = []
    times = []
    turns = []
    titles = []
    descriptions = []

    current_date = ''
    lines = journal_md.splitlines()
    for line in lines:
        date_match = re.match(r'##\s*(August \d{2}, 2025\s*-\s*.+)', line)
        if date_match:
            current_date = date_match.group(1).strip()
            continue
        
        entry_match = re.match(r'-\s*\*\*(\d{2}:\d{2})\s*\(Turn (\d+):\s*(.*?)\)\*\*:\s*(.*)', line)
        if entry_match and current_date:
            dates.append(current_date)
            times.append(entry_match.group(1))
            turns.append(int(entry_match.group(2)))
            titles.append(entry_match.group(3))
            descriptions.append(entry_match.group(4).strip())

    df = pd.DataFrame({
        'Date': dates,
        'Time': times,
        'Turn': turns,
        'Title': titles,
        'Description': descriptions
    })

    if compress:
        compressed_data = snappy.compress(df.to_csv(index=False).encode())
        with open(output_path + '.snappy', 'wb') as f:
            f.write(compressed_data)
        print(f"Compressed CSV saved to {output_path}.snappy")
    else:
        df.to_csv(output_path, index=False)
        print(f"CSV saved to {output_path}")

def convert_world_npcs_to_csv(input_path='World_NPCs.markdown', output_path='World_NPCs.csv', compress=False):
    """
    Converts World_NPCs.markdown to CSV.
    Columns: Category, Name, Relation, Known_Facts
    """
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        world_md = f.read()

    categories = []
    names = []
    relations = []
    facts = []

    current_category = ''
    current_name = None
    current_relation = None
    lines = world_md.splitlines()
    for line in lines:
        cat_match = re.match(r'##\s*(\w+)', line)
        if cat_match:
            current_category = cat_match.group(1)
            continue
        
        name_match = re.match(r'###\s*(.+)', line)
        if name_match:
            if current_name and current_relation:  # Save previous if incomplete
                categories.append(current_category)
                names.append(current_name)
                relations.append(current_relation)
                facts.append('')  # Default if no facts
            current_name = name_match.group(1).strip()
            current_relation = None
            continue
        
        rel_match = re.match(r'-\s*\*\*Relation\*\*:\s*(.*)', line)
        if rel_match and current_name:
            current_relation = rel_match.group(1).strip()
            continue
        
        fact_match = re.match(r'-\s*\*\*Known Facts\*\*:\s*(.*)', line)
        if fact_match and current_name and current_relation:
            categories.append(current_category)
            names.append(current_name)
            relations.append(current_relation)
            facts.append(fact_match.group(1).strip())
            current_name = None
            current_relation = None

    # Save last entry if pending
    if current_name and current_relation:
        categories.append(current_category)
        names.append(current_name)
        relations.append(current_relation)
        facts.append('')

    df = pd.DataFrame({
        'Category': categories,
        'Name': names,
        'Relation': relations,
        'Known_Facts': facts
    })

    if compress:
        compressed_data = snappy.compress(df.to_csv(index=False).encode())
        with open(output_path + '.snappy', 'wb') as f:
            f.write(compressed_data)
        print(f"Compressed CSV saved to {output_path}.snappy")
    else:
        df.to_csv(output_path, index=False)
        print(f"CSV saved to {output_path}")

if __name__ == "__main__":
    # Convert both files; set compress=True for snappy compression
    convert_journal_to_csv(compress=False)
    convert_world_npcs_to_csv(compress=False)
