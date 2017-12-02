import requests
import json



##POSTER
payload = {
            "src" : "393939393939",
            "dst" : "101010101010",
          }
header_data = {"content-type": "application/json"}

flask_url = "http://127.0.0.1:5000/input"

print payload


response = requests.post(url = flask_url, data = json.dumps(payload), headers = header_data)


###GETTER
# header_data = {"content-type": "application/xml"}
# flask_url = "http://127.0.0.1:5000/fwdxml"
# response = requests.get(url = flask_url, headers = header_data)

content =  str(response.content)
print content

#This was something that was rejected outright and made obselote.
