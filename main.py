from bs4 import BeautifulSoup

# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
#
# print(soup.title.string)
# print(soup.a)
#
# all_anchor_tag = soup.find_all(name="a")
# print(all_anchor_tag)
# for tag in all_anchor_tag:
#     print(tag.getText())
#     print(tag.get("href"))
#
# all_para_tags = soup.find_all(name="p")
#
# all_heading_tags =soup.find_all(name="h1")
# print(all_heading_tags)


# print(soup.p)

# heading = soup.find(name="h1", id ="name")
# print(heading)

# heading = soup.find(name="h3", class_="heading")
# print(heading)

# company_url = soup.select_one(selector= "p a")
# print(company_url)

from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
print(response.text)
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

# printing the title of the next article
# article_tag = soup.find(name= "a", class_= "storylink")
# print(article_tag)
#
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# print(article_text)
# print(article_link)
#
# article_votes = soup.find(name= "span", class_ = "score").getText()
# print(article_votes)

articles = soup.find_all(name= "a", class_ ="storylink")
print(articles)

article_text = []
article_link = []

for article in articles:
    text = article.getText()
    article_text.append(text)

    link = article.get("href")
    article_link.append(link)

# article_upvotes = soup.find_all(name= "span", class_ = "score")


article_upvotes = [score.getText() for score in soup.find_all(name= "span", class_ = "score")]
print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_text[largest_index])
print(article_link[largest_index])
print(largest_number)





