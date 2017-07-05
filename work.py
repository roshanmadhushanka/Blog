import xml.etree.ElementTree as ET

NEWS_TAG = "news"
TITLE = "title"
CONTENT = "content"
IMAGE = "image"
REFERENCE = "reference"


tree = ET.parse("static/news/news.xml")
root = tree.getroot()

news_list = []
for node in root:
    if node.tag == NEWS_TAG:
        news = {}
        for column in node:
            news[column.tag] = str(column.text)
        news_list.append(news)
