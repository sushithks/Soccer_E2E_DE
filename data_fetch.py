import requests

NO_IMAGE = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/No-image-available.png/480px-No-image-available.png'

urls = 'https://en.wikipedia.org/wiki/List_of_North_American_stadiums_by_capacity'

def get_wikipedia_page(url):

    print("Getting wikipedia page...", url)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # check if the request is successful

        return response.text
    except requests.RequestException as e:
        print(f"An error occured: {e}")


print(get_wikipedia_page(urls))