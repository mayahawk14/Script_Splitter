import xml.etree.ElementTree as ET

xml_data = "/Users/mayahawkins/repos/Script_Splitter/rot.xml"

# Parse the XML data
root = ET.parse(xml_data).getroot()

# Iterate over elements
for parent in root:
    print(f"Parent tag: {parent.tag}")
    for child in parent:
        print(f"Child tag: {child.tag}")
        for grandchild in child:
            print(f"Grandchild tag: {grandchild.tag}, Attribute: {grandchild.attrib}")

# Access elements
product = root.find(".//product")
name = product.find(".//name").text
price = product.find(".//price").text
rate = product.find(".//rate").text 
description = product.find(".//description").text 

print(f"Name: {name}, Price: {price}, Rate: {rate}, Description: {description}")