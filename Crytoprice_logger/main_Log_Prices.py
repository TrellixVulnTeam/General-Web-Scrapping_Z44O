# log BTC-USD, ETH-BTC, ETH-USD 
# USD this the master
# based on this https://www.scrapingbee.com/blog/selenium-python/
# interpreter Anaconda 3.8.5 with clearterminal
# XPATH == path for fetched html
# https://tcoil.info/how-to-get-price-data-for-bitcoin-and-cryptocurrencies-with-python-json-restful-api/
#%%
import time
import requests
from datetime import datetime
import platform

####SETUP####

#############


def get_current_data(from_sym, to_sym):
    url = 'https://min-api.cryptocompare.com/data/price'    
    
    parameters = {'fsym': from_sym, 'tsyms': to_sym }
    # response comes as json
    response = requests.get(url, params=parameters)   
    #https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD Example of what the link looks like with the parameterss
    data = response.json()
    
    return data[str(list(data)[0])]

def get_time():
    return time.time()

def log_csv():
    with open("Crytoprice_logger/BitCoinPriceLogging.csv", "a") as file:
        enitites = [get_time(), btc_usd, eth_usd, eth_btc, btc_thb, eth_thb]
        for enity in enitites:
            file.write('"' + str(enity) + '",')
        file.write("\n")
    print("""Cryto price logged: {}

DONE
DONE""".format(enitites))
    time.sleep(3) 

def error_notification(message):
    if platform.system() == 'Windows':
        from win10toast import ToastNotifier
        # create an object to ToastNotifier class
        n = ToastNotifier()
        
        n.show_toast("Crypto Logger", message, duration = 15, icon_path = "dependances\python logo.png")



if __name__ == '__main__' :
    """ import timeit
    print('1. :\t' , timeit.timeit(get_btc,number =1), 'milliseconds')
    print('2. :\t' , timeit.timeit(get_eth,number =1), 'milliseconds') """
    btc_usd = get_current_data('BTC','USD')
    eth_usd = get_current_data('ETH','USD')
    eth_btc = get_current_data('ETH','BTC')
    btc_thb = get_current_data('BTC','THB')
    eth_thb = get_current_data('ETH','THB')
    
    try:
        log_csv()
    except PermissionError:
        error_notification("PermissionError: CSV is being opened by another program")
    except Exception as e:
        error_notification("Error: {}".format(e))

    
    


