from bs4 import BeautifulSoup
from requests import get

response = get(url="https://news.ycombinator.com/")
yc_news = response.text

soup = BeautifulSoup(yc_news, "html.parser")
articles = soup.select(".titleline")
article_titles = []
article_links = []
for article in articles:
    article_titles.append(article.get_text())
    article_links.append(article.find("a").get("href"))
upvotes = soup.select(".score")
article_upvotes = []
for upvote in upvotes:
    article_upvotes.append(int(upvote.get_text().split()[0]))

most_upvotes_index = article_upvotes.index(max(article_upvotes))

print(article_titles[most_upvotes_index])
print(article_links[most_upvotes_index])
print(article_upvotes[most_upvotes_index])

# print(article_titles)
# print(article_links)
# print(article_upvotes)
