import os
import requests

# Define the file paths and URLs
data_folder = 'data'
quran_file = os.path.join(data_folder, 'QuranCompiled.csv')

# URLs to download the files
quran_compiled_url = 'https://raw.githubusercontent.com/furqanx11/SimilarVerse-Backend/main/data/QuranCompiled.csv'


def ensure_data_folder_exists(folder_path):
    """Ensure the data folder exists."""
    os.makedirs(folder_path, exist_ok=True)

def download_file(url, file_path):
    """Download a file from a URL to a specified file path."""
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {file_path}")

def check_and_download_file(file_path, url):
    """Check if a file exists, else download it from the specified URL."""
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist. Downloading...")
        download_file(url, file_path)
    else:
        print(f"{file_path} already exists.")

def main():
    """Main function to ensure data folder exists and download necessary files."""
    ensure_data_folder_exists(data_folder)
    check_and_download_file(quran_file, quran_compiled_url)
