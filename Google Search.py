import webbrowser
tabUrl = "https://www.google.com/search?q="
searches = []

class search():
    ingredients = 'egg, tomato, cheese, potato'
    array = ingredients.split(', ')
    
    for i in range(len(array)):
        temp = ''

        for j in range(len(array)):
            if j >= i:
                temp += array[j] + ', '
                searches.append(temp)

    for i in searches:
        webbrowser.open(tabUrl + i + 'recipes', new = True)
    