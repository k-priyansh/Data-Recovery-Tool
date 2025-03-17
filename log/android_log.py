import subprocess
import os

# Define the path to the log file
log_file_path = '/path/to/your/logfile.log'

def parse_log_file(path):
    if os.path.exists(path):
        with open(path, 'r') as file:
            for line in file:
                # Process each line (e.g., print it or extract information)
                print(line.strip())
    else:
        print("Log file does not exist.")

def extract_logcat_logs():
    try:
        # Run adb logcat command and save output to a file
        logcat_output = subprocess.check_output(['adb', 'logcat', '-d'], universal_newlines=True)
        with open(log_file_path, 'w') as file:
            file.write(logcat_output)
        print("Logcat logs extracted to", log_file_path)
    except subprocess.CalledProcessError as e:
        print(f"Error extracting logcat logs: {e}")

def get_system_info():
    try:
        # Run adb shell commands to get system information
        cpu_info = subprocess.check_output(['adb', 'shell', 'cat', '/proc/cpuinfo'], universal_newlines=True)
        mem_info = subprocess.check_output(['adb', 'shell', 'cat', '/proc/meminfo'], universal_newlines=True)
        print("CPU Information:")
        print(cpu_info)
        print("Memory Information:")
        print(mem_info)
    except subprocess.CalledProcessError as e:
        print(f"Error getting system information: {e}")

if __name__ == "__main__":
    print("Extracting logcat logs:")
    extract_logcat_logs()

    print("\nParsing log file:")
    parse_log_file(log_file_path)

    print("\nGetting system information:")
    get_system_info()
