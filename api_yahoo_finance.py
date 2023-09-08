import requests
import json

symbols = ["AAPL", "BA", "T", "MGM", "AMZN", "IBM", "TSLA", "GOOG"]
url = "https://yahoo-finance127.p.rapidapi.com/esg-score/"

headers = {
	"X-RapidAPI-Key": "d16667ccbdmsh2c98a919f9decedp1b6e22jsn2d964a84e911",
	"X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
}

esg_scores = []
for sym in symbols:
    response = requests.get(url+sym, headers=headers)
    esg_scores.append({sym:response.json()})


esgFile = open("datasets\esg_scores.json", "w")
esgFile.write(json.dumps(esg_scores))
esgFile.close()