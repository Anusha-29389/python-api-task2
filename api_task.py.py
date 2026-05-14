import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users"

try:
    # Fetch data from API
    response = requests.get(url)

    # Check status
    response.raise_for_status()

    # Convert JSON to Python
    users = response.json()

    print("user Details:\n")

    # Display user details
    for user in users:
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"City: {user["address"]['city']}")
        print("-" * 30)
        
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)