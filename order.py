
from time import sleep
import gspread
from tabulate import tabulate

class User_order:
    """
    Class that creates user order instance
    """
    def __init__(self, user_name, item_num, item_name, price, order_type, address):
        #instance attribute
        self.user_name = user_name
        self.item_num = item_num
        self.item_name = item_name
        self.price = price
        self.order_type = order_type
        self.address = address


    def append_order_data(self):
        """
        
        """
        order_data = [self.user_name, self.item_num, self.item_name, self.price, self.order_type, self.address]
        update_worksheet = SHEET.worksheet('order').append_row(order_data)