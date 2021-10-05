products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]


def key_func(s):
    return s[1]

def sort_price(list_of_tupels):
    return sorted(list_of_tupels, key=key_func, reverse=True)

print(sort_price(products))