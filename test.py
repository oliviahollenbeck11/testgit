pip install picamera

import os
import time
import picamera2

# Set the path where you want to save the picture
folder_path = '/path/to/folder'

# Create the folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# Capture a picture with the Raspberry Pi camera
with picamera.PiCamera() as camera:
    # Wait for the camera to warm up
    time.sleep(2)
    
    # Generate a unique filename based on the current timestamp
    timestamp = time.strftime('%Y%m%d%H%M%S')
    file_name = f'picture_{timestamp}.jpg'
    file_path = os.path.join(folder_path, file_name)
    
    # Capture the picture and save it to the specified path
    camera.capture(file_path)

    # Print the path where the picture was saved
    print(f'Picture saved: {file_path}')
