import requests
import schedule
import time

# Downloading function as before
def download_phishing_data(url, file_path):
    response = requests.get(url)
    with open(file_path, 'w') as file:
        file.write(response.text)
    print("Phishing data updated.")

# New function to load phishing URLs from file
def load_phishing_urls(file_path):
    with open(file_path, 'r') as file:
        return set(file.read().splitlines())

# New function to check if a URL is a phishing URL
def is_phishing_url(url, phishing_urls):
    return url in phishing_urls

# Initial setup
openphish_url = 'https://openphish.com/feed.txt'
local_file_path = 'feed.txt'
download_phishing_data(openphish_url, local_file_path)
phishing_urls = load_phishing_urls(local_file_path)

# Schedule the update function
schedule.every(12).hours.do(download_phishing_data, openphish_url, local_file_path)

while True:
    schedule.run_pending()
    phishing_urls = load_phishing_urls(local_file_path)
    test_url = input("Enter a URL to check (or 'exit' to quit): ")
    if test_url.lower() == 'exit':
        break
    if is_phishing_url(test_url, phishing_urls):
        print(f"The URL '{test_url}' is a phishing site.")
    else:
        print(f"The URL '{test_url}' is not listed as a phishing site.")

    time.sleep(1)