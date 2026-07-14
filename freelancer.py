import requests

url = "https://freelancer-api.p.rapidapi.com/find-jobs"
# or
url = "https://freelancer-api.p.rapidapi.com/find-jobs/1"

headers = {
    "x-rapidapi-key": "YOUR_KEY",
    "x-rapidapi-host": "freelancer-api.p.rapidapi.com"
}

r = requests.get(url, headers=headers)

print(r.status_code)
print(r.json())