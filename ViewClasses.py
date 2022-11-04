class Admin:
    def __init__(self, a_name, a_id, a_password):
        self.name = a_name
        self.id = a_id
        self.password = a_password

class Items:
    def __init__(self, a_name, a_price, a_quantity, a_category):
        self.name = a_name
        self.price = a_price
        self.quantity = a_quantity  
        self.category = a_category

class CartItem:
    def __init__(self, a_name, a_price, a_qantity, a_amount):
        self.name = a_name
        self.price = a_price
        self.quantity = a_qantity
        self.amount = a_amount
