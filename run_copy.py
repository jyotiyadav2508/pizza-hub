"""
Import gspread, to access and update data in our spreadsheet and
import credentials class from google-auth to set up the authenication
needed to access our Google Cloud Project.
"""
import os
from time import sleep
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
# from order import *

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
ORDER_LIST = SHEET.worksheet('order_list')
RECEIPT = SHEET.worksheet('receipt')
MAX_MENU_ITEM = 15





class UserOrder:
    """
    Class that creates user order instance
    """
    def __init__(self):
        # instance attribute
        self.user_name = None

        self.id = None
        self.order_type = None
        self.address = None

        self.items = list()
         
        # self.item_num = None
        # self.item_name = None
        # self.price = None

    @classmethod
    def new(cls, user_name):
        new_order = cls()
        new_order.user_name = user_name
        return new_order

    @classmethod
    def existing(cls, order_id):
        existing_order = cls()
        existing_order.id = order_id
        self._fetch_order()
        return existing_order

    def add_item(self, item_number)  :
        self.items.add(item_number)

    def complete(self)  :
        if self.id:
            return
        
        self.id = uuid()
        # Save info to worksheet
        rows = []
        for item in items:
            row.append([self.id, self.user_name, self.address, self.order_type, item])

    def _fetch_order(self):
        # Go to sheet


    def preview_order(self):
        """
        Function to preview user order
        """
        order_template = """
        Order ID: %s
        User Name: %s
        Order Type: %s
        Address: %s
        ----------------------------------------------
        Item Name   Item Price
        """
        item_teplate = """
        %s  %s
        """
        order_receipt = order_template % (self.id, self.user_name, self.order_type, self.address)
        
        total_price = 0
        for item in self.items:
            item_details = MENU.get(item)
            item_price = item_details[2]
            total_price += item_price
            order_receipt+=item_teplate % (item_details[1], item_details[2])
    
        order_receipt += "Total price: %s" total_price

        print(order_receipt)


    # def append_order_list(self):
    #     """
    #     Function to update user data in order worksheet
    #     """
    #     order_data = [self.user_name, self.item_num, self.item_name,
    #                 self.price, self.order_type, self.address]
    #     update_worksheet = SHEET.worksheet('order')
    #     update_worksheet.append_row(order_data)
    #     formatted_order_data = (tabulate(update_worksheet))
    #     print(formatted_order_data)


def welcome():
    """
    Function to display home page
    """
    print("Welcome to Pizza Hub!\n")
    while True:
        start_order = input("To order now, enter Y: ")
        print(start_order)
        if start_order.capitalize() == 'Y':
            clear_screen()
            get_user_details()
            break
        else:
            print("Invalid input. Enter Y to order.\n")

    # Workflow

    # 1. Welcome user
    # 2. Get User details
    # 3. User options - loop
    #   a. Place order
    #   b. Preview order
    #   c. exit

    user_name = input("Enger name")
    order = UserOrder.new(user_name)    

    # Place order Workflow
    # 1. Select delivery method
    # 2. Address
    # 3. While user wants to add more items:
    #   a. Show menu
    #   b. Select item
    #   c. Append item to current order
    # 4. Generate order id
    # 5. Update order in Google sheet
    # 6. Share order id/details to user

    order.order_type = "D"
    order.address = "<enterd address>"
    order.add_item(item_number)  
    order.complete()  
    order.preview_order()


    # Preview order Workflow
    # 1. Ask user for order id
    # 2. Get all rows from sheet against that order id
    # 3. Get all rows corresponding to unique items from menu
    # 4. Compute the final amount and show to user.

    order = UserOrder.existing(order_id)
    order.preview_order()
    

if __name__ == "__main__":
    welcome()   