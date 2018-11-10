import urllib.request

u = urllib.request.urlopen("http://www.example.com")
print(u.read())
