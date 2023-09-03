import requests
import json
api_url = "https://api.github.com/repos/kpsherva/gh-manage/issues/2/labels"
response = requests.get(api_url)
resp = response.json()
name = resp[0].get('name')
print("label's name: " , name)

