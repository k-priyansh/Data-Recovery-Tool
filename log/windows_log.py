import json
import csv
import winreg
import psutil

# Define the path to the log file
log_file_path = r'C:\path\to\your\logfile.log'

def parse_log_file(path):
    with open(path, 'r') as file:
        for line in file:
            # Process each line (e.g., print it or extract information)
            print(line.strip())

def parse_json_log_file(path):
    with open(path, 'r') as file:
        logs = json.load(file)
        for entry in logs:
            # Process each JSON entry
            print(entry)

def parse_csv_log_file(path):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Process each row (as a dictionary)
            print(row)

def extract_registry_info():
    try:
        # Example of reading from a registry key
        key_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion'
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
            value, regtype = winreg.QueryValueEx(key, 'ProgramFilesDir')
            print(f'ProgramFilesDir: {value}')
    except FileNotFoundError:
        print("Registry key not found")
    except OSError as e:
        print(f"Error accessing the registry: {e}")

def get_system_info():
    # Get system CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f'CPU Usage: {cpu_usage}%')

    # Get system memory usage
    memory_info = psutil.virtual_memory()
    print(f'Total Memory: {memory_info.total}, Available Memory: {memory_info.available}')

if __name__ == "__main__":
    print("Parsing log file:")
    parse_log_file(log_file_path)

    print("\nParsing JSON log file:")
    # Replace with your JSON log file path if needed
    # parse_json_log_file(r'C:\path\to\your\json_logfile.json')

    print("\nParsing CSV log file:")
    # Replace with your CSV log file path if needed
    # parse_csv_log_file(r'C:\path\to\your\csv_logfile.csv')

    print("\nExtracting registry information:")
    extract_registry_info()

    print("\nGetting system information:")
    get_system_info()
