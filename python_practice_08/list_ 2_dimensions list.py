Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> aa=[10,20,30]
>>> aa[1]=200
>>> aa
[10, 200, 30]
>>> aa[1:2]=['a','b']
>>> aa
[10, 'a', 'b', 30]
>>> bb=[10,20,30]
>>> bb
[10, 20, 30]
>>> bb[1]=['a','b']
>>> bb
[10, ['a', 'b'], 30]
>>> bb[1][0]
'a'
>>> bb[1][1]
'b'
>>> bb[1]
['a', 'b']
>>> del(bb[1])
>>> bb
[10, 30]
>>> 