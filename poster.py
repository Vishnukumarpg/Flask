import requests
import json


payload = {
            "src" : "666666666666",
            "dst" : "444444444444",
          }
header_data = {"content-type": "application/json"}

flask_url = "http://127.0.0.1:5000/input"

print payload


response = requests.post(url = flask_url, data = json.dumps(payload), headers = header_data)

content =  str(response.content)
print content
