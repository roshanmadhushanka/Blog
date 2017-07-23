import xml.etree.ElementTree as ET

# News update
NEWS_ROOT = "news"
NEWS_TAGS = ['title', 'content', 'image', 'reference']

# Projects update


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
            if node.tag == NEWS_ROOT:
                news = {}
                for column in node:
                    if column not in NEWS_TAGS:
                        print "Invalid tag :", column
                        break
                    news[column.tag] = str(column.text).strip()
                news_list.append(news)
        return news_list

    def read_projects_xml(self, file_name):
        tree = ET.parse(file_name)
