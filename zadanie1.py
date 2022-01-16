owoce = ["gruszka", "melon", "arbuz", "agrest", "jagody"]

print(owoce)
print(owoce[4])

print("=== petla for1 ===")
for owoc in owoce:
    print(owoc)

print("=== petla for2 ===")
for number in range(len(owoce)):
    o = owoce[number]
    print("number: {0} name: {1}".format(number, o))
