import json
import csv
import psutil

# Define the path to the log file
# log_file_path = '/var/log/syslog'
log_file_path = '/etc/passwd'
# log_file_path = '/var/log/auth.log'
#log_file_path = '/path/to/your/application.log'
#log_file_path = '/path/to/your/logfile.log'

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

def extract_passwd_info():
    passwd_file_path = '/etc/passwd'
    with open(passwd_file_path, 'r') as file:
        for line in file:
            fields = line.strip().split(':')
            username = fields[0]
            uid = fields[2]
            gid = fields[3]
            print(f'Username: {username}, UID: {uid}, GID: {gid}')

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
    # parse_json_log_file('/path/to/your/json_logfile.json')

    print("\nParsing CSV log file:")
    # Replace with your CSV log file path if needed
    # parse_csv_log_file('/path/to/your/csv_logfile.csv')

    print("\nExtracting /etc/passwd information:")
    extract_passwd_info()

    print("\nGetting system information:")
    get_system_info()
