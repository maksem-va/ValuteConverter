from xml.etree import ElementTree

import requests


def cb_page_getter():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    inp = input('Input request. "-faq" for additional information. ').split()
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
        for cde in tree.findall('Valute'):
            code = cde.find('CharCode').text
            name = cde.find('Name').text
            codeDict[code] = name
        return print(codeDict)
    if inp[0] == '-faq':
        return print('Thank you for using my application. Hope, that you will never use this app again. Use command'
              ' -codes for list of available valutes. Input format: Incoming valute Value. Example: USD 10')
    string = xmlDict[inp[0].lower()].split()
    wage = string[0].replace(',', '.')
    print(inp[1] + " " + inp[0].upper() + " equals " + str(float(inp[1]) * float(wage)) + " RUB")


if __name__ == '__main__':
    cb_page_getter()
