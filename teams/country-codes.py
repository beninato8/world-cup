import pycountry

with open('countries.txt', 'r') as f:
    input_countries = [''.join(y for y in x if y != '\n') for x in f]
print([x.name.encode('utf8') for x in pycountry.countries if 'russia' in x.name.lower()])
countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_2

codes = [countries.get(country, 'Unknown code') for country in input_countries]

print(codes)  # prints [u'AS', u'CA', u'FR']