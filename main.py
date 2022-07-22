import requests
import json

searchterms = input("What keyword would you like to search? EX. Python > ")
location = input("Where would you like to search?")

url = "https://linkedin-jobs-search.p.rapidapi.com/"

payload = {
	"search_terms": str(searchterms),
	"location": str(location),
	"page": "1",
	"fetch_full_text": "yes"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "a8d4419650msh7397b85e8950129p111a20jsn6505c0588d46",
	"X-RapidAPI-Host": "linkedin-jobs-search.p.rapidapi.com"
}

r = requests.request("POST", url, json=payload, headers=headers)

orders = json.loads(r.content)
formatted = json.dumps(orders, indent=4)

with open("linkedin.json", "w") as f:
    f.write(formatted)



url = "https://indeed11.p.rapidapi.com/"

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "a8d4419650msh7397b85e8950129p111a20jsn6505c0588d46",
	"X-RapidAPI-Host": "indeed11.p.rapidapi.com"
}

r = requests.request("POST", url, json=payload, headers=headers)

orders = json.loads(r.content)
formatted = json.dumps(orders, indent=4)

with open("indeed11.json", "w") as f:
    f.write(formatted)




url = "https://indeed-search-results-scraper1.p.rapidapi.com/scrape_indeed_results_by_search/"

payload = {
	"country": "us",
	"location": str(location),
	"page": 1,
	"keyword": str(searchterms),
	"days_old": 1
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "a8d4419650msh7397b85e8950129p111a20jsn6505c0588d46",
	"X-RapidAPI-Host": "indeed-search-results-scraper1.p.rapidapi.com"
}

r = requests.request("POST", url, json=payload, headers=headers)


orders = json.loads(r.content)
formatted = json.dumps(orders, indent=4)

with open("indeed.json", "w") as f:
    f.write(formatted)

print("Finished Scraping 3 API's - LinkedIn - Indeed - Indeed11")
print("linkedin.json, indeed.json, indeed11.json")