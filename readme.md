# HTML Image Scraper

This Python script downloads all image files (`<img>`) from one or more URLs and saves them to a local `images/` directory. It uses `BeautifulSoup` for HTML parsing and `requests` for HTTP operations.

## Features

- Fetches HTML content from a given URL  
- Extracts all `<img src="">` links  
- Automatically handles relative image URLs  
- Downloads each image to a structured directory under `images/<page_title>/`  
- Basic error handling for invalid URLs or failed downloads  

## Requirements

Make sure you have the required packages installed:

```
pip install beautifulsoup4 requests
```

## Usage

Run the script from the command line:

```
python script.py <URL> [<URL2> <URL3> ...]
```

### Examples

Download images from a single page:

```
python script.py https://example.com
```

Download images from multiple pages:

```
python script.py https://example.com https://example2.com
```

## Output

Images are saved inside the `images/` folder under a subfolder named after the page's `<title>`.  
If the page has no title, images are saved under `images/No Title/`.

## Notes

- The script does not currently sanitize filenames. Pages with special characters in their `<title>` tag may cause file system errors.  
- Only direct image links (`<img src="">`) are extracted. Background images (e.g., in CSS) are not included.  
- Relative image paths are resolved using the base URL.  
- If a download fails (e.g. HTTP 403, 404), an error message is shown, and the script continues.  

## License

MIT License – feel free to use and modify.
