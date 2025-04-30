from bs4 import BeautifulSoup
import requests
import os
from sys import argv

def extract_images_from_html(url, html_content: str) -> list[list[str], str]:
    """
    Extracts image URLs from the given HTML content.

    Args:
        html_content (str): The HTML content to parse.

    Returns:
        list: A list of image URLs found in the HTML content.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    images = soup.find_all('img')
    title = soup.title.string if soup.title else 'No Title'

    image_urls = [img['src'] for img in images if 'src' in img.attrs]
    
    print(f"Found {len(image_urls)} images.", image_urls)
    # Handle relative URLs
    for i in range(len(image_urls)):
        if not image_urls[i].startswith('http'):
            image_urls[i] = requests.compat.urljoin(url, image_urls[i])
    return image_urls, title

def extract_html(url: str) -> str:
    """
    Fetches the HTML content from the given URL.

    Args:
        url (str): The URL to fetch the HTML content from.

    Returns:    
        str: The HTML content of the page.
    """
    try:
        response = requests.get(url)
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None


def download_images(url):
    if not os.path.exists('images'):
        os.mkdir('images')
    html_content = extract_html(url)
    if html_content:
        image_urls, title = extract_images_from_html(url, html_content)
        for i, image_url in enumerate(image_urls):
            try:
                response = requests.get(image_url)
                if response.status_code == 200:
                    filename = os.path.join('images', f"{title}/{i}.jpg")
                    with open(filename, 'wb') as f:
                        f.write(response.content)
                    print(f"Downloaded {filename}")
                else:
                    print(f"Failed to download {image_url}: {response.status_code}")
            except requests.RequestException as e:
                print(f"Error downloading the image: {e}")

    else:
        print("Failed to fetch HTML content.")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py <URL>")
        exit(1)
    if not argv[1].startswith('http'):
        print("Please provide a valid URL.")
        exit(1)
    else:
        for i in range(1, len(argv)):
            if not argv[i].startswith('http'):
                print("Please provide a valid URL.")
                exit(1)
            else:
                print(f"Downloading images from {argv[i]}")
                download_images(argv[i])
                print(f"Finished downloading images from {argv[i]}")
                print("--------------------------------------------------")
            print("--------------------------------------------------")
