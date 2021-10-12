import requests

url = f"https://kidkodschool.github.io/welcome"

response = requests.get(url)

print(dir(response))
print(response.status_code)
print(response.headers)
# with open("./python_is_cool.html", "wb") as f :
#     f.write(response.content)