#🟫 libraries -> requests
import requests

#🟦 Input -> API URL
url = "https://jsonplaceholder.typicode.com/users"

#🟩 Logic -> GET request + Loop + process JSON
response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    
    for user in users:
        #🟧 Output -> print()
        print(f"Name: {user['name']}")
        print(f"zipcode: {user['address']['zipcode']}")
        print("------")

else:
    #🟧 Error Output -> print()
    print("Error fetching data")
    
