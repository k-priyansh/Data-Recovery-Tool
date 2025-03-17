import pandas as pd
import json
import re

def preprocess_json(json_file_path, output_file_path):
    with open(json_file_path, 'r') as file:
        content = file.read()

    # Replace single quotes with double quotes
    content = re.sub(r"(?<!\\)'", '"', content)

    with open(output_file_path, 'w') as file:
        file.write(content)

def json_to_table(json_file_path, output_file_path):
    preprocessed_file_path = 'preprocessed_data.json'
    preprocess_json(json_file_path, preprocessed_file_path)

    try:
        with open(preprocessed_file_path, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    def flatten_json(y):
        flat_dict = {}
        def flatten(x, name=''):
            if isinstance(x, dict):
                for a in x:
                    flatten(x[a], name + a + '_')
            elif isinstance(x, list):
                i = 0
                for a in x:
                    flatten(a, name + str(i) + '_')
                    i += 1
            else:
                flat_dict[name[:-1]] = x
        flatten(y)
        return flat_dict

    flat_data = [flatten_json(record) for record in data] if isinstance(data, list) else [flatten_json(data)]

    df = pd.DataFrame(flat_data)

    try:
        df.to_csv(output_file_path, index=False)
        print(f"Data successfully saved to {output_file_path}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

# Example usage
json_file_path = 'data.json'  # Replace with your JSON file path
output_file_path = 'output_table.csv'  # Desired output file path
json_to_table(json_file_path, output_file_path)