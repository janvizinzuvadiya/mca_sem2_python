# converting string into dictionary

s = "name:John,age:30,city:New York"
d = {}
for item in s.split(","):
    key, value = item.split(":")
    d[key] = value
print(d)


state = 'gujarat=gandhinagar,maharashtra=mumbai,rajasthan=jaipur,punjab=chandigarh'
print(state)

l =[]
for i in state.split(","):
    y =i.split("=")
    l.append(y)
print(l)
d = dict(l)
print(d)