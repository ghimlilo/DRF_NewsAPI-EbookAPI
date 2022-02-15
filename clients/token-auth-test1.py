from lib2to3.pgen2 import token
from urllib import response
import requests

def client():
    token_h = "Token ba1f6f55e6fb341beee1a81523fc304ee59dd3fa"
    # credentials = {"username" : "admin_4", "password" : "12345"}

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
    #                         data=credentials)

    headers = {"Authorization" : token_h}

    response = requests.get("http://127.0.0.1:8000/api/profiles",
                            headers=headers)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()