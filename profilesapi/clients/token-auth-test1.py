import requests

def client():
    # credentials = {"username":"jorge", "password":"cabral99"}

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
    #                             data= credentials)

    token_h = "Token 92e61b3da9f0525f4098edbb96c9a4c1bab89047"
    
    headers = {"Authorization": token_h}


    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print("Status Code:", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == '__main__':
    client()