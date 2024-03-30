import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_and_save_css(website):
    '''
    This function fetches css from any website and saves the output to a file.
    :param website: the website in which you will like to scrape
    '''
    # Ensure the website includes the scheme (http:// or https://)
    if not website.startswith(('http://', 'https://')):
        website = f"https://{website}"

    response = requests.get(website)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all link elements that have a rel attribute equal to 'stylesheet'
    css_links = soup.find_all('link', {'rel': 'stylesheet'})

    for idx, link in enumerate(css_links, start=1):
        # Resolve the CSS file's absolute URL (in case it's relative)
        css_href = urljoin(website, link['href'])
        css_response = requests.get(css_href)

        # Define a file name for the CSS content
        css_filename = f"css_file_{idx}.css"

        # Save the CSS file content to a new file
        with open(css_filename, 'w') as css_file:
            css_file.write(css_response.text)
            print(f"Saved CSS from {css_href} to {css_filename}")

if __name__ == "__main__":
    website = input("Enter the website you want to target for CSS (without https://): ")
    fetch_and_save_css(website)
    print("Finished scraping CSS.")
