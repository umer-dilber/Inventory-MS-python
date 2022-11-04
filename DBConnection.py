import pymysql
from ViewClasses import Admin

class ConnectionClass:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        try:
            self.connection = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
        except Exception as e:
            print("There is error in connection", str(e))

    def insertAdmin(self, Admin):
        mydbCursor = None
        try:
            mydbCursor = self.connection.cursor()
            # Get cursor object
            query = "insert into admin(name ,emp_id, password) values(%s,%s,%s)"
            args = (Admin.name, Admin.id, Admin.password)
            mydbCursor.execute(query, args)
            self.connection.commit()
        except Exception as e:
            print("In Insert Admin got exception", str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()

    def checkAdmin(self, a_name, a_password):
        mydbCursor = None
        try:
            mydbCursor = self.connection.cursor()
            query = "select name, password from admin where name=%s and password=%s"
            args = (a_name, a_password)
            mydbCursor.execute(query, args)
            if len(mydbCursor.fetchall()) > 0:
                return True
            return False
        except Exception as e:
            print("Exception in check admin" + str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()

    def insertItem(self, Items):
        mydbCursor = None
        try:
            mydbCursor = self.connection.cursor()
            # Get cursor object
            query = "insert into items(name, price, quantity, category) values(%s,%s,%s,%s)"
            args = (Items.name, Items.price, Items.quantity, Items.category)
            mydbCursor.execute(query, args)
            self.connection.commit()

        except Exception as e:
            print("In Insert Admin got exception", str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()

    def ShowCategories(self):
        mydbCursor = None
        try:
            mydbCursor = self.connection.cursor()
            mydbCursor.execute("select * from category")
            return mydbCursor.fetchall()
        except Exception as e:
            print("In Show Catogries got exception", str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()


    def ShowItemsAdmin(self):
        mydbCursor = None
        try:
            mydbCursor = self.connection.cursor()
            mydbCursor.execute("select * from items")
            array = mydbCursor.fetchall()
            for item in array:
                print (*item, sep='\t')
        except Exception as e:
            print("In Insert Admin got exception", str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()

    def removeItemAdmin(self):
        mydbCursor = None
        try:
            mydbCursor = self.connection.cursor()
            mydbCursor.execute("Select name from items")
            array = mydbCursor.fetchall()
            for item in array:
                print(*item)
            select = input("\nEnter name of item for deletion from listed above: ")
            for it in array:
                if it[0].casefold() == select.casefold():
                    query = "delete from items where name=%s"
                    args = (select.casefold())
                    mydbCursor.execute(query, args)
                    self.connection.commit()
                    return 
            print("Item not exists")
        except Exception as e:
            print("Error in removing admin! ", str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()

    def showItemsCustomer(self, cat):
        mydbCursor = None
        try:
            mydbCursor = self.connection.cursor()
            query = ("select item_id, name, price, category from items where category=%s")
            args = (cat)
            mydbCursor.execute(query, args)
            return mydbCursor.fetchall()
        except Exception as e:
            print("In Show Items to customer got exception", str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()

    def verifyItem(self, na):
        mydbCursor = None
        try:
            mydbCursor = self.connection.cursor()
            query = ("select name from items where name=%s")
            args = (na)
            mydbCursor.execute(query, args)
            if len(mydbCursor.fetchall()) > 0:
                return True
            return False
        except Exception as e:
            print("In Show Items to customer got exception", str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()

    def verifyQuantity(self, na, q):
        mydbCursor = None
        try:
            mydbCursor = self.connection.cursor()
            query = ("select quantity from items where name=%s")
            args = (na)
            mydbCursor.execute(query, args)
            array = mydbCursor.fetchall()
            if q <= array[0][0]:
                return True
            return False
        except Exception as e:
            print("In Show Items to customer got exception", str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()

    def getPrice(self, na):
        mydbCursor = None
        try:
            mydbCursor = self.connection.cursor()
            query = ("select price from items where name=%s")
            args = (na)
            mydbCursor.execute(query, args)
            array = mydbCursor.fetchall()
            if array != None:
                return array[0][0]
            else:
                raise Exception
        except Exception as e:
            print("In Show Items to customer got exception", str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close() 

    def UpdateInventory(self, Cart):
        mydbCursor = None
        try:
            mydbCursor = self.connection.cursor()
            for i in Cart:
                query = ("Update items Set quantity = quantity - (%s) where name = (%s)")
                args = (i.quantity, i.name)
                mydbCursor.execute(query, args)
                self.connection.commit()
        except Exception as e:
            print("In update inventory got exception", str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close() 