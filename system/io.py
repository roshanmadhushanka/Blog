import xml.etree.ElementTree as ET

# News update
NEWS_TAG = "news"
TITLE = "title"
CONTENT = "content"
IMAGE = "image"
REFERENCE = "reference"

class FileHandler:
    def read(self, file_name):
        fp = None
        try:
            fp = open(file_name, 'r')
            return fp.read()
        except IOError:
            print(file_name, " not found!")
            return ""
        finally:
            if fp is not None:
                fp.close()

    def readLines(self, file_name):
        fp = None
        try:
            fp = open(file_name, 'r')
            return fp.readlines()
        except IOError:
            print(file_name, " not found!")
            return []
        finally:
            if fp is not None:
                fp.close()

    def read_news_xml(self, file_name):
        tree = ET.parse(file_name)
        root = tree.getroot()

        news_list = []
        for node in root:
            if node.tag == NEWS_TAG:
                news = {}
                for column in node:
                    news[column.tag] = str(column.text).strip()
                news_list.append(news)
        return news_list