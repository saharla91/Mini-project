import csv
from orders import order_menu 


    #MAIN MENU #main programme menu
while True: 
    print('''--------VIEW MAIN MENU--------

        [0] To exit the program

        [1]To view the Product menu

        [2]To view Courier menu

        [3]To view Order menu''')

    menu = int(input("select one of the options: "))
        
    
        #product menu selection options
    if menu == 1:
        while True:    
            print('''-----PRODUCT MENU-----

        [0]To exit product menu

        [1]To view the Products

        [2]To add to products

        [3]To remmove a product''')

    #PRODUCT MENU
        #input to get product list from csv file
            product_menu = int(input("Enter product menu option: "))
            if product_menu == 1:
                with open("data/products.csv", mode='r') as file:
                    product_list_index = []
                    product_list_index = file.readlines()
                    for index, product in enumerate(product_list_index):
                        print(index, product)
                            
        #input to add new product and price to current list
            elif product_menu == 2:
                with open("data/products.csv", mode='a', newline='') as file:
                    product_list = []   
                    field_name = ["product name", "product price"]
                    writer = csv.DictWriter(file,fieldnames=field_name, delimiter=',')
                    product_name = input("add product: ")
                    product_price = float(input("Enter price: "))
                    product_dictionary = {"product name":product_name, "product price":product_price}
                    writer.writerow(product_dictionary)
                    print("Product has been added")
        
        #input to remove from the product list using index
            elif product_menu == 3:
                with open("data/products.csv","r+", newline='') as file:
                    product_list = file.readlines()
                    for index, product in enumerate(product_list):
                        print(index, product)
                    index_to_remove_product = input("Remove product: ")
                    product_list.pop(int(index_to_remove_product))
                    file.writelines(product_list)
                    file.close()
                    print("Product has been removed")

            elif product_menu == 4:
                print("Product menu has been exited", menu)
            break

        #COURIER MENU
        #courier menu selection options
    if menu == 2:
        while True:
            print('''-----COURIER MENU----

            [0]Exit courier menu

            [1]To view couriers

            [2]Add to courier
        
            [3]To remove courier''')

        #enter input to get courier names from csv file
            courier_menu = int(input("Enter courier menu option: "))
            if courier_menu == 1:
                with open("data/couriers.csv", "r", newline='') as file:
                    courier_list_index = []
                    courier_list_index = file.readlines()
                    for index, courier in enumerate(courier_list_index):
                            print(index, courier)

        #input to add new courier name and phone number 
            elif courier_menu == 2:
                with open("data/couriers.csv", mode='a', newline='') as file:
                    courier_list = []
                    field_name = ["courier name", "courier phone"]
                    writer = csv.DictWriter(file,fieldnames=field_name, delimiter=',')
                    courier_name = input("add courier name: ")
                    courier_phone = float(input("enter courier phone: "))
                    courier_dictionary = {"courier name": courier_name, "courier phone":courier_phone}
                    writer.writerow(courier_dictionary)
                    print("courier name and phone has been added")

        #input to remove from current courier list using index
            elif courier_menu == 3:
                with open("data/couriers.csv", "r", newline='') as file:
                    reader = csv.DictReader(file)
                    courier_list = list(reader)
                    field_names = reader.fieldnames
                for index, courier in enumerate(courier_list):
                    print(index, courier)
                index_to_remove_courier = input("remove courier: ")
                courier_list.pop(int(index_to_remove_courier))
                with open("data/couriers.csv", 'w', newline='') as file:
                    writer = csv.DictWriter(file, field_names)
                    writer.writeheader()
                    writer.writerows(courier_list)
                print("courier has been removed")

            elif courier_menu == 4:
                print("courier menu has been exited", menu)
            break

        #ORDERS MENU
    if menu == 3:
        order_menu()

    if menu == 0:
        print("Programme is finished")
        
