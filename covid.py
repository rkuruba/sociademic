import requests
import json

url = "http://data.fixer.io/api/latest/?apikey=b038545c7fc087f5cedd8e60294324cf"

# Make request and store response
response = requests.get(url)

# Print status code
print(response.status_code)
