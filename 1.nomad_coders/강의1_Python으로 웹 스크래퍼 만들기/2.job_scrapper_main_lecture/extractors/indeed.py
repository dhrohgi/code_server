from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def get_page_count(keyword):
    base_url = "https://kr.indeed.com/jobs?q="

    # 셀레니움으로 스크래핑을 하기 위한 준비
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)
    browser.get(f"{base_url}{keyword}")


    if browser.page_source == None:
        print("Can't request page")
    else:
        soup = BeautifulSoup(browser.page_source, "html.parser")
        pagination = soup.find("nav", role="navigation")
        if pagination == None:
            return 1
        pages = pagination.find_all("div", class_="css-tvvxwd")
        count = len(pages)
        if count > 5:
            return 5
        else:
            return count



def extract_indeed_jobs(keyword):    
    pages = get_page_count(keyword)
    print("Found", pages, "page")
    
    results = []
    
    for page in range(pages):
        base_url = "https://kr.indeed.com/jobs"
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        print("Requesting", final_url)

        # 셀레니움으로 스크래핑을 하기 위한 준비
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        browser = webdriver.Chrome(options=options)
        browser.get(final_url)


        if browser.page_source == None:
            print("Error")
        else:            
            soup = BeautifulSoup(browser.page_source, "html.parser")
            job_list = soup.find("ul", class_="css-zu9cdh eu4oa1w0")
            jobs = job_list.find_all("li", recursive=False)
            for job in jobs:
                zone = job.find("div", class_="mosaic-zone")
                if zone == None:
                    anchor = job.select_one("h2 a")
                    title = anchor["aria-label"]
                    link = anchor["href"]
                    company = job.find("span", class_="companyName")
                    location = job.find("div", class_="companyLocation")
                    job_data = {
                        'link': f"https://kr.indeed.com{link}",
                        'company': company.string.replace(","," "),
                        'location': location.string.replace(","," "),
                        'position': title.replace(","," ")
                    }
                    results.append(job_data)
    return results

