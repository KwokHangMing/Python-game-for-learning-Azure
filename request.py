import requests
import json

url = "https://api.dialogflow.com/v1/query?v=20150910"
headers = {
    'content-type': 'application/json',
    'Authorization': 'Bearer YOUR_CLIENT_ACCESS_TOKEN',
    'Accept': 'application/json'
}
payload = {
    "contexts": ["shop"],
    "lang": "en",
    "query": "YOUR_QUERY",
    "sessionId": "12345",
    "timezone": "America/New_York"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)
print(response.json)