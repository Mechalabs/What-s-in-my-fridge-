try: 
    from urllib.request import urlopen
    import webbrowser
    import requests
    from bs4 import BeautifulSoup
    from googlesearch import search

except ImportError:  
    print("No module named 'google' found") 

class Search():

    def __init__(self, ingredients):
        self.tabUrl = "https://www.allrecipes.com/search/?sort=Title&page="
        self.searches = []
        self.array = ingredients
        
        for i in range(len(self.array)):
            temp = ''
            for j in range(len(self.array)):
                if j >= i:
                    temp += self.array[j] + ' '
                    self.searches.append(temp)

    def openResults(self):
        for i in self.searches:
            webbrowser.open(self.tabUrl + i, new = True)

    def returnResults(self):
        for i in self.searches:
            page = requests.get(self.tabUrl + i)
            soup = BeautifulSoup(page.text, 'html.parser')
            for article in soup.select('article'):
                if article['class'] == 'fixed-recipe-card':
                    print(article.text)

    def printUrl(self):
        for i in self.searches:
            print(i)

    def googleSearch(self):
        
        for i in self.searches:
            currentQuery = str(i) + ' recipe'
            for url in search(currentQuery, tld='com', lang='en', num=10, start=0, stop=3, pause=2.0):
                r = requests.get(url)
                print(url)
