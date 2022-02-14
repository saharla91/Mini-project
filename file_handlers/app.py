import csv
products = ["fish finger", "waffles", "pizza"]
couriers = ["sarah", "hanna", "adam", "sam"] 
statuses = ["preparing", "out for delivery", "cancelled" , "delivered"]

    #MAIN MENU
while True: 
    print('''--------VIEW MAIN MENU--------

    [0] To exit the program

    [1]To view the Product menu

    [2]To view Courier menu

    [3]To view Order menu''')

    menu = int(input("select one of the options:"))
    
    if menu == 1:
        print('''-----PRODUCT MENU-----

    [0]To exit product menu

    [1]To view the Products

    [2]To add to products

    [3]To remmove a product''')

#PRODUCT MENU
    product_menu = int(input("Enter product menu option: "))
    if product_menu == 1:
        with open("data/products.csv", 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                    print(row)

    elif product_menu == 2:
        with open('data/products.csv', mode='a') as file:
            product_list = []   
            field_name = ["product name", "product price"]
            writer = csv.DictWriter(file,fieldnames=field_name, delimiter=',')
            product_name = input("add product: ")
            product_price = float(input("Enter price: "))
            product_dictionary = {"product name":product_name, "product price":product_price}
            writer.writeheader()
            writer.writerow(product_dictionary)
            print("Product has been added")

    elif product_menu == 3:
        with open("data/products.csv","r+") as file:
            product_list = file.readlines()
            for index, product in enumerate(product_list):
                print(index, product)
            index_to_remove_product = input("Remove product: ")
            product_list.pop(int(index_to_remove_product))
            file.writelines(product_list)
            file.close()
            print("Product has been removed")

    elif product_menu == 4:
        print("Product menu")
        break

#COURIER MENU
