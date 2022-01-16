samolot = {
    "name": "mig",
    "przebieg": 10000,
    "typ": "mysliwiec"
}

print(samolot["name"])
print(samolot["przebieg"])
print(samolot.get("xyz"))

if "abc" in samolot:
    print("mamy klucz abc")

for key in samolot:
    print('{0}:{1}'.format(key, samolot[key]))
