name = ["bob", "john", "steve"]
roll_no = [1, 2, 3]
new_list = [(x, y) for x, y in zip(name, roll_no)]
print(new_list)
