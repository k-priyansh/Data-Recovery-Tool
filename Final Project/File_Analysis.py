import hashlib
import os

def calculate_hash(file_path, algorithm='md5'):
    try:
        hash_func = getattr(hashlib, algorithm)()
    except AttributeError:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}")
    
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return None
    
    return hash_func.hexdigest()

def analyze_directory(directory, algorithm='md5'):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path, algorithm)
            if file_hash:
                print(f"File: {file_path}, {algorithm.upper()}: {file_hash}")

# Example usage
analyze_directory("extracted_files/", algorithm='sha256')
