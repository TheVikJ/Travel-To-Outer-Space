import requests


def responses() :
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url).json()
    print(response)



if __name__ == "__main__":
    responses()