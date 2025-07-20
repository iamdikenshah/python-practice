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