import subprocess
import os

def mount_img(img_path, mount_point):
    # Ensure the mount point exists
    if not os.path.exists(mount_point):
        os.makedirs(mount_point)

    # Mount the image file
    try:
        subprocess.run(['sudo', 'mount', '-o', 'loop', img_path, mount_point], check=True)
        print(f"Mounted {img_path} to {mount_point}")
    except subprocess.CalledProcessError as e:
        print(f"Error mounting image: {e}")

def unmount_img(mount_point):
    # Unmount the image file
    try:
        subprocess.run(['sudo', 'umount', mount_point], check=True)
        print(f"Unmounted {mount_point}")
    except subprocess.CalledProcessError as e:
        print(f"Error unmounting image: {e}")

# Example usage
img_path = '/home/ipriyansh/Desktop/disk_image.img'
mount_point = '/home/ipriyansh/Desktop/disk_image/'

mount_img(img_path, mount_point)

# When you're done with the image
# unmount_img(mount_point)