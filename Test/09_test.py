s = set()
s.add(18)
s.add("18")

print(s) # {18, '18'}

ss = set()
ss.add(20)
ss.add(20.0)
ss.add('20')
print(ss) # {20, '20'}
