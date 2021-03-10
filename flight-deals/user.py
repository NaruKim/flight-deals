import requests

GET_ENDPOINT = "https://api.sheety.co/8aee92b9d053a6a4c35116f530584a6f/copyOfFlightDeals/users"
POST_ENDPOINT = "https://api.sheety.co/8aee92b9d053a6a4c35116f530584a6f/copyOfFlightDeals/users"
PUT_ENDPOINT = "https://api.sheety.co/8aee92b9d053a6a4c35116f530584a6f/copyOfFlightDeals/users/[Object ID]"


def get():
    params = {
    }
    response = requests.get(GET_ENDPOINT, params=params)


def post(n):
    json = {
        "user": {
            "firstName": n['first_name'],
            "lastName": n['last_name'],
            "email": n['email'],
        }
    }
    response = requests.post(POST_ENDPOINT, json=json)
    print(response)
    print(response.text)


def put(n):
    json = {
        "user": {
            "firstName": n['first_name'],
            "lastName": n['last_name'],
            "email": n['email'],
        }
    }
    response = requests.put(PUT_ENDPOINT, json=json)


print("Welcome to Flight Club")

user_data = {
    "first_name": input("What is your First Name?: "),
    "last_name": input("What is your Last Name?: "),
    "email": input("What is your Email?: "),
}

verify_email = None
while user_data['email'] != verify_email:
    verify_email = input("Type your email again: ")

post(user_data)

print("You are in the club")