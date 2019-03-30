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

    def googleSearch(self):
        
        for i in self.searches:
            currentQuery = str(i) + ' recipe'
            for url in search(currentQuery, tld='com', lang='en', num=10, start=0, stop=3, pause=2.0):
                r = requests.get(url)
                print(url)

    def allRecipes(self):
        for i in self.searches:
            currentQuery = 'site: allrecipes.com ' + str(i) + ' recipe'
            for url in search(currentQuery, tld='com', lang='en', num=10, start=0, stop=3, pause=1.0):
                print(url)

'''             TO DO LATER
                http = urllib3.PoolManager()
                r = http.request('GET', url)
                soup = BeautifulSoup(r.data, 'html.parser')

                for p in soup.select('li'):
                    if p['class'] == 'checkList__line':
                        print(p.text)
'''
s = Search(['tomato','bread'])
s.allRecipes()