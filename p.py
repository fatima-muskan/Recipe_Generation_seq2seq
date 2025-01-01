import json
import csv

def extract_recipe_data(json_files, csv_file):
    # Fields to extract
    fields = ['title', 'ingredients', 'instructions']
    rows = []

    # Read each JSON file
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            # Check if the data is a dictionary
            if isinstance(data, dict):
                for key, value in data.items():
                    # Ensure all required fields exist
                    row = {
                        'title': value.get('title', key),  # Use key as a fallback for title
                        'ingredients': value.get('ingredients', ''),
                        'instructions': value.get('instructions', '')
                    }
                    rows.append(row)
            else:
                print(f"Unexpected format in file: {json_file}")

    # Write to a single CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    print(f"CSV file '{csv_file}' created successfully with {len(rows)} recipes.")

# Example usage
json_files = ["recipes_raw_nosource_ar.json", "recipes_raw_nosource_epi.json", "recipes_raw_nosource_fn.json"]  # Replace with your JSON file paths
csv_file = "recipes_combined.csv"
extract_recipe_data(json_files, csv_file)
