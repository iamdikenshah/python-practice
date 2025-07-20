import requests
from api_client import APIClient

request = requests.get('https://api.github.com/events')
print(request.status_code)  # Should print 200 if the request was successful
print(request.json())  # Print the JSON response from the API

with open("api_call/github_events.json", "w") as file:
    file.write(request.text)  # Save the response to a file
print("Data saved to api_call/github_events.json")



request = requests.get('https://api.github.com/users/iamdikenshah')
print(request.status_code)  # Should print 200 if the request was successful
print(request.json())  # Print the JSON response from the API

with open("api_call/dikenshah.json", "w") as file:
    file.write(request.text)  # Save the response to a file
print("Data saved to api_call/dikenshah.json")



# Create a GitHub API client
github_api = APIClient(base_url="https://api.github.com")

# Get user data and download profile image
user_data = github_api.get("/users/iamdikenshah")

if 'error' not in user_data:
    print(github_api.save_to_file(user_data['data'], "dikenshah.json"))
    
    # Download user's avatar image
    avatar_url = user_data['data']['avatar_url']
    print(github_api.download_image(avatar_url, "dikenshah_avatar.png"))

# Download any image directly
image_result = github_api.download_image(
    "https://avatars.githubusercontent.com/u/12345?v=4", 
    "sample_avatar.jpg"
)
print(image_result)