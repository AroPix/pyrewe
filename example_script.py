import os

from pyrewe import rewe

cookie = '<no authentication implemented yet, so grab cookie from Chrome request>'
re = rewe(cookie)


def prompter():
    search = input("What product do you want to search for?\n-> ")
    products = re.get_products(str(search))['products']
    index = 0
    for item in products:
        index += 1
        string = f'[{index}] ' + item['name'] + ': ' + str(item['price'] / 100) + '€'
        if 'discount' in item:
            discount = item['discount']
            string += f' | DISCOUNT: -{str(discount).replace(".", ",")}%'
        print(string)
    selection = int(input('\nSelect the product you want to add to the basket\n-> '))
    s = int(selection - 1)
    prompt = input(
        f"\nDo you really want to add:\n{products[s]['name']} for {products[s]['price'] / 100} €? [y/n]\n-> ")
    match prompt:
        case "y":
            quantity = int(input("\nHow much do you want of that item?\n-> "))
            data, status_code = re.add_to_basket(products[s]['listingId'], quantity)
            match status_code:
                case 200:
                    print("Added to basket, starting from new...")
                case _:
                    print(f"Error: {status_code}\nData: {data}")
        case "n":
            print("Okay, starting from new...")
        case _:
            pass
    tui()


def list_basket():
    items = re.get_basket()[0]
    index = 0
    for item in items['merchantBaskets'][0]['lineItems']:
        index += 1
        name = item['listing']['_embedded']['product']['productName']
        price = str(item['totalPrice'] / 100).replace('.', ',')
        quantity = item['quantity']
        if 'basePrice' not in item['listing']['pricing']:
            price_per = f"{str(item['listing']['pricing']['currentPrice'] / 100).replace('.', ',')}€/{item['listing']['pricing']['grammage']}"
        else:
            price_per = f"{str(item['listing']['pricing']['basePrice']['value'] / 100).replace('.', ',')}€/{item['listing']['pricing']['basePrice']['measure']['uom']}"
        if 'discount' in item['listing']['pricing']:
            price_per += ' | DISCOUNT: -{}%'.format(str(item['listing']['pricing']['discount']['discountRate']).replace(".", ","))
        print(f'[{index}]: {name} | Price: {price} € | Quantity: {quantity} | PPM: {price_per}')
    print('Total price: ' + str(items['totalPrice']/100).replace('.', ',') + ' €')


def actions():
    prompt = input(
        '\n[1] Remove Item\n[2] Change Quantity of Item (If you want to add more of a specific item go for option 3)\n[3] Add items\n-> ')
    match prompt:
        case "1":
            selector = int(input('\nWhich item would you like to remove?\n-> '))
            re.remove_from_basket(re.basket['merchantBaskets'][0]['lineItems'][selector - 1]['listing']['id'])
        case "2":
            selector = int(input('\nWhich item would you like to change the quantity of?\n-> '))
            quantity = int(input('\nWhat quantity do you want to change it to?\n-> '))
            re.set_basket_quantity(re.basket['merchantBaskets'][0]['lineItems'][selector - 1]['listing']['id'],
                                   quantity)
        case "3":
            prompter()
        case _:
            tui()
    tui()


def tui():
    """Very very simple TUI (because TUI's are great)"""
    list_basket()
    actions()


tui()
