import os

from pyrewe import rewe

cookie = '_rdfa=s:7770ebb4-5519-46d3-8250-307bb4686cdf.tLxovD1veTELoBfX8qdgMDig2cOGrdAwHgbWpqoO5yo; __cfruid=30a2ac9dad0d9bc183993cfbcfd2c6d2c600d3fa-1699393565; _cfuvid=y4mutghMy4gzwupK1dTe6MI_waUEUT9Y9NK3Py8t0OQ-1699393565437-0-604800000; intentionLayerIsForced=true; consentSettings={%22Usercentrics-Consent-Management-Platform%22:1%2C%22Adobe-Launch%22:1%2C%22Adobe-Experience-Cloud-Identity-Service%22:1%2C%22AWIN%22:1%2C%22reCAPTCHA%22:1%2C%22Cloudflare%22:1%2C%22Keycloak%22:1%2C%22gstatic-com%22:1%2C%22Google-Maps%22:1%2C%22JSDelivr%22:1%2C%22YouTube-Video%22:1%2C%22Google-AJAX%22:1%2C%22jQuery%22:1%2C%22Vimeo%22:1%2C%22Adobe-Analytics%22:1%2C%22Google-Ad-Manager-Basis%22:1%2C%22Funktionale-Cookies-und-Speicher%22:1%2C%22GfK-SENSIC%22:1%2C%22ChannelPilot%22:0%2C%22Adobe-Analytics-erweiterte-Web-Analyse%22:0%2C%22artegic-ELAINE-Software%22:0%2C%22Outbrain%22:0%2C%22RDFA-Technologie-Statistik-%22:0%2C%22Mouseflow%22:0%2C%22Facebook-Pixel%22:0%2C%22Microsoft-Advertising-Remarketing%22:0%2C%22Adform%22:0%2C%22Google-Ads-Conversion-Tracking%22:0%2C%22Google-Ads-Remarketing%22:0%2C%22Snapchat-Advertising%22:0%2C%22Pinterest-Tags%22:0%2C%22trbo%22:0%2C%22TikTok-Advertising%22:0%2C%22LinkedIn-Ads%22:0%2C%22Taboola%22:0%2C%22TradeDesk%22:0%2C%22DoubleClick-Floodlight%22:0%2C%22Cmmercl-ly%22:0%2C%22Google-Ad-Manager%22:0%2C%22RDFA-Technologie-Marketing-%22:0%2C%22tms%22:1%2C%22necessaryCookies%22:1%2C%22cmpPlatform%22:1%2C%22marketingBilling%22:1%2C%22fraudProtection%22:1%2C%22basicAnalytics%22:1%2C%22marketingOnsite%22:1%2C%22extendedAnalytics%22:0%2C%22serviceMonitoring%22:0%2C%22abTesting%22:0%2C%22conversionOptimization%22:0%2C%22feederAnalytics%22:0%2C%22personalAdsOnsite%22:0%2C%22remarketingOffsite%22:0%2C%22userProfiling%22:0%2C%22sessionMonitoring%22:0%2C%22targetGroup%22:0%2C%22advertisingOnsite%22:0}; AMCV_65BE20B35350E8DE0A490D45%40AdobeOrg=179643557%7CMCMID%7C92216584251834302489219331036141508634%7CMCAID%7CNONE%7CvVersion%7C5.5.0; marketsCookie=%7B%22online%22%3A%7B%22wwIdent%22%3A%22431036%22%2C%22marketZipCode%22%3A%2285435%22%2C%22serviceTypes%22%3A%5B%22PICKUP%22%5D%2C%22customerZipCode%22%3A%2285435%22%7D%2C%22stationary%22%3A%7B%7D%7D; icVarSave=tc108_t%2Ctc_56_control%2CTC%2062%20Control%2Ctc102_c; __cf_bm=HCko4YNgJZxkEp0syir4HIPcPYrb.3Mpoq9tyDgVTZ0-1699401250-0-AePoH4t0yVOho9rdCnTgkV42J9jXyDez2229NR+iSyn1twuZZyN9Z/s+QlEw+sn0w0I6TiiDISq1xBc5nZtb8TI=; cf_clearance=EVgR9oG7c5JPsBHj1ghf0so1gFD.I3KtvQlZTOR3.qw-1699401250-0-1-2adcef84.f1f154dd.c6dd90c5-0.2.1699401250; cso_jsid=NDVhNjBjYzAtMjg5Mi00NDA0LTk2MDEtMmYzZjA0NDZiYTFk; OAuth_Token_Request_State=1170ef5b-be49-459d-9ceb-00e6861c3671; c_lpv_a=1699401465321|ref_github.com_nn_nn_nn_nn_nn_nn_nn; MRefererUrl=direct; mtc=s%3AeyJoYXNoIjpbNjgsMTA5LDE2OSwzMiwxMDcsNDUsMTM0LDI0OSwxNzcsMTc5LDEwNSwxNzUsNTMsMTU4LDIxOSw0M10sInN0YWJsZSI6WyJwcm9kdWN0bGlzdC1uZXctaW5kZXgiLCJvZmZlci1kZXRhaWxzLXRyYWNraW5nIiwicmV3ZS1zc28iLCJwcm9kdWN0bGlzdC1yZWdpb25hbC1iYWRnZSIsInByb2R1Y3RsaXN0LW5hdmlnYXRpb24tdHJhY2tpbmciLCJzb3Mtc3dpdGNoLXJhbmtpbmdzIiwicGF5YmFjay1lY291cG9uLWFwaSIsImluaS0zODEyLWhpZGUtcmVndWxhci1wcmljZSIsImluaS00MTkwLWdhbSIsInByb2R1Y3RsaXN0LWdhbSIsInByb2R1Y3RsaXN0LW5ldy10b3BzZWxsZXIiLCJwcm9kdWN0bGlzdC1mbGFnc2hpcC1iYW5uZXIiLCJ3b29raWVlcy1zdGF0aW9uYXJ5LWZhcWNlbnRlciIsInBheWJhY2stdGFyZ2V0ZWQtYm9udXMtY291cG9uIiwicGF5YmFjay1jYXJkLWNoYW5nZSIsInN5LWNtcy1oZWFkbGluZXMiLCJwcm9kdWN0bGlzdC1jaXRydXNhZCIsImNtcDMiLCJ0YzEwOC1oaWRlLW9mZmVycyIsInByb2R1Y3RsaXN0LWdhbS1saW1pdGVkYWRzIiwiY2hlY2tvdXQtZGlzcGxheS1zaG93cm9vbS1hZCIsInByb2R1Y3RsaXN0LXRpZXJzLWhpZGUtaWNvbiIsInByb2R1Y3RsaXN0LXBhY2thZ2luZy1maWx0ZXIiLCJ3b29raWVlcy1waWNrdXAtcGFnZSIsIlBJRTcxLW5vT2ZmZXItaG9tZXBhZ2UiLCJuZXctbmF2aWdhdGlvbi10cmFja2luZyIsInBheWJhY2stZXZvdWNoZXIiLCJtZW5nZW5yYWJhdHRpZXJ1bmciLCJjaGVja291dC1tb2JpbGUtdXNlLW5ldy1wYXltZW50LWF1dGhvcml6YXRpb25zIiwicGF5YmFjay1yZXdlLW5ld3NsZXR0ZXIiLCJwcC1yZXdlLWVib24iLCJwYXliYWNrLXRhcmdldGVkLWJ1cm4iXSwicmR0Z2EiOltdLCJtdGNFeHBpcmVzIjo2MCwidGVzdGdyb3Vwc0hhc2giOiJmOTdlNGY0YmNkYjI0YmM2NmZhODNmNWJmNDljYTdlNGE3Zjg1Mzk4NDRiN2Q5ZWZjNmQ4ZjljMGIzYTY2NzlhIn0%3D.FGkqO7Piki0BxTkuo5L1y32uJctyMNO12lyyREEngwM; rstp=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhZXMxOTIiOiJjYzdlMDMzMzU3Y2VmMTg2Yjk1OWViODExYjliMjU0ODk4MzM0MjkwZDE5Mjk3MzExNDFjNDQwODVlYmE0MDc5NjA5ZTY3ZWM4ZjlmMGU1ZmU3NmZhMzA4MWQ3ZWIyZGM4OWM5ZWEwZjZmNjFhODE3ZWIxYjllMDlmNGZjZjViNGExMGQ1ODNmMDViNDE0ZmJkN2FhODM5MTRmMWRiZmJmMmE5OTA3NzVlNjM4NmE5YzkzZWIwZjBhZGEzOGRmNzA4MzkyODdiOTQ5NWQyMmE2MTFjMGMwM2MxNzhiM2VkOGYwODAyNjVjYjRkZGVkMzJjNTk4MWI5NjU4ZWY3ZmU2NjdiM2Q3YzI3MDMyZGM0ZWIyNTg4OGM5N2I0Mjk0N2FhZWFkYTRkNTdiMDMxYTQzMWY3NjU0YzgzN2FhNDhlYzg5MzlkYTBiOTU2NjBkNWFkMzdiNTMxZDdjOWUzOTFiZjY4Mjg5MDQxZDcxOWNmMGY5ZTJkZTBjYzkzMTIzNDljZGMzMDM1NGFiNGUwOTA5OTljZDlhMTY2MTZiNjMxMmQ4ZGU2ZWY4N2JhMGJhY2VjNDUwMDQ4ZDQ2ZjQxODEwMDc1ZjYxZDBiYjJkMGM1MWVmMTA0ZTBhOTc2YjdlODVhNmJiNmFlYmZmYjY5NTFmNGFjMTdmZDU0YTM3MjUxMDE2N2JlZmU1NGIzNWQyZTU0MjZkMjQ2OWVkMGViZDJhYzU3ZjUxMjAwMTA3MTczNzM3ODlkOWJmZWQ1YTJjMzFlNGZlOWUxYmY2N2ZkZDUxYmExYjY1YzI1YWQwYzdkOTliYzY5NDlhMTNmOTE3ZjkwMzg5Zjc3ZjE3NjA0YzhhMjI2ZWE0ZTNlNjQzZmM0MjA1N2Y3MDc5YzlmYWNhMGRhMDliNWY5MDZkMjc3Mjg1YWU0MDA4NGY2YTZjMTlkMTllNWYzMWEwYjI5OTZhMGYxNmNhYjAyNzNiYzFhNTlkMDJkYzk3MjMwMzAxNTZjM2RjMmZmMGIwMzk5NWI0YmUiLCJpYXQiOjE2OTk0MDE4NzgsImV4cCI6MTY5OTQwMjQ3OH0.iyh8uYBpURKcmbR_gVYPMN7j2q7e4tgQSv-vWlFFVozVsuX4NBNPGrUzXlYBGaytDbjl-nxJB6j8YEqVMRzW0A'
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
    if len(items['merchantBaskets']) != 0:
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
    else:
        print('No items in cart! Add some :)')


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
