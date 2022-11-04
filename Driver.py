from AdminController import AdminController
from CustomeController import Customer

admin = AdminController()
customer = Customer()
while True:
    try:
        print("Welcome to Inventor Management System!")
        i = int(input("Enter 1 for Admin Control: \n"
                        "Enter 2 for Customer Use: \n"
                        "Enter 3 for exit: "))
        
        while i<0 and i>3:
            print("Enter valid number")
            i = int(input("Enter 1 for Admin Control: \n"
                        "Enter 2 for Customer Use: "))

        if i == 1:
            j = int(input("Enter 1 for Sign in: \n"
                        "Enter 2 for Sign up: "))
        
            while j<0 and j>2:
                print("Enter valid number")
                j = int(input("Enter 1 for Sign in: \n"
                        "Enter 2 for Sign up: "))
            flag = False
            if j==1:
                if admin.signIn():
                    flag = True
            else:
                admin.signUp()
                admin.signIn()
                flag = True
            if flag:
                while True:
                    k = int(input("Enter 1 for add item: \n"
                            "Enter 2 for remove item: \n"
                            "Enter 3 for show items: \n"
                            "Enter 4 for break: "))
                    while k<0 or k>4:
                        print("Invalid input")
                        k = int(input("Enter 1 for add item: \n"
                            "Enter 2 for remove item: \n"
                            "Enter 3 for show items: "))
                    if k==1:
                        admin.addItem()
                    elif k==2:
                        admin.removeItem()
                    elif k==3:
                        admin.ShowItems()
                    else:
                        break
        elif i==2:
            print("Welcome to customer screen! ")
            a = int(input("Enter 1 for shopping! "))
            if a == 1:
                customer.Shopping()
        else:
            exit(0)
    except Exception as e:
        print ("Exeception in input" + str(e))