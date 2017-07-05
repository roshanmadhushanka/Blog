from system.io import FileHandler


def load_news():
    file_handler = FileHandler()
    return file_handler.read_news_xml('static/news/news.xml')
