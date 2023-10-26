d = {
    "name": "Albert",
    "surname": "Einstein",
    "occupation": {
        "role": "Professor",
        "workplace": "Uni of Berlin",
    },
    "languages": ["German", "Latin", "Italian", "English"],
}
print(d.items())

for k, v in d.items():
    if type(v) == list:
        for i in v:
            print(i)
    elif type(v) == dict:
        for k, v in v.items():
            print(k, v)