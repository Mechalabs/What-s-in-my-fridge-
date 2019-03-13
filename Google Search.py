try: 
    from googlesearch import search 
    import requests
    from bs4 import BeautifulSoup

except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = "tomato recipe"
  
for url in search(query, tld="com", num=10, stop=1, pause=2): 
    r = requests.get(url) 
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.prettify())
    print(url)
  
    h6 = soup.find('h6', attrs={'class': 'name'})
    h5 = soup.find('h5', attrs={'class': 'name'})
    h4 = soup.find('h4', attrs={'class': 'name'})
    h3 = soup.find('h3', attrs={'class': 'name'})
    h2 = soup.find('h2', attrs={'class': 'name'})
    h1 = soup.find('h1', attrs={'class': 'name'})
    p = soup.find('p', attrs={'class': 'name'})
    name6 = h6.text.strip()
    name5 = h5.text.strip()
    name4 = h4.text.strip()
    name3 = h3.text.strip()
    name2 = h2.text.strip()
    name1 = h1.text.strip()
    namep = p.text.strip()
    print(name6)
    print(name5)
    print(name4)
    print(name3)
    print(name2)
    print(name1)
    print(namep)