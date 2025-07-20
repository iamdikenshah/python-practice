import requests

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


from api_call.APIClient import APIClient

# Create a GitHub API client
github_api = APIClient(base_url="https://api.github.com")

# Make requests easily
events = github_api.get("/events")
user_data = github_api.get("/users/iamdikenshah")

# Save responses
if 'error' not in events:
    print(github_api.save_to_file(events['data'], "github_events.json"))

if 'error' not in user_data:
    print(github_api.save_to_file(user_data['data'], "dikenshah.json"))