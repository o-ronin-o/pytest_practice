import requests

db = {
    1: "alice",
    2: "meow",
    3: "omar"
}


def get_user(id):
    print(f"Processed {db.get(id)}")
    return db.get(id)



def get_user_api():
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    if response.status_code == 200: 
        return response.json()

    raise requests.HTTPError
    

