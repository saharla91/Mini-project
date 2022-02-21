import csv

def order_menu():

    while True:
        print('''-----ORDER MENU----

    [0]Exit order menu

    [1]To view  orders

    [2]To update order

    [3]To view status order
    
    [4]Order and staus update''')

        order_menu = int(input("enter order menu option: "))
        if order_menu == 1:
            with open("data/orders.csv", mode='r') as file:
                order_list = []
                order_list = file.readlines()
                for index, orders in enumerate(order_list):
                    print(index, orders)

        elif order_menu == 2:
            with open("data/orders.csv", mode='a', newline='') as file:
                order_list = []
                field_name = ["customer name", "customer address", "customer phone"]
                writer = csv.DictWriter(file,fieldnames=field_name, delimiter=',')
                customer_name = input("Enter customer name: ")
                customer_address = input("Enter customer address: ")
                customer_phone = float(input("Enter customer phone number: "))
                order_dictionary = {"customer name":customer_name, "customer address":customer_address, "customer phone":customer_phone}
                writer.writerow(order_dictionary)
                print("Details have been added")    
                
        elif order_menu == 3:
            status_list=["Preparing", "Out for delivery", "Cancelled", "Delivered"]
            print("These are your status options: ")
            for index, status in enumerate(status_list):
                print(index, status)
            status_input_order = input("Enter status: ") 
            print(status_input_order)            
        
        
        elif order_menu == 4:
            with open("data/orders.csv", mode='r') as file:
                order_list = []
                orders = file.readlines()
                for index, order in enumerate(orders):
                    print(index, order)
                chosen_order_index = int(input("pick an order: "))
                print(order)
                status_list = ["preparing", "out-for-delivery", "cancelled", "delivered"]
                for index, status in enumerate(status_list):
                    print(index, status)
                chosen_status_index = int(input("pick a status: "))
                orders[chosen_order_index] = status_list[chosen_status_index]
                print(order,status)
                #orders[chosen_order_index] = status_list[chosen_status_index]
                #return order, status

        elif order_menu == 0:
            print("Order menu exited")
        break
    