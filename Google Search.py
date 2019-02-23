import webbrowser
tabUrl = "https://www.google.com/search?q="

class search():
    ingredients = 'egg, tomato, cheese, potato'
    array = ingredients.split(',')
    
    for i in array:
        webbrowser.open(tabUrl + i + ' recipes', new = True)