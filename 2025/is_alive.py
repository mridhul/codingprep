import requests

def is_alive(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

print(is_alive("https://google.com"))
print(is_alive("https://fdsfdfsdfsdfsdfsdfsdfewr3qfdasfs.com"))