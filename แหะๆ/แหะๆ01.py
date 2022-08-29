value = input() # banana
s = []

for i in value: 
    x = []
    c = value.count(i)
    x.append(i)
    x.append(c)
    s.append(tuple(x))
print(s)
string_dubplicate = list(set(s))

max_str_db = {}
for i in string_dubplicate:
    max_str_db.update({i[1]:i[0]})
db = max(max_str_db.keys())
print(max_str_db.get(db))