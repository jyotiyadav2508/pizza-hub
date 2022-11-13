"""
Import gspread, to access and update data in our spreadsheet and
import credentials class from google-auth to set up the authenication
needed to access our Google Cloud Project.
"""
import os
import gspread
from google.oauth2.service_account import Credentials
from time import sleep
from tabulate import tabulate


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pizza_hub')

MENU = SHEET.worksheet('menu')
ORDER = SHEET.worksheet('order')
RECEIPT = SHEET.worksheet('receipt')


def clear_screen():
    """
    Clear screen
    """
    if (os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')    


def main():
    """
    Home page
    """
    print("Welcome to Pizza Hub!\n")
    
    while True:
        start_order = input("To order now, enter Y: ")
        print(start_order)
        if start_order == 'y' or start_order == 'Y':
            clear_screen()
            get_user_details()
            break
        else:
            print("Invalid input. Enter Y to order.\n")
    

def get_user_details():
    """
    user details
    """
    input("Enter your name: ")
    while True:
        order_type = input("Order type:\n For Home delivery, enter D and For Pickup, enter P: ")
        if order_type == 'D' or order_type == 'd':
            print("Your selected delivery type is: Home delivery\n")
            address = input("Enter your Full Address: ")
            print(f"Your provided address: {address}")
            print("Loading menu...")
            sleep(5)
            clear_screen()
            display_menu_list()
            break
        elif order_type == 'P' or order_type == 'p':
            print("Your selected delivery type is: Pickup")
            print("Loading menu...")
            sleep(5)
            clear_screen()
            display_menu_list()
            break
        else:
            print("Invalid delivery type. Try again.")
    

def display_menu_list():
    """
    Get data from google spreadsheet
    """
    show_menu = MENU.get_all_values()
    formatted_menu = (tabulate(show_menu))
    print(formatted_menu)
    print("\nEnter Item number to add item to order list.")
    # print("Enter R to remove item from order list")
    print("Enter P to preview your order")
    print("Enter Q to quit\n")

    user_choice = input("Enter your choice: ")
    cell = MENU.find(user_choice)
    added_item = MENU.get('B' + str(cell.row))
    print(f"You added: {added_item[0][0]}")

# display_menu_list()
main()