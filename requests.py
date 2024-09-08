import requests
#test edit2
url="https://www.weather.reports.up.com"
response=requests.get(url)
if requests.status_code==200:
  print(response.json())
else:
  print(f'{requests.status_code} is not working please check it again')
  
