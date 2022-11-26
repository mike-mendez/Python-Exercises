import re

url ="https://www.google.com/maps/place/CAFE+REISSUE/@35.6711763,139.6904488,15z/data=!3m1!5s0x60188ca3399572bd:0xc73f0eb2ca1f1e20!4m10!1m2!2m1!1scafe!3m6!1s0x60188ca339bc257f:0xc312aa30dd798189!8m2!3d35.6711763!4d139.7079583!15sCgRjYWZlWgYiBGNhZmWSAQtjb2ZmZWVfc2hvcOABAA!16s%2Fg%2F11c55bqbws"
test = re.sub(r'@.+/', "", url)
print(test)
print(url)
