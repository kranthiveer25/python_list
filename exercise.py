import requests as re
from bs4 import BeautifulSoup
import os

URL = "https://www.kaggle.com"
response = re.get(URL)

if response.status_code != 200:
    print("HTTP connection is not successful. Try again.")
else:
    print("HTTP connection is successful.")
    soup = BeautifulSoup(response.content, "html.parser")
    title_with_tags = soup.title
    if title_with_tags:
        print("Title with tags:", title_with_tags)
        print("Title without tags:", title_with_tags.text)
    else:
        print("No title found in the HTML content.")

for link in soup.find_all("link"):
    print(link.get("href"))
print(soup.get_text())

folder = "mini_dataset"

if not os.path.exists(folder):
    os.mkdir(folder)

def scrape_content(URL):
    response = re.get(URL)
    if response.status_code == 200:
        print("HTTP connection is successful for the URL:", URL)
        return response
    else:
        print("HTTP connection is not successful for the URL:", URL)
        return None

path = os.getcwd() + "/" + folder  # Use os.getcwd() instead of os.getcwdb()

def save_html(to_where, text, name):
    file_name = name + ".html"  # Add the file extension ".html"
    with open(os.path.join(to_where, file_name), "w") as f:  # Corrected "w" for write mode
        f.write(text)

test_text = response.text
save_html(path, test_text, "example")

URL_list = [
    "https://www.kaggle.com",
    "https://stackoverflow.com",
    "https://www.researchgate.net",
    "https://www.python.org",
    "https://www.w3schools.com",
    "https://wwwen.uni.lu",
    "https://github.com",
    "https://scholar.google.com",
    "https://www.mendeley.com",
    "https://www.overleaf.com"
]
def create_mini_dataset(to_where, URL_list):
    for i in range(0, len(URL_list)):
        content = scrape_content(URL_list[i])
        if content is not None:
            save_html(to_where, content.text, str(i))
        else:
            pass
    print("Mini dataset is created!")


create_mini_dataset(path, URL_list)
