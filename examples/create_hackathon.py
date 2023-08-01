import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth

source='http://localhost:8000' #Change the source after deploying in AWS
route = '/api/hackathons/create/'
endpoint=source+route

auth = HTTPBasicAuth('admin', 'admin')

files = {
    'background_image': open(r"C:\Users\Sourav\Downloads\challengeConnect_logo.png", 'rb'),
    'hackathon_image': open(r"C:\Users\Sourav\Downloads\challengeConnect_logo.png", 'rb'),
}

data = {
    'title': 'Test Hackathon',
    'description': 'Testing submission types',
    'type_of_submission': 'link',  
    'start_datetime': '2020-08-01T12:00:00Z',
    'end_datetime': '2020-08-07T12:00:00Z',
    'reward_prize': '1000 USD',
}

response = requests.post(endpoint, data=data, files=files,auth=auth)


if response.status_code == 201:
    print('Hackathon created successfully!')
    pprint(response.json()) 
else:
    print('Failed to create hackathon.')
    print(response.status_code)  
    pprint(response.text)  
