import os
import requests
from urllib.parse import urlparse
import hashlib

# Directory to store fetched images
IMAGE_DIR = "Fetched_Images"


def create_directory():
    """
    Create the directory for fetched images if it doesn't exist.
    """
    os.makedirs(IMAGE_DIR, exist_ok=True)


def generate_filename(url, content):
    """
    Generate a safe filename from the URL.
    If no filename is available, generate one from a hash of the content.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    if not filename:  # If the URL doesn't provide a filename
        # Use a hash of the content for uniqueness
        file_hash = hashlib.md5(content).hexdigest()
        filename = f"image_{file_hash}.jpg"

    return filename


def fetch_image(url):
    """
    Fetch and save an image from the given URL.
    Implements Ubuntu principles: community, respect, sharing, practicality.
    """
    try:
        # Respectful request with headers (mimicking a browser)
        headers = {
            "User-Agent": "UbuntuFetcher/1.0 (Respectful Bot)",
            "Accept": "image/*"
        }
        response = requests.get(url, headers=headers, timeout=10)

        # Raise HTTP errors (404, 500, etc.)
        response.raise_for_status()

        # Check if content is actually an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"⚠️ Skipping {url} - Not an image (Content-Type: {content_type})")
            return

        # Prevent duplicate downloads
        filename = generate_filename(url, response.content)
        filepath = os.path.join(IMAGE_DIR, filename)
        if os.path.exists(filepath):
            print(f"⏩ Skipping {url} - Duplicate image already downloaded.")
            return

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Successfully fetched: {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching {url}: {e}")


def main():
    """
    Main function to run the Ubuntu-Inspired Image Fetcher.
    Handles both single and multiple URLs.
    """
    create_directory()

    # Prompt user for one or multiple URLs
    urls = input("🌍 Enter image URL(s), separated by spaces:\n> ").split()

    for url in urls:
        fetch_image(url)


if __name__ == "__main__":
    main()
