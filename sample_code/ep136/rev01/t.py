cities_by_country = {
    'San Mateo': 'US',
    'Toronto': 'CA',
    'Detroit': 'US',
    'London': 'UK',
    'Paris': 'FR',
    'Seattle': 'US',
    'Vancouver': 'CA',
}

# Problem:
# produce a mapping from {country: [sorted list of cities]}

dct = {}
for city, country in cities_by_country.items():
    if country in dct:
        dct[country].append(city)
    else:
        dct[country] = [city]

for cities_list in dct.values():
    cities_list.sort()


import pprint
pprint.pprint(dct)
