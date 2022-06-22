
"""file = open("city.txt", "r", encoding="utf8")
# baslarina turkiye yazmak icin kod parcasi
file2 = open("city_with_countries.txt", "w")
for line in file.readlines():
    line = "Turkiye " + line
    file2.write(line)
file2.close()"""

countries_dictionary = {}
file = open('city_with_countries.txt', 'r', encoding='utf8')
for line in file.readlines():
    items = line.split()
    country = items[0]
    city = items[1]
    max_temp = items[2]
    min_temp = items[3]
    if country in countries_dictionary:
        countries_dictionary[country][city] = {'max': max_temp, 'min': min_temp}
    else:
        countries_dictionary[country] = {city: {'max': max_temp, 'min': min_temp}} 

countries = list(countries_dictionary.keys())
#print(countries)
#cities = countries_dictionary['Turkiye'] 
#print(cities)


print('##### COUNTRY/CITY SELECTION #####')
selected_country_idx = -1
selected_city_idx = -1

err = True
while(err):
    print('Select an index for country:')
    for i in range(len(countries)):
        print('\t{}-{}'.format(i+1, countries[i]))
    selected_country_idx = int(input())-1
    if selected_country_idx < len(countries):
        err = False

cities = list(countries_dictionary[countries[selected_country_idx]].keys())
err = True
while(err):
    print('Select an index for city:')
    idx = 1
    for city in cities:
        print('\t{}-{}'.format(idx, city))
        idx += 1
    selected_city_idx = int(input()) - 1
    if selected_city_idx < len(cities):
        err = False

selected_country = countries[selected_country_idx]
selected_city = cities[selected_city_idx]

max_temp = countries_dictionary[selected_country][selected_city]['max']
min_temp = countries_dictionary[selected_country][selected_city]['min']

print('*********************')
print('Selected Country: {}'.format(selected_country))
print('Selected City   : {}'.format(selected_city))
print('\tMax Temperature : {}'.format(max_temp))
print('\tMin Temperature : {}'.format(min_temp))
print('*********************')
print()
##############################################################
##############################################################
print('##### PANEL SELECTION #####')
panels_dictionary = {}
panels_file = open('panels.txt', 'r', encoding='utf8')
for line in panels_file.readlines():
    items = line.rstrip('\n').rstrip('\r\n').split(',')
    if len(items) != 5:
        print('There is wrong line format!')
        continue
    brand = items[0]
    model = items[1]
    power = float(items[2])
    voc = float(items[3])
    bvoc = float(items[4])
    if brand in panels_dictionary:
        panels_dictionary[brand][model] = {'power': power, 'voc': voc, 'bvoc': bvoc}
    else:
        panels_dictionary[brand] = {model: {'power': power, 'voc': voc, 'bvoc': bvoc}}


panels = list(panels_dictionary.keys())
selected_brand_idx = -1
err = True
while(err):
    print('Select an index for panel brand:')
    for i in range(len(panels)):
        print('\t{}-{}'.format(i+1, panels[i]))
    selected_brand_idx = int(input())-1
    if selected_brand_idx < len(panels):
        err = False

selected_model_idx = -1
models = list(panels_dictionary[panels[selected_brand_idx]].keys())
err = True
while(err):
    print('Select an index for panel model:')
    idx = 1
    for model in models:
        print('\t{}-{}'.format(idx, model))
        idx += 1
    selected_model_idx = int(input()) - 1
    if selected_model_idx < len(models):
        err = False

selected_panel = panels[selected_brand_idx]
selected_model = models[selected_model_idx]
voc = panels_dictionary[selected_panel][selected_model]['voc']
bvoc = panels_dictionary[selected_panel][selected_model]['bvoc']
power = panels_dictionary[selected_panel][selected_model]['power']

print('*********************')
print('Selected Panel Brand: {}'.format(selected_panel))
print('Selected Panel Model: {}'.format(selected_model))
print('\tPower : {}'.format(power))
print('\tVOC   : {}'.format(voc))
print('\tBVOC  : {}'.format(bvoc))
print('*********************')


EviriciMaxinput = float(input("Eviricinin maximumum gerilim değerini giriniz : "))

EviriciMininput = float(input("Eviricinin minumum gerilim değerini giriniz : "))

delta2 = int(max_temp) - 25
delta1 = int(min_temp) - 25

y = ((int(delta1) * float(bvoc) * (float(voc)/100)) + float(voc))

y1 = ((int(delta2) * float(bvoc) * (float(voc)/100)) + float(voc))

print("Maximum Y Değeri : ",float(y))

print("Minumum Y Değeri : ",float(y1))

Maxdizisayisi = (EviriciMaxinput / (float(y)))

Mindizisayisi = (EviriciMininput / (float(y1)))

print("Maximum dizisayisi : ",int(Maxdizisayisi))

print("Minumum dizisayisi : ",int(Mindizisayisi+1))
































