
import requests
import json
import os

class APIClient:
    def __init__(self, base_url=None, headers=None):
        self.base_url = base_url or ""
        self.headers = headers or {}
    
    def get(self, endpoint, params=None):
        """Make a GET request"""
        try:
            url = f"{self.base_url}{endpoint}" if self.base_url else endpoint
            response = requests.get(url, params=params, headers=self.headers)
            response.raise_for_status()  # Raises exception for bad status codes
            return {
                'status_code': response.status_code,
                'data': response.json(),
                'raw': response.text
            }
        except requests.exceptions.RequestException as e:
            return {'error': str(e), 'status_code': None}
    
    def post(self, endpoint, data=None, json_data=None):
        """Make a POST request"""
        try:
            url = f"{self.base_url}{endpoint}" if self.base_url else endpoint
            response = requests.post(url, data=data, json=json_data, headers=self.headers)
            response.raise_for_status()
            return {
                'status_code': response.status_code,
                'data': response.json(),
                'raw': response.text
            }
        except requests.exceptions.RequestException as e:
            return {'error': str(e), 'status_code': None}
    
    def save_to_file(self, data, filename, folder="api_call"):
        """Save API response to a file"""
        try:
            # Create folder if it doesn't exist
            if not os.path.exists(folder):
                os.makedirs(folder)
            
            filepath = os.path.join(folder, filename)
            with open(filepath, 'w') as file:
                if isinstance(data, dict):
                    json.dump(data, file, indent=2)
                else:
                    file.write(str(data))
            return f"Data saved to {filepath}"
        except Exception as e:
            return f"Error saving file: {str(e)}"

# Usage examples:
if __name__ == "__main__":
    # GitHub API client
    github_client = APIClient(base_url="https://api.github.com")
    
    # Get GitHub events
    events = github_client.get("/events")
    if 'error' not in events:
        print(f"Status: {events['status_code']}")
        print(github_client.save_to_file(events['data'], "github_events.json"))
    else:
        print(f"Error: {events['error']}")
    
    # Get user profile
    user = github_client.get("/users/iamdikenshah")
    if 'error' not in user:
        print(f"Status: {user['status_code']}")
        print(github_client.save_to_file(user['data'], "dikenshah.json"))
    else:
        print(f"Error: {user['error']}")
    
    # General API client (for any API)
    general_client = APIClient()
    response = general_client.get("https://jsonplaceholder.typicode.com/posts/1")
    if 'error' not in response:
        print(f"Status: {response['status_code']}")
        print(response['data'])