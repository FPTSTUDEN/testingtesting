#https://api.chucknorris.io/
import requests
def get_random_joke():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    if response.status_code == 200:
        joke_data = response.json()
        return joke_data['value']
    else:
        return "Failed to retrieve a joke."
if __name__ == "__main__":
    print(get_random_joke())