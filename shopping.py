cart = {
    'T-Shirt': 0,
    'Long Sleeve Tee': 0,
    'Crewneck': 0,
    'Hoodie': 0,
    }
    
while True:
    print('\n-- Welcome to Panacea Textile Co --')
    prompt = input('\nWhat would you like to do today?\nShop("s") - View Cart("v") - Add/Remove Item("i") - Finish Shopping("f")\n:')

    if prompt.lower() == 's':
        print('What would you like to purchase today?')
        print('\nT-Shirt("t") | Long Sleeve Tee("l") | Crewneck("c") | Hoodie("h")')
        item = input('\nItem: ')
        if item.lower() == 't':
            print('\nNice, how many T-Shirts would you like?')
            quantity = int(input('Quantity: '))
            cart['T-Shirt'] = quantity
            print('Great, your cart has been updated!')
        if item.lower() == 'l':
            print('\nNice, how many Long Sleeve Tees would you like?')
            quantity = int(input('Quantity: '))
            cart['Long Sleeve Tee'] = quantity
            print('Great, your cart has been updated!')
        if item.lower() == 'c':
            print('\nNice, how many Crewnecks would you like?')
            quantity = int(input('Quantity: '))
            cart['Crewneck'] = quantity
            print('Great, your cart has been updated!')
        if item.lower() == 'h':
            print('\nNice, how many Hoodies would you like?')
            quantity = int(input('Quantity: '))
            cart['Hoodie'] = quantity
            print('Great, your cart has been updated!')
    if prompt.lower() == 'v':
        print('\nOkay, let\'s take a look!')
        print('Your Cart:')
        print(cart)
    if prompt.lower() == 'i':
        print('\nWould you like to add("a") or remove("r") items from your cart?')
        aor = input('Enter here: ')
        if aor.lower() == 'a':
            print('\nHere is your current cart: ')
            print(cart)
            print('\nWhat item would you like to add more of?')
            print('T-Shirt("t") | Long Sleeve Tee("l") | Crewneck("c") | Hoodie("h")')
            item = input('\nItem: ')
            if item.lower() == 't':
                print('\nNice, how many T-Shirts would you like to add?')
                add = int(input('Quantity: '))
                cart['T-Shirt'] = cart['T-Shirt'] + add
                print('Great, we got those added and your cart has been updated!')
            if item.lower() == 'l':
                print('\nNice, how many Long Sleeve Tees would you like to add?')
                add = int(input('Quantity: '))
                cart['Long Sleeve Tee'] = cart['Long Sleeve Tee'] + add
                print('Great, we got those added and your cart has been updated!')
            if item.lower() == 'c':
                print('\nNice, how many Crewnecks would you like to add?')
                add = int(input('Quantity: '))
                cart['Crewneck'] = cart['Crewneck'] + add
                print('Great, we got those added and your cart has been updated!')
            if item.lower() == 'h':
                print('\nNice, how many Hoodies would you like to add?')
                add = int(input('Quantity: '))
                cart['Hoodie'] = cart['Hoodie'] + add
                print('Great, we got those added and your cart has been updated!')
        if aor.lower() == 'r':
            print('\nHere is your current cart: ')
            print(cart)
            print('\nWhat item would you like to remove?')
            print('T-Shirt("t") | Long Sleeve Tee("l") | Crewneck("c") | Hoodie("h")')
            item = input('\nItem: ')
            if item.lower() == 't':
                if cart['T-Shirt'] == 0:
                    print('Sorry, you don\'t have any in your cart.')
                    continue
                print('\nOkay, how many T-Shirts would you like to remove?')
                sub = int(input('Quantity: '))
                cart['T-Shirt'] = cart['T-Shirt'] - sub
                if cart['T-Shirt'] < 0:
                    cart['T-Shirt'] = 0
                print('Those items have been removed and your cart has been updated!')
            if item.lower() == 'l':
                if cart['Long Sleeve Tee'] == 0:
                    print('Sorry, you don\'t have any in your cart.')
                    continue
                print('\nOkay, how many Long Sleeve Tees would you like to remove?')
                sub = int(input('Quantity: '))
                cart['Long Sleeve Tee'] = cart['Long Sleeve Tee'] - sub
                if cart['Long Sleeve Tee'] < 0:
                    cart['Long Sleeve Tee'] = 0
                print('Those items have been removed and your cart has been updated!')
            if item.lower() == 'c':
                if cart['Crewneck'] == 0:
                    print('Sorry, you don\'t have any in your cart.')
                    continue
                print('\nOkay, how many Crewnecks would you like to remove?')
                sub = int(input('Quantity: '))
                cart['Crewneck'] = cart['Crewneck'] - sub
                if cart['Crewneck'] < 0:
                    cart['Crewneck'] = 0
                print('Those items have been removed and your cart has been updated!')
            if item.lower() == 'h':
                if cart['Hoodie'] == 0:
                    print('Sorry, you don\'t have any in your cart.')
                    continue
                print('\nOkay, how many Hoodies would you like to remove?')
                sub = int(input('Quantity: '))
                cart['Hoodie'] = cart['Hoodie'] - sub
                if cart['Hoodie'] < 0:
                    cart['Hoodie'] = 0
                print('Those items have been removed and your cart has been updated!')
    if prompt.lower() == 'f':
        print('\nHere\'s your receipt!')
        print(cart)
        print('\nThank you for shopping with Panacea Textile, we hope to see you again soon!')

        break
