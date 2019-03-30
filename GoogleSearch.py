try: 
    from urllib.request import urlopen
    import urllib3
    import webbrowser
    import requests
    from bs4 import BeautifulSoup
    from googlesearch import search

except ImportError:  
    print("Missing Library") 

class Search():
    def __init__(self, ingredients):
        self.tabUrl = "https://www.allrecipes.com/search/?sort=Title&page="
        self.searches = []
        self.array = ingredients
        self.stop = 2
        self.pause = 1.0
        self.links = []
        
        for i in range(len(self.array)):
            temp = ''
            for j in range(len(self.array)):
                if j >= i:
                    temp += self.array[j] + ' '
                    self.searches.append(temp)

    def openResults(self):
        for i in self.searches:
            webbrowser.open(self.tabUrl + i, new = True)

    def printUrl(self):
        for i in self.searches:
            print(i)

    def search(self, site):
        site = site.lower()
        for i in self.searches:
            if site == 'all recipes':
                currentQuery = 'site: allrecipes.com' + str(i) + ' recipe'
            
            elif site == 'jamie oliver':
                currentQuery = 'site: jamieoliver.com' + str(i) + ' recipe'
            
            elif site == 'food network':
                currentQuery = 'site: foodnetwork.ca' + str(i) + ' recipe'

            else:
                currentQuery = str(i) + ' recipe'
            
        for url in search(currentQuery, tld='com', lang='en', num=10, start=0, stop=self.stop, pause=self.pause):
            print(url)
            self.links.append(url)
                
# s = Search(['tomato','bread'])
# s.search('food network')