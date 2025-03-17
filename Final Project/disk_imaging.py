import subprocess
import os
from pathlib import Path

def list_devices():
    try:
        result = subprocess.run(['lsblk', '-dpo', 'NAME,SIZE,MODEL'], capture_output=True, text=True)
        devices = result.stdout.strip().split('\n')
        return devices
    except Exception as e:
        print(f"Error listing devices: {e}")
        return []

def select_device(devices):
    if not devices:
        print("No devices found.")
        return None

    print("Available devices:")
    for i, device in enumerate(devices):
        print(f"{i + 1}: {device}")

    try:
        choice = int(input("Select a device by number: "))
        if 1 <= choice <= len(devices):
            return devices[choice - 1].split()[0]  # Return the device name (e.g., /dev/sda)
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("Invalid input.")
        return None

def get_output_image_path():
    # Use the current user's Desktop path
    desktop_path = Path.home() / "Desktop"
    default_output_image = desktop_path / "disk_image.img"
    
    print(f"Default output image path: {default_output_image}")
    use_default = input("Do you want to use the default output path? (y/n): ").strip().lower()
    
    if use_default == 'y':
        output_image = default_output_image
    else:
        output_image = input("Enter the path for the output image file: ").strip()
        if not output_image:
            print("Error: Output image path cannot be empty.")
            return None
        output_image = Path(output_image)

    if output_image.exists():
        overwrite = input(f"{output_image} already exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("Operation aborted.")
            return None

    return str(output_image)


def create_disk_image(source_device, output_image):
    if not os.path.exists(source_device):
        print(f"Source device {source_device} does not exist.")
        return
    
    command = ['sudo', 'dd', f'if={source_device}', f'of={output_image}', 'status=progress', 'conv=noerror,sync','bs=4M']
    
    try:
        subprocess.run(command, check=True)
        print(f"Disk image created: {output_image}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating disk image: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Main execution flow
if __name__ == "__main__":
    devices = list_devices()
    source_device = select_device(devices)

    if source_device:
        output_image = get_output_image_path()
        if output_image:  # Proceed only if output_image is valid
            create_disk_image(source_device, output_image)
