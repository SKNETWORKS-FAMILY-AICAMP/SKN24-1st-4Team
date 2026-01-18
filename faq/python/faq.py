
import requests
from bs4 import BeautifulSoup
items = bs.select("ul.general_board2 dl")

for item in items:
    title = item.select_one("dt a")
    answer = item.select_one("dd")

    if not title or not answer:
        continue

    print(title.get_text(strip=True))
    print(answer.get_text(strip=True))
    print("-" * 30)
