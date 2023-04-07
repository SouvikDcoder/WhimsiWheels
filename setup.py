import os
import subprocess

# Read the requirements.txt file and extract package names
with open('requirements.txt', 'r') as req_file:
    requirements = req_file.read().splitlines()
    
# Check if each package is installed and install any missing packages
for requirement in requirements:
    try:
        __import__(requirement)
    except ImportError:
        print(f"{requirement} is not installed. Installing now...")
        subprocess.call(['pip', 'install', requirement])
