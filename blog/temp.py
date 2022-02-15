import requests
from bs4 import BeautifulSoup

url = "https://optinmonster.com/73-type-of-blog-posts-that-are-proven-to-work/"
res = requests.get(url=url)

results = []
soup = BeautifulSoup(res.text, "html.parser")
i = 0
if soup:
    all_h3 = soup.find_all("h3")
    for h3 in all_h3:
        i += 1
        if i < 10:
            results.append(h3.text.strip().replace("\xa0", "")[3:])
        else:
            results.append(h3.text.strip().replace("\xa0", "")[4:])

    print(results)