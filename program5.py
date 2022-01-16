mig = {
    "name": "mig",
    "przebieg": 10000,
    "typ": "mysliwiec"
}

boeing = {
    "name": "boeing",
    "przebieg": 40000,
    "typ": "pasazerski"
}

samoloty = [mig, boeing]

for s in samoloty:
    print(s["name"])
