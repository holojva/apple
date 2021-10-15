from typing import cast
import requests
from bs4 import BeautifulSoup
url = f"https://kidkodschool.github.io/welcome"

response = requests.get(url)

print(dir(response))
print(response.status_code)
print(response.headers)
# with open("./python_is_cool.html", "wb") as f :
#     f.write(response.content)
query = "cats"
url = f"https://kiddle.co/s.php?q={query}"
page = requests.get(url).text
soup = BeautifulSoup(page, "html.parser")
print(soup)
for raw_img in soup.find_all("img"):
    link = raw_img.get("src")
    if link and link.startswith("https") :
        response = requests.get(link)
        with open("./today_avatar.jpg", "wb") as f :
            f.write(response.content)
        break