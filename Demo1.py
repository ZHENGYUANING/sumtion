import urllib.request
import urllib.parse

# url = 'http://www.baidu.com'
# req = urllib.request.urlopen(url)
# print(req.read().decode('utf-8'))
# print(req.getheader('server'))

url = 'http://httpbin.org/post'

data = bytes(urllib.parse.urlencode({'htllo':'word'}),encoding='utf-8',timeout=2)

req = urllib.request.urlopen(url,data)

print(req.status)

print(req.read())

