#3.8
countries = ['испания', 'норвегия', 'исландия', 'южная корея', 'япония']
print(countries)
print(sorted(countries))
print(countries)
print(sorted(countries, reverse=True))
print(countries)
countries.reverse()
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
print("\n")

#3.9 упражнение выполнено в файле lists_medium_level.py

#3.10 испробовать все функции из главы
languages = ['java', 'python', 'c', 'assembler']
print(languages)
print(languages[0])
print(languages[1].title())
print(languages[-2])
languages[2] = 'js'
print(languages)
languages.append('php')
print(languages)
languages.insert(0, 'html')
print(languages)
del languages[0]
print(languages)
print(languages.pop())
languages.remove('java')
print(languages)
languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)
print(sorted(languages))
print(languages)
languages.reverse()
print(languages)
print(len(languages))
