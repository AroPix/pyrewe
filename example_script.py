import os

from pyrewe import rewe

cookie = "_rdfa=s:7770ebb4-5519-46d3-8250-307bb4686cdf.tLxovD1veTELoBfX8qdgMDig2cOGrdAwHgbWpqoO5yo; __cfruid=30a2ac9dad0d9bc183993cfbcfd2c6d2c600d3fa-1699393565; _cfuvid=y4mutghMy4gzwupK1dTe6MI_waUEUT9Y9NK3Py8t0OQ-1699393565437-0-604800000; intentionLayerIsForced=true; consentSettings={%22Usercentrics-Consent-Management-Platform%22:1%2C%22Adobe-Launch%22:1%2C%22Adobe-Experience-Cloud-Identity-Service%22:1%2C%22AWIN%22:1%2C%22reCAPTCHA%22:1%2C%22Cloudflare%22:1%2C%22Keycloak%22:1%2C%22gstatic-com%22:1%2C%22Google-Maps%22:1%2C%22JSDelivr%22:1%2C%22YouTube-Video%22:1%2C%22Google-AJAX%22:1%2C%22jQuery%22:1%2C%22Vimeo%22:1%2C%22Adobe-Analytics%22:1%2C%22Google-Ad-Manager-Basis%22:1%2C%22Funktionale-Cookies-und-Speicher%22:1%2C%22GfK-SENSIC%22:1%2C%22ChannelPilot%22:0%2C%22Adobe-Analytics-erweiterte-Web-Analyse%22:0%2C%22artegic-ELAINE-Software%22:0%2C%22Outbrain%22:0%2C%22RDFA-Technologie-Statistik-%22:0%2C%22Mouseflow%22:0%2C%22Facebook-Pixel%22:0%2C%22Microsoft-Advertising-Remarketing%22:0%2C%22Adform%22:0%2C%22Google-Ads-Conversion-Tracking%22:0%2C%22Google-Ads-Remarketing%22:0%2C%22Snapchat-Advertising%22:0%2C%22Pinterest-Tags%22:0%2C%22trbo%22:0%2C%22TikTok-Advertising%22:0%2C%22LinkedIn-Ads%22:0%2C%22Taboola%22:0%2C%22TradeDesk%22:0%2C%22DoubleClick-Floodlight%22:0%2C%22Cmmercl-ly%22:0%2C%22Google-Ad-Manager%22:0%2C%22RDFA-Technologie-Marketing-%22:0%2C%22tms%22:1%2C%22necessaryCookies%22:1%2C%22cmpPlatform%22:1%2C%22marketingBilling%22:1%2C%22fraudProtection%22:1%2C%22basicAnalytics%22:1%2C%22marketingOnsite%22:1%2C%22extendedAnalytics%22:0%2C%22serviceMonitoring%22:0%2C%22abTesting%22:0%2C%22conversionOptimization%22:0%2C%22feederAnalytics%22:0%2C%22personalAdsOnsite%22:0%2C%22remarketingOffsite%22:0%2C%22userProfiling%22:0%2C%22sessionMonitoring%22:0%2C%22targetGroup%22:0%2C%22advertisingOnsite%22:0}; AMCV_65BE20B35350E8DE0A490D45%40AdobeOrg=179643557%7CMCMID%7C92216584251834302489219331036141508634%7CMCAID%7CNONE%7CvVersion%7C5.5.0; marketsCookie=%7B%22online%22%3A%7B%22wwIdent%22%3A%22431036%22%2C%22marketZipCode%22%3A%2285435%22%2C%22serviceTypes%22%3A%5B%22PICKUP%22%5D%2C%22customerZipCode%22%3A%2285435%22%7D%2C%22stationary%22%3A%7B%7D%7D; MRefererUrl=direct; cso_jsid=OGM1ZGVkMmMtMzJjNi00OWVjLWJmZDgtZjQxZmI3ZWE0MGQ0; OAuth_Token_Request_State=df289d50-efac-4fde-9e0c-6204bb017f52; icVarSave=tc108_t%2Ctc_56_control%2CTC%2062%20Control%2Ctc102_c; mtc=s%3AeyJoYXNoIjpbNjgsMTA5LDE2OSwzMiwxMDcsNDUsMTM0LDI0OSwxNzcsMTc5LDEwNSwxNzUsNTMsMTU4LDIxOSw0M10sInN0YWJsZSI6WyJjaGVja291dC1kaXNwbGF5LXNob3dyb29tLWFkIiwiUElFNzEtbm9PZmZlci1ob21lcGFnZSIsInBheWJhY2stZXZvdWNoZXIiLCJpbmktNDE5MC1nYW0iLCJtZW5nZW5yYWJhdHRpZXJ1bmciLCJwYXliYWNrLXJld2UtbmV3c2xldHRlciIsIndvb2tpZWVzLXN0YXRpb25hcnktZmFxY2VudGVyIiwidGMxMDgtaGlkZS1vZmZlcnMiLCJwYXliYWNrLWVjb3Vwb24tYXBpIiwib2ZmZXItZGV0YWlscy10cmFja2luZyIsInNvcy1zd2l0Y2gtcmFua2luZ3MiLCJwcm9kdWN0bGlzdC1yZWdpb25hbC1iYWRnZSIsInByb2R1Y3RsaXN0LXBhY2thZ2luZy1maWx0ZXIiLCJwYXliYWNrLXRhcmdldGVkLWJvbnVzLWNvdXBvbiIsInBheWJhY2stY2FyZC1jaGFuZ2UiLCJjbXAzIiwicmV3ZS1zc28iLCJwcm9kdWN0bGlzdC1uZXctdG9wc2VsbGVyIiwicGF5YmFjay10YXJnZXRlZC1idXJuIiwic3ktY21zLWhlYWRsaW5lcyIsInByb2R1Y3RsaXN0LWNpdHJ1c2FkIiwicHJvZHVjdGxpc3QtbmF2aWdhdGlvbi10cmFja2luZyIsIm5ldy1uYXZpZ2F0aW9uLXRyYWNraW5nIiwicHJvZHVjdGxpc3QtZmxhZ3NoaXAtYmFubmVyIiwiY2hlY2tvdXQtbW9iaWxlLXVzZS1uZXctcGF5bWVudC1hdXRob3JpemF0aW9ucyIsImluaS0zODEyLWhpZGUtcmVndWxhci1wcmljZSIsInByb2R1Y3RsaXN0LWdhbS1saW1pdGVkYWRzIiwicHJvZHVjdGxpc3QtbmV3LWluZGV4IiwicHJvZHVjdGxpc3QtdGllcnMtaGlkZS1pY29uIiwicHJvZHVjdGxpc3QtZ2FtIiwid29va2llZXMtcGlja3VwLXBhZ2UiLCJwcC1yZXdlLWVib24iXSwicmR0Z2EiOltdLCJtdGNFeHBpcmVzIjo2MCwidGVzdGdyb3Vwc0hhc2giOiJmOTdlNGY0YmNkYjI0YmM2NmZhODNmNWJmNDljYTdlNGE3Zjg1Mzk4NDRiN2Q5ZWZjNmQ4ZjljMGIzYTY2NzlhIn0%3D.gs%2FpK6FRi7Iyw0ostdVGj6vH8mg0fPTV8VMyjjv2wWo; rstp=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhZXMxOTIiOiI0NTIyNDVkMDFjNmMxMjc1N2ExNjQxNDgwMzZmNDZhYzU1YWY1MGM2ZTg3ZTcwOGU3ZWU3MWViOTMwMjY5OGRkOTQ3NmYxNThkZGVhZjk0YjQ4N2Y3NzM3YmIxOGQ5MDkwNmRkNWFhOWZjODg1NjQ2ZGYwYTUwZWY5OGE5NDAyMDYyOTEwYTI1N2Y1YTBhYzU0NzAyZjRhNzY3OTc2ODAxYWUxYWMwMTUzZDA1ODZiYTVlOWNkNWRkN2E5MWNmNjUzNzc0NmRiNzE4YzIxYWNhOGM4OTZjYWRhNGE2NjQ4ZWM4NGIxNTdiYjA5NDc4MGE5ZWM5ODEzY2YyYWJjNDRiODZjZDg1N2I3M2FkMGFjMjFiN2ZkYzYwODA3ZDcxNTg1ZDlmMjM5NThlMzAxMTRlNjhhOTA2OWZmNWM0ZjE5MjVhOTJkOThmNDhlZDExMTA3YTBjY2M4YTQ1ZWE1NzQ5M2Q5OGM0ZmMxMWM5YmJmYjgyYzk3MGI0YzNjNGQ2NjVhZjJmMWZlNDU3YzM2NjE2ZjJkY2IyYTM4ODRkZjZjYWMxZTY1NzJkMTk0YmVjZmFlZDM2ZWUwNTczMTUxMDVkNTdhMjllM2I4Yzk0NzU4MDhhYzcwYjc2NjBiMmExNzkzMGM5OWRjZmVmYjg1YWYxZjRkMjk0NjNhMWQzZTRmMThkNTdmZjUzNmY1YmU0ZTc5ODhmNGYyMmNjM2UzMmI4MDliYzc0NjI4ODljOGNlZjgwNmIxMzQxOGI2ODM5OTRmYTEyNmFlZDQ0OGVjNDAxMjE2MzdlMTIxZWUzODY1Y2U0MTkzYjcyZTg4ZGU2YjU2Mjc3NDViY2MxNjFlNzllY2I1YjlhOTAyNDY5ZDJiNDkzMmZlYzIwNzNhYTBhMThhZTllYmM4OTJmMTNiYzY2NWQxOWI4ZGE1MjQzYWYxZGQ4ZjM5ZmRhZDhlNTA5MTQxMTliNmNmMjg0YzAwZjA3Nzk2MzFmOGQ3NDc4NjJhMDQ4MmJhYTUxN2MzMjVmNjY2NTY3YjQ0ZWMyYzE3NzAxODMzNzc5Y2ZjMDU4MjI1ZSIsImlhdCI6MTY5OTM5ODk5NCwiZXhwIjoxNjk5Mzk5NTk0fQ.ahzhV2t7ZWH65kYwTRck77Pr5e0RLESKxmF3g20DukbMaJxusqBgHaxDFo5V95zFXeaKqSSPR4Tk4K1sXbzsFQ; cf_clearance=um2vP01Q01HeRWMpRyyBMeupAEZQp9zpqKpkUQQRTrs-1699399001-0-1-2adcef84.f1f154dd.c6dd90c5-0.2.1699399001; __cf_bm=lMlrdBds0rj_HB20q.b8YIotBUG3qJDfJycf1CjKbUI-1699399145-0-AVIsRZSZnFNGharMAPFginmRqRx/cniIQv+VfwV1jzKCflChhpIMBVKuT53OMjvyRD1OZmrTk7/qnTCKBR2TMI0=; c_lpv_a=1699399145632|dir_direct_nn_nn_nn_nn_nn_nn_nn"
re = rewe(cookie)


def prompter():
    search = input("What product do you want to search for?\n-> ")
    products = re.get_products(str(search))['products']
    index = 0
    for item in products:
        index += 1
        print(f'[{index}] ' + item['name'] + ': ' + str(item['price'] / 100) + '€')
    selection = int(input('\nSelect the product you want to add to the cart\n-> '))
    s = int(selection - 1)
    prompt = input(
        f"\nDo you really want to add:\n{products[s]['name']} for {products[s]['price'] / 100} €? [y/n]\n-> ")
    match prompt:
        case "y":
            quantity = int(input("\nHow much do you want of that item?\n-> "))
            data, status_code = re.add_to_basket(products[s]['listingId'], quantity)
            match status_code:
                case 200:
                    print("Added to card, starting from new...")
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
        price_per = f"{str(item['listing']['pricing']['basePrice']['value'] / 100).replace('.', ',')}€/{item['listing']['pricing']['basePrice']['measure']['uom']}"
        print(f'[{index}]: {name} | Price: {price} € | Quantity: {quantity} | PPM: {price_per}')


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
    os.system('cls' if os.name == 'nt' else 'clear')
    list_basket()
    actions()


tui()
