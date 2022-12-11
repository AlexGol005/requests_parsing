import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

r = requests.get('https://fgis.gost.ru/fundmetrology/cm/results/1-206906310', headers=headers)
# print(r)
# print(dir(r))
# print(r.headers)
# print(r.raw)
# print(r.status_code)
print(r.content)
# print(r.text)
url ='https://klike.net/uploads/posts/2019-05/1556708032_1.jpg'
# r = requests.get(url, headers=headers, stream=True)
# with open('1.jpg', 'wb') as fd:
#     for chunk in r.iter_content(chunk_size=1024*10):
#         fd.write(chunk)

# r = requests.get(url, headers=headers)
# with open('2.jpg', 'wb') as fd:
#     fd.write(r.content)

name = url.split('/')[-1]
r = requests.get(url, headers=headers)
with open(name, 'wb') as fd:
    fd.write(r.content)




