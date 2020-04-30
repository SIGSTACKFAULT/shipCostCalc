import click
import requests
from requests.structures import CaseInsensitiveDict

oreList = [
            'Tritanium',
            'Pyerite',
            'Isogen',
            'Megacyte',
            'Mexallon',
            'Nocxium',
            'Zydrine'
           ]

marketList = [
                'jita',
                'hek',
                'amarr',
                'rens',
                'dodixie'
              ]

def welcome():
    print('Hello and Welcome to Jeklah\'s Ship Cost Calculator')
    print('Please choose which market you would like to use: ')
    for market in marketList:
        print('Ξ ' + marketList.index(market) + ' ' + market + '\n')

def choose_market():
    marketChoice = raw_input('Your choice by number: ')

    return(marketChoice)

def get_appraisal(ore, market):
    url = 'https://www.evepraisal.com/appraisal'
    payload = {
        'raw_textarea': ore + ' 1',
        'market': market
    }
    req = requests.post(url, params=payload)
    appraisal_id = req.headers['X-Appraisal-Id']
    appraisal_url = 'https://www.evepraisal.com/a/{}.json'.format(appraisal_id)
    result = requests.get(appraisal_url).json()


    ## Notes and code that will help
    #
    # convert = str(result).replace('\'', '"')
    # result['items'][0]['prices']
    # prices = result['items'][0]['prices']['buy']
    # quantity = result['items'][0]['quantity']

    oreName = result['items'][0]['name']
    currAvg = result['items'][0]['prices']['buy']['avg']
    minPrice = result['items'][0]['prices']['buy']['min']
    maxPrice = result['items'][0]['prices']['buy']['max']


    return(oreName, currAvg, minPrice, maxPrice)


def main():
    ret = get_appraisal()
    print(ret)

if __name__ == "__main__":
    main()


