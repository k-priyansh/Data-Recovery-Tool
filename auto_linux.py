import os
import psutil
import scapy.all as scapy
from loguru import logger
import yara

# Initialize logger
logger.add("scanner.log", rotation="1 week", level="INFO")

# Define the directory to scan
DIRECTORY_TO_SCAN = '/home/user/desktop/disk_image/'
NETWORK_INTERFACE = 'wlan0'  # Adjust as needed

def scan_files(directory):
    logger.info(f"Scanning directory: {directory}")
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            analyze_file(file_path)

def analyze_file(file_path):
    logger.info(f"Scanning file: {file_path}")
    try:
        with open(file_path, 'r', errors='ignore') as f:
            contents = f.read()
            if "suspicious" in contents:
                logger.warning(f"Suspicious content found in {file_path}")
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {e}")

def analyze_system_logs():
    # Example log analysis (update with actual log files or analysis methods if needed)
    log_files = ['/var/log/syslog', '/var/log/auth.log']
    for log_file in log_files:
        if os.path.exists(log_file):
            logger.info(f"Analyzing log file: {log_file}")
            try:
                with open(log_file, 'r', errors='ignore') as f:
                    for line in f:
                        if "error" in line.lower():
                            logger.warning(f"Error found in {log_file}: {line.strip()}")
            except Exception as e:
                logger.error(f"Error reading log file {log_file}: {e}")

def monitor_network():
    logger.info(f"Monitoring network on interface: {NETWORK_INTERFACE}")
    
    def packet_callback(packet):
        logger.info(f"Packet captured: {packet.summary()}")

    scapy.sniff(iface=NETWORK_INTERFACE, prn=packet_callback, count=10)  # Adjust count as needed

def main():
    logger.info("Starting scan...")
    scan_files(DIRECTORY_TO_SCAN)
    analyze_system_logs()
    # monitor_network()
    logger.info("Scan complete.")

if __name__ == "__main__":
    main()
