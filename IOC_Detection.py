import hashlib
import requests

def calculate_hash(file_path):
    hash_algo = hashlib.sha256()  # You can use other algorithms like md5 or sha1
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()

def check_iocs(file_hash, known_iocs):
    if file_hash in known_iocs:
        print(f"IOC Detected: {file_hash}")
    else:
        print("No IOC found")

def load_known_iocs(file_path):
    known_iocs = []
    with open(file_path, 'r') as file:
        for line in file:
            known_iocs.append(line.strip())
    return known_iocs

# Load known IOCs from a text file
known_iocs_file_path = 'known_iocs.txt'  # Path to your text file containing hashes
known_iocs = load_known_iocs(known_iocs_file_path)

# Example file hash checking
file_path = 'suspicious_file.txt'  # Path to the file you want to check
file_hash = calculate_hash(file_path)
check_iocs(file_hash, known_iocs)

# Example of using VirusTotal API to get file hash information
api_key = 'YOUR_API_KEY'  # Replace with your VirusTotal API key
file_id = 'your_file_id_here'  # Replace with the actual file ID if available

url = f"https://www.virustotal.com/api/v3/files/{file_id}"
headers = {
    "accept": "application/json",
    "x-apikey": api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    file_data = response.json()
    print(file_data)
else:
    print(f"Failed to retrieve data: {response.status_code} {response.text}")
