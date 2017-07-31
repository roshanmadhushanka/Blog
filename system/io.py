import xml.etree.ElementTree as ET

# News update
NEWS_ROOT = "news"
NEWS_TAGS = ['title', 'content', 'image', 'reference']

# Projects update
PROJECT_ROOT = "project"
PROJECT_TAGS = ['title', 'description', 'image', 'link', 'tag']


class FileHandler:
    def __init__(self):
        return

    def read(self, file_name):
        '''
        Read a file
        :param file_name: File name to be read
        :return: String of content
        '''

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

    def read_lines(self, file_name):
        '''
        Read a file
        :param file_name: File name to be read
        :return: List of lines in the file
        '''

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
        '''
        Read News from XML
        :param file_name: XML file name to be read
        :return: List of news
        '''

        tree = ET.parse(file_name)
        root = tree.getroot()

        news_list = []
        for node in root:
            if node.tag == NEWS_ROOT:
                news = {}
                for column in node:
                    if column.tag not in NEWS_TAGS:
                        print "Invalid tag :", column
                        break
                    news[column.tag] = str(column.text).strip()
                news_list.append(news)
        return news_list

    def read_projects_xml(self, file_name):
        '''
        Read projects from XML
        :param file_name: XML file name to be read
        :return: List of projects
        '''

        tree = ET.parse(file_name)
        root = tree.getroot()

        project_list = []
        for node in root:
            if node.tag == PROJECT_ROOT:
                project = {}
                for column in node:
                    if column.tag not in PROJECT_TAGS:
                        print "Invalid tag :", column
                        break
                    project[column.tag] = column
                project_list.append(project)
        return project_list
