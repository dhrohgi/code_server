# remoteok 웹사이트 스크래퍼 - 과제

from bs4 import BeautifulSoup
import requests

def extract_jobs(term):

    headers = {"User-Agent": "Daehan"}
    base_url = "https://remoteok.com/remote-"

    response = requests.get(f"{base_url}{term}-jobs", headers=headers)

    if response.status_code != 200:
        print("Can't request to the website!")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("tr", class_="job")
        result = []

        for job_section in jobs:
            job_posts = job_section.find_all("td", class_="company position company_and_position")
            for post in job_posts:
                anchors = post.find_all("a", itemprop="url")
                anchor = anchors[0]
                link = anchor["href"]
                title = anchor.find(itemprop="title")
                company = post.find(itemprop="name")
                regions = post.find_all("div", class_="location")
                regions.pop(-1)
                country = []
                for region in regions:
                    country.append(region.string)
                job_data = {
                    "link": f"https://remoteok.com{link}",
                    "title": title.string.strip(),
                    "company": company.string.strip(),
                    "region": country
                }
                result.append(job_data)
        return result

jobs = extract_jobs("python")
for job in jobs:
    print(job, "\n--------------------------------")