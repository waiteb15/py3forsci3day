#!/usr/bin/env python


import lxml.etree as ET

doc = ET.parse('DATA/presidents.xml')
print(doc)

pres_list = doc.getroot()

print(pres_list)

for pres in pres_list:
    name = pres.find('name')
    first_name = name.find('first').text
    last_name = name.find('last').text
    print(first_name, last_name)


#OOORRRR


for name in doc.findall('.//name'):
    first_name = name.findtext('first')
    print(f"{first_name}")