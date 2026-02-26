import requests

url = "https://api.freeapi.app/api/v1/public/books"

response = requests.get(url)
data = response.json()


def fetching_Data(bookIndex):

    if response.status_code == 200 and "data" in data:
        author = data["data"]["data"][bookIndex]["volumeInfo"]["authors"][0]
        category = data["data"]["data"][bookIndex]["volumeInfo"]["categories"][0]
        description = data["data"]["data"][bookIndex]["volumeInfo"]["description"]

        return author, category, description
    else:
        raise Exception("Failed to fetch the data from the URL")


# got_books = fetching_Data()
book_index = int(
    input("Enter the book number you want to get index between(1- 10) : "))
author, category, description = fetching_Data(book_index - 1)


if author:
    print(f"Author is : {author}")
else:
    raise Exception("No author found for this Book.")

if category:
    print(f"Category is : {category}")
else:
    raise Exception("No Category found for this Book.")

if description:
    print(f"Description is : {description}")
else:
    raise Exception("No Description found for this Book.")
