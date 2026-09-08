phonebook = {'Anirach': '777-1111', 'Mivkey': '777-2222', 'Donald': '777-3333', 'Pluto': '777-4444'}

herosdict = {}
herosdict['Hulk'] = '888-1111'
herosdict['Iron Man'] = '888-2222'
print(herosdict.get('Halk', 'Key not Found'))
print(herosdict.get('Hulk', 'Key not Found'))

for key, value in phonebook.items():
    print(key, value)

print(phonebook.keys())
print(phonebook.values())

print(phonebook.pop('Mick','Element not Found'))
print(phonebook.pop('Mickey','Element not Found'))
print(phonebook)
print(phonebook.popitem())
print(phonebook)
phonebook.clear()
print('After clear')
print(phonebook)