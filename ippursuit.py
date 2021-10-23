from ippursuit import *
from ippursuit.tools.greynoise import get_greynoise_api

__author__ = 'Michael Rippey'


def show_menu():
    version = 0.1
    print(f"""
    ________   ____                        _ __ 
   /  _/ __ \ / __ \__  ______________  __(_) /_
   / // /_/ // /_/ / / / / ___/ ___/ / / / / __/
 _/ // ____// ____/ /_/ / /  (__  ) /_/ / / /_  
/___/_/____/_/    \__,_/_/  /____/\__,_/_/\__/  
     /_____/                                    
                                                                                                                                                                          
    Version: {version} 
    Author: {__author__}
        """)

    print('[MENU]' + ' Select an option below to continue\n')
    print('[1]' + ' Query all the below API services simultaneously')
    print('[2]' + ' GreyNoise')
    print('[3]' + ' SecurityTrails')
    print('[4]' + ' PulseDive')
    print('[5]' + ' RiskIQ')
    print('[6]' + ' DNSDB')
    print('[7]' + ' Shodan')
    print()


def main():

    #gn = GreyNoiseFinder()
    
    while True:
        show_menu()
        choice = input('Enter a number: ')

        if choice == '2':
            print(f'[*] Option {choice} selected')
            get_greynoise_api()

        elif choice == 'q':
            raise SystemExit
        else:
            print('Didnt understand')


if __name__ == '__main__':
    main()
