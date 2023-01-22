import xmltodict

rows = []

with open('static/Cars.xml', 'r') as file:
    myfile = file.read()

mydict = xmltodict.parse(myfile)

# rows = list(mydict["row"])
data = mydict["root"]["row"]
rows = data[1:]


# import xml.etree.ElementTree as ET
# tree = ET.parse('static/Cars.xml')

# roots = tree.getroot()

# from xml.dom.minidom import parse
# import xml.dom.minidom

# DOMTree = xml.dom.minidom.parse('static/Cars.xml', 'r')
# collection = DOMTree.documentElement

# if collection.hasAttribute("shelf"):
#     print (collection.getAttribute('shelf'))

# datas = collection.getElementsByTagName("row")[1:]

# for data in datas:
#     print(".........Mobil.........")
#     idnya = data.getElementsByTagName("Id")[0]
#     print("Id : %s" % idnya.childNodes[0].data)
