from bs4 import BeautifulSoup
import requests

from library.models import Book

products = 1
url = f"https://www.empik.com/bestsellery/ksiazki?searchCategory=31&hideUnavailable=true&start=1"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
soup_selector = soup.find("div", class_="search-footer")
selector = soup_selector.findAll("a")
last_page = selector[-2]
page_number = int(last_page.get_text())

for _ in range(page_number):
    url = f"https://www.empik.com/bestsellery/ksiazki?searchCategory=31&hideUnavailable=true&start={products}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    soup_selector = soup.findAll("div", class_="search-list-item-hover")
    for selector in soup_selector:
        tag_title_book = selector.find("strong", class_="ta-product-title")
        title_book = tag_title_book.get_text().splitlines()[-1]
        tag_author_name = selector.find("a", class_="smartAuthor")
        author_name = tag_author_name.get_text().splitlines()[-1]
        Book.objects.create(book_title=title_book, author_name=author_name)
    products += 30

