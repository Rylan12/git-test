#!/usr/bin/env python

# countries.csv source:
# https://datahub.io/JohnSnowLabs/country-and-continent-codes-list

import csv

country_lines = []

with open('countries.csv', 'r') as country_file:
    reader = csv.reader(country_file)
    for row in reader:
        country_lines.append(row)

continents = {
    'Africa': [],
    'Antarctica': [],
    'Asia': [],
    'Europe': [],
    'North America': [],
    'Oceania': [],
    'South America': []
}

for line in country_lines[1:]:
    continents[line[0]].append(line[2:4])

for continent in continents:
    with open('countries/' + continent + '.txt', 'w') as continent_file:
        for country in continents[continent]:
            continent_file.write(country[0] + ' (' + country[1] + ')\n')
