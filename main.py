import xml.etree.ElementTree as ET

""""
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

"""
xml_data = "/Users/mayahawkins/repos/Script_Splitter/DearMomc.xml"

# Parse the XML data
tree = ET.parse(xml_data)
root = tree.getroot()


# TITLE PAGE PRINTING
def print_title_page():
    for Paragraph in root.iter('TitlePage'):
        for Text in Paragraph.iter('Text'):
            print(Text.text)
    
"""
for i in root.iter('Paragraph'):
    for Text in i.iter('Text'):
        print(Text.text)
"""
        
# SCENE HEADING PRINTING
def print_scene_headings():
    print("ALL SCENE HEADINGS:")
    for i in root.iter('Paragraph'):
        # Check the "type" attribute
        item_type = i.get('Type')
        
        if item_type == 'Scene Heading':
            for Text in i.iter('Text'):
                print(Text.text)
        
# Int vs Ext PRINTING
def print_scene_info():
    print("SCENES INFORMATION:")
    int = 0
    ext = 0
    for i in root.iter('Paragraph'):
        # Check the "type" attribute
        item_type = i.get('Type')
        
        if item_type == 'Scene Heading':
            for Text in i.iter('Text'):
                if Text.text.startswith("INT."):
                    #print(f"Interior Scenes: {Text.text}")
                    int += 1
                elif Text.text.startswith("EXT."):
                    ext += 1
                    #print(f"Exterior Scene: {Text.text}")
    print(f"Total Scenes: {int + ext}")
    print(f"Total Interior Scenes: {int}")
    print(f"Total Exterior Scenes: {ext}")
    print("To print all scene headings, use --sceneHeadings function.")

# CHARACTER PRINTING
def print_characters():
    print("CHARACTER INFORMATION:")
    print(f"   # of characters: {len(root.findall('.//Member'))}")
    print(f"   (in order of appearance)")
    for i in range(0, len(root.findall(".//Member"))):
        character = root.findall(".//Member")[i].get("Character") 
        print("   ", end="")
        print(f"{i + 1}: {character}")  
        
def options():
    while True:
        print("OPTIONS:")
        print("   --titlePage: prints the title page")
        print("   --sceneHeadings: prints all scene headings")
        print("   --sceneInfo: prints the script scenes info")
        print("   --characters: prints all characters in order of appearance")
        print("   --exit: exits the program")
        choose = input("Choose an option: ")
        if "titlePage" in choose:
            print_title_page()
        elif "sceneHeadings" in choose:
            print_scene_headings()
        elif "sceneInfo" in choose:
            print_scene_info()  
        elif "characters" in choose:
            print_characters()
        elif "exit" in choose:
            print("Exiting program...")
            print("Thank you for using the script splitter!")
            break

options()



#print(f"Name: {name}, Price: {price}, Rate: {rate}, Description: {description}")
#print(f"Title: {titlePage}")
#print(f"Paragraph Type: {paragraph}, Text: {text}")