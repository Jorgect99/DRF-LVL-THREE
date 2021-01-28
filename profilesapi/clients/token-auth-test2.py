import requests

def client():

    # data = {
    #     "username":"topo", 
    #     "email":"topo@gmail.com", 
    #     "password1":"changeme123",
    #     "password2":"changeme123",
    #     }

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
    #                             data= data)

    token_h = "Token 4b4bdb562122771de2d8fab0a39f637092b35176"
    
    headers = {"Authorization": token_h}


    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print("Status Code:", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == '__main__':
    client()