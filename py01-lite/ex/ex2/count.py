import sys
import requests

url = sys.argv[1]
url_2 = sys.argv[2]

response = requests.get(url)

if response.status_code == 200:
  print(response.text.count(url_2))

else:
  print("ERROR:404")