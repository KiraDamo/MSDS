#Written by Kira Damo

from urllib.request import urlopen, Request    # import Request too
from html.parser import HTMLParser

class WordsParser(HTMLParser):

    search_tags = ['p', 'div', 'span', 'a', 'h1', 'h2', 'h3', 'h4']
    current_tag=''
    common_words = {}
    
    def handle_starttag(self, tag, attrs):
        self.current_tag = tag

    def handle_data(self, data):
        if self.current_tag in self.search_tags:
            for word in data.strip().split():
                common_word = word.lower()
                common_word = common_word.replace('.','')
                common_word = common_word.replace(':','')
                common_word = common_word.replace(',','')
                common_word = common_word.replace('"','')

                if (
                    len(common_word) > 2 and common_word not in ['the', 'and', 'all']
                    and common_word[0].isalpha()
                    ):
                    
                    try:
                        self.common_words[common_word] += 1
                    except:
                        self.common_words.update({common_word: 1})
                        
                
if __name__ == '__main__':

    url = 'https://www.cdm.depaul.edu/'

    h = {'User-Agent': 'Chrome/136.0.0.0'}   # you can use any other browser here
    req = Request(url, headers=h)
    response = urlopen(req)

    html = response.read().decode('utf-8', errors='ignore')
    
    words_parser = WordsParser()

    words_parser.feed(html)

    print(words_parser.common_words)
