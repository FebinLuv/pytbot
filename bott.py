import requests
from bs4 import BeautifulSoup

# specify the URL of the job search page
URL = "https://in.indeed.com/jobs?q=digital%20marketing&l=pune&from=searchOnHP"

# send a GET request to the website
page = requests.get(URL)

# parse the HTML content
soup = BeautifulSoup(page.content, "html.parser")

# find all job listings on the page
job_listings = soup.find_all("div", class_="jobsearch-SerpJobCard")

# print the job title and company name for each listing
for listing in job_listings:
    title = listing.find("a", class_="jobtitle").text.strip()
    company = listing.find("span", class_="company").text.strip()
    print(f"{title} - {company}")
