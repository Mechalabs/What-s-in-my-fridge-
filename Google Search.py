import webbrowser
tabUrl = "https://www.google.com/search?q="
totalSearch = []

class search():
    ingredients = 'egg, tomato, cheese, potato'
    array = ingredients.split(',')
    
    for i in range(len(array)):
        #webbrowser.open(tabUrl + array[i] + ' recipes', new = True)
        totalSearch.append(array[i])
        temp = ''
        print('loading')

        for j in range(len(array)):
            if j <= i:
                temp += array[j] + ', '
                print('loading..')
                
                for k in totalSearch:
                    if temp != k:
                        totalSearch.append(array[j])
                        print('loading....')
                        break

print(totalSearch)