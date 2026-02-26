import requests

url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"


def fetch_data():

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and "data" in data:
        username = data["data"]["name"]["first"], data["data"]["name"]["last"]
        location = data["data"]["location"]["state"], data["data"]["location"]["country"]
        return username, location

    else:
        raise Exception("Fetching cannnot be done")


def main():
    try:
        username, location = fetch_data()
        print(f"Username : {username}")
        print(f"Country : {location}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
