# converting list into dictionary


state = ["Maharashtra", "Gujarat", "Rajasthan", "Punjab"]
capital = ["Mumbai", "Gandhinagar", "Jaipur", "Chandigarh"]

z = zip(state,capital)
print(z)
sta_cap=dict(z)
print(sta_cap)