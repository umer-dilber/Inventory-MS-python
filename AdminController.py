from ViewClasses import *
from DBConnection import ConnectionClass
class AdminController:
    def __init__(self):
        self.CntrollerObj = ConnectionClass("localhost", "root", "", "inventory")

    def __del__(self):
        if self.CntrollerObj.connection != None:
            self.CntrollerObj.connection.close()
    
    def signIn(self):
        print("Enter Sign in details! \n")
        try:
            name = input("Enter name: ")
            password = int(input("Enter password: "))
            if self.CntrollerObj.checkAdmin(name, password):
                return True
            return False
        except Exception as e:
            print("In Admin sign in got exception", str(e))

    def signUp(self):
        try:
            name = input("Enter name: ")
            id = int(input("Enter id: "))
            password = int(input("Enter password: "))
            while len(str(password)) != 4:
                print("Enter valid length! ")
                password = int(input("Enter password: "))
            a = Admin(name, id, password)
            if self.CntrollerObj.insertAdmin(a):
                return True
            return False
        except Exception as e:
            print("In Admin sign up got exception", str(e))

    def addItem(self):
        array = self.CntrollerObj.ShowCategories()
        for item in array:
            print(*item, sep='. ')
        try:
            select = int(input("\nSelect Category from listed above: "))
            while(select < 1 or select > 3):
                print("Selecet valid number")
                select = int(input("\nSelect Category from listed above: "))
            category = ""
            if select == 1:
                category = array[0][1]
            elif select==2:
                category = array[1][1]
            else:
                category = array[2][1]
            name = (input("Enter name: ")).capitalize()
            price = int(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            obj = Items(name, price, quantity, category.capitalize())
            self.CntrollerObj.insertItem(obj)
        except Exception as e:
            print("In Insert item got exception", str(e))

    def removeItem(self):
        self.CntrollerObj.removeItemAdmin()

    def ShowItems(self):
        self.CntrollerObj.ShowItemsAdmin()