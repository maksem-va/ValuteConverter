from xml.etree import ElementTree

import requests


def cb_page_getter():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    inp = input('Input request. Format: Target Valute Number ').split()
    page = requests.get(url)
    tree = ElementTree.fromstring(page.content)
    xmlDict = {}
    codeDict = {}
    for dt in tree.findall('Valute'):
        code = dt.find('CharCode').text
        vle = dt.find('Value').text
        nom = dt.find('Nominal').text
        name = dt.find('Name').text
        xmlDict[code.lower()] = vle + " " + nom + " " + name
    if inp[0] == '-codes':
        for cd in tree.findall('Valute'):
            code = cd.find('CharCode').text
            name = cd.find('Name').text
            codeDict[code] = name
        return print(codeDict)
    string = xmlDict[inp[0].lower()].split()
    wage = string[0].replace(',', '.')
    print(inp[1] + " " + inp[0].upper() + " equals " + str(float(inp[1]) * float(wage)) + " RUB")


if __name__ == '__main__':
    cb_page_getter()
