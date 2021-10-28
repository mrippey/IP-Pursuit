from ippursuit.tools.binaryedge import display_binedge_data
from ippursuit.tools.greynoise import get_greynoise_api
from ippursuit.tools.riskiq import fetch_riskiq_data

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
    print('[4]' + ' BinaryEdge')
    print('[5]' + ' RiskIQ')
    print('[6]' + ' DNSDB')
    print('[7]' + ' Shodan')
    print('[Quit]' + 'q or Q to quit\n')
   

def main():
    
    while True:
        show_menu()
        choice = input('Enter a number: ')

        if choice == '1':
	    pass
        elif choice == '2':
            get_greynoise_api()
        elif choice == '3':
	    pass
        elif choice == '4':
            display_binedge_data() 
	elif choice == '5':
 	    fetch_riskiq_data()
        elif choice == '6':
 	    pass
        elif choiec == '7':
  	    pass
        elif choice == 'q'.lower():
            raise SystemExit
        else:
            print(f'{choice} is not an option. Try again...\n')


if __name__ == '__main__':
    main()
