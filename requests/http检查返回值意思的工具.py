import requests

try:
    url = 'https://httpbin.org/status/403'
    response = requests.get(url)
    response.raise_for_status()

except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
