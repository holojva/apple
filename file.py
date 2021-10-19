from typing import cast
import requests
from bs4 import BeautifulSoup
url = f"https://kidkodschool.github.io/welcome"
import sys
import random
response = requests.get(url)
query = sys.argv[1] if len(sys.argv) > 1 else input("ima avatara ")
# print(dir(response))
# print(response.status_code)
# print(response.headers)
# with open("./python_is_cool.html", "wb") as f :
#     f.write(response.content)
# query = "cats"
url = f"https://google.com/images?q={query}"
page = requests.get(url).text
soup = BeautifulSoup(page, "html.parser")
count = 0
randnum = random.randint(1, 20)
for raw_img in soup.find_all("img"):
    print("Searching...")
    link = raw_img.get("src")
    alternative = raw_img.get("alt")
    if link and link.startswith("https") and alternative != "Google":
        count += 1
        if randnum == count :
            response = requests.get(link)
            with open(f"./today_avatar.jpg", "wb") as f :
                f.write(response.content)
                print("Found!")
                break
    # elif link and link.startswith("/images/") :
    #     response = requests.get("https://www.google.com" + link)
    #     with open(f"./today_avatar{num}.jpg", "wb") as f :
    #         f.write(response.content)
