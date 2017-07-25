from system.io import FileHandler


def load_news():
    file_handler = FileHandler()
    return file_handler.read_news_xml('static/news/news.xml')


def load_projects():
    file_handler = FileHandler()
    return file_handler.read_projects_xml('static/projects/projects.xml')