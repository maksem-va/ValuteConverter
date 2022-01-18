from xml.etree import ElementTree

import requests


def cb_page_getter():
    inp = input('Input request. Format: Target Valute Number ').split()
    result = round(conv_money(inp[0], inp[1]), 3)
    print((inp[1] + " " + inp[0].upper() + " equals " + str(result) + " RUB"))


def conv_money(valute, value):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
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
    if valute == '-codes':
        for cd in tree.findall('Valute'):
            code = cd.find('CharCode').text
            name = cd.find('Name').text
            codeDict[code] = name
        return print(codeDict)
    string = xmlDict[valute.lower()].split()
    wage = string[0].replace(',', '.')
    return float(value) * float(wage)


if __name__ == '__main__':
    cb_page_getter()
