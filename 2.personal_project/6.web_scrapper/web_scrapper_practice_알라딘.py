from requests import get
from bs4 import BeautifulSoup

base_url = "https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Book&SearchWord="
search_term = input("검색어를 입력하세요!: ")

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request the website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("div", class_ = "ss_book_box")
    for book in books:
        contents = book.find_all("li")
        for content in contents:
            anchors = content.find_all("a")
            for anchor in anchors:
                print(anchor)
                print(".......")