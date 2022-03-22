import xml.etree.ElementTree as ET
import requests

# y = input("informe o ano da qualificação: ")
# r = input("informe o round da qualificação: ")

url = f"http://ergast.com/api/f1/2022/1/qualifying"


payload={}
headers = {}


resp = requests.request("GET", url, headers=headers, data=payload)
tree =  ET.ElementTree(ET.fromstring(resp.content))

root = tree.getroot()

# filtro = "*"
# for child in root.iter(filtro):
#     print(child.tag, child.text)

for child in root.findall("{http://ergast.com/mrd/1.5}RaceTable"):
    # for title in child.findall("TITLE"):
    print(child)


# print(root)