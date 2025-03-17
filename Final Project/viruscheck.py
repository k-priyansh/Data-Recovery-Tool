import os
import subprocess
import hashlib
import requests
import argparse

# Metadata Extraction
def extract_metadata(file_path):
    subprocess.run(['exiftool', file_path])

# File Type Detection
def detect_file_type(file_path):
    subprocess.run(['file', file_path])

# VirusTotal Check
def check_virus_total(file_path, api_key):
    try:
        with open(file_path, 'rb') as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()

        # Check if the file hash exists in VirusTotal
        url = f'https://www.virustotal.com/api/v3/files/{file_hash}'
        headers = {"x-apikey": api_key}

        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print(response.json())
        elif response.status_code == 404:  # File not found, so upload it
            upload_url = 'https://www.virustotal.com/api/v3/files'
            with open(file_path, 'rb') as f:
                files = {'file': f}
                upload_response = requests.post(upload_url, headers=headers, files=files)
                print(upload_response.json())
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Password Cracking
def crack_password(file_path):
    subprocess.run(['office2john', file_path])

# Main function to parse arguments and call appropriate functions
def main():
    parser = argparse.ArgumentParser(description="File Analysis Tool")
    parser.add_argument("file", help="File to analyze")
    parser.add_argument("--metadata", action="store_true", help="Extract metadata")
    parser.add_argument("--filetype", action="store_true", help="Detect file type")
    parser.add_argument("--virustotal", help="Check with VirusTotal (provide API key)")
    parser.add_argument("--crack", action="store_true", help="Crack password")

    args = parser.parse_args()

    if args.metadata:
        extract_metadata(args.file)
    if args.filetype:
        detect_file_type(args.file)
    if args.virustotal:
        check_virus_total(args.file, args.virustotal)
    if args.crack:
        crack_password(args.file)

    # api_key="f549b3c6c918b485e5d60b464827f8135934db568a793ee2091c1351fc5ac3a9"

if __name__ == "__main__":
    main()
