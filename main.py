def cb_page_getter():
    inp = input('Input request. ').split()
    print(inp[0] + " " + inp[1].upper() + " equals " + str(float(inp[0]) * 30) + " RUB")


# 30 рублей как в 2007

if __name__ == '__main__':
    cb_page_getter()