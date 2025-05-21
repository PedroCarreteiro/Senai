import requests

url = "https://g1.globo.com/"
response = requests.get(url)

print(response.status_code)

