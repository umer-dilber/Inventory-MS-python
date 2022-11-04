from DBConnection import ConnectionClass
from ViewClasses import *
class Customer:
    def __init__(self):
        self.CntrollerObj = ConnectionClass("localhost", "root", "", "inventory")
        self.listOfCart = []

    def __del__(self):
        if self.CntrollerObj.connection != None:
            self.CntrollerObj.connection.close()

    def Shopping(self):
        array = self.CntrollerObj.ShowCategories()
        for item in array:
            print(*item, sep='. ')
        try:
            select = int(input("\nSelect Category from listed above: "))
            while(select < 1 or select > 3):
                print("\nSelecet valid number")
                select = int(input("Select Category from listed above: "))
            category = ""
            if select == 1:
                category = array[0][1]
            elif select==2:
                category = array[1][1]
            else:
                category = array[2][1]

            array2 = self.CntrollerObj.showItemsCustomer(category)
            for it in array2:
                print(*it, sep='\t')
            sel = (input("\nEnter item name from listed above: "))
            sel = sel.capitalize()
            if self.CntrollerObj.verifyItem(sel):
                qua = int(input("Enter quantity: "))
                if self.CntrollerObj.verifyQuantity(sel ,qua):
                    price = self.CntrollerObj.getPrice(sel)
                    c = CartItem(sel, price, qua, price*qua)
                    self.listOfCart.append(c)
                    check = input("Checkout Y/N: \n")
                    if check == 'Y' or check=='y':
                        self.__generateReciept(self.listOfCart)
                        self.CntrollerObj.UpdateInventory(self.listOfCart)
                    elif check=='N' or check == 'n':
                        self.Shopping()
                    else:
                        raise Exception
                else:
                    print("Stock not available! ")
            else: 
                print("Item no found")
        except Exception as e:
            print("In Insert item got exception", str(e))
        
    def __generateReciept(self, cart):
        total = 0
        for i in cart:
            total += i.amount

        for i in cart:
            print(i.name + "\t" + str(i.price) + "\t" + str(i.quantity) + "\t" + str(i.amount))
        print("\t\t\t" + "Total\t" + str(total))