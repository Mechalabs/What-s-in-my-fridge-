import webbrowser

class search():
    def __init__(self):
        self.tabUrl = "https://www.google.com/search?q="
        self.searches = []

    def begin(self):
        ingredients = 'egg, tomato'
        array = ingredients.split(', ')
        
        for i in range(len(array)):
            temp = ''

            for j in range(len(array)):
                if j >= i:
                    temp += array[j] + ', '
                    self.searches.append(temp)

        for i in self.searches:
            webbrowser.open(self.tabUrl + i + 'recipes', new = True)

s = search()
s.begin()