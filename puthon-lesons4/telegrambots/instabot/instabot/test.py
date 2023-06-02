# import requests

# url = "https://youtube-mp36.p.rapidapi.com/dl"

# querystring = {"id":"UxxajLWwzqY"}

# headers = {
# 	"X-RapidAPI-Key": "c2ca2c2bbamshb0ce422c6db8588p180b58jsn02f29913a05c",
# 	"X-RapidAPI-Host": "youtube-mp36.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())

import requests
def audio_yukla_ber(video_id):
  url = "https://youtube-mp36.p.rapidapi.com/dl"

  querystring = {"id":video_id}

  headers = {
    "X-RapidAPI-Key": "7d02d25f3amsh428a3ea7e144132p1b23adjsn1878a89c049d",
    "X-RapidAPI-Host": "youtube-mp36.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers, params=querystring)
  return response.json()['link']
