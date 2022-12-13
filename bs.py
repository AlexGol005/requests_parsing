from bs4 import BeautifulSoup

# soup = BeautifulSoup('<a></b></a>', 'lxml')
# print(soup)
# with open()
with open('2.txt', 'r', encoding='utf-8') as f:
    s = BeautifulSoup(f, 'lxml')


print(s.title.text)
