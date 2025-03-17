import os
import psutil
import winreg
import scapy.all as scapy
import pandas as pd

def scan_files(directory):
    """Scan files in a directory."""
    print(f"Scanning files in {directory}")
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Perform file analysis (e.g., check for signatures)
            print(f"Found file: {file_path}")

def analyze_logs(log_path):
    """Parse and analyze system logs."""
    print(f"Analyzing logs at {log_path}")
    # Open the log file and analyze its contents
    with open(log_path, 'r') as log_file:
        logs = log_file.readlines()
        # Perform analysis on logs (e.g., search for keywords)
        for line in logs:
            if 'error' in line.lower():
                print(f"Error found: {line.strip()}")

def analyze_registry():
    """Analyze Windows registry entries."""
    print("Analyzing Windows registry")
    key = winreg.HKEY_LOCAL_MACHINE
    subkey = r"SOFTWARE\Microsoft\Windows\CurrentVersion"
    try:
        with winreg.OpenKey(key, subkey) as reg_key:
            for i in range(0, winreg.QueryInfoKey(reg_key)[1]):
                value_name, value_data, value_type = winreg.EnumValue(reg_key, i)
                print(f"Registry Value: {value_name} = {value_data}")
    except FileNotFoundError:
        print(f"Registry key {subkey} not found")

def monitor_network(interface):
    """Monitor network activity."""
    print(f"Monitoring network interface {interface}")
    def packet_callback(packet):
        print(f"Packet: {packet.summary()}")
    
    scapy.sniff(iface=interface, prn=packet_callback, count=10)  # Sniff 10 packets

def main():
    scan_files('C:\\path\\to\\directory')
    analyze_logs('C:\\path\\to\\logfile.log')
    analyze_registry()
    monitor_network('eth0')  # Replace with your network interface

if __name__ == "__main__":
    main()
