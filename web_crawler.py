from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin

from html_parser import Collector

class Crawler(object):

    def __init__(self):
        self.visited = set()
        
    def crawl(self, url):
        'recursive web crawler that calls analyze'
        links = self.analyze(url)
        self.visited.add(url)
        for link in links:
            try:
                if link not in self.visited:
                    self.crawl(link)
            except:
                pass

    def analyze(self, url):
        'returns the list of URLs found in the parser'
        print("Visiting ", url)
        content = urlopen(url).read().decode()
        collector = Collector(url)
        collector.feed(content)
        urls = collector.getLinks()
        return urls
