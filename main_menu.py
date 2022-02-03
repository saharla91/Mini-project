
food= ["pizza", "jacket potatoe","fish fingers", "waffles"]

#------------------------------MAIN MENU-------------------------------------------   
while True:

    print("""------------Main menu------------

    Please choose one of the selections below:

    [0] To exit the program 

    [1]To view the product menu

    [2]To enter a new product 

    [3]Remove product
    
    [4] To view couriers  """)

    
    #user option:
    user_input = int(input("please enter option number:"))
    if user_input == 1:
        print(food)


    #new product
    elif user_input == 2:
        create_product = input("Enter new product:")
    
        food.append(create_product)
        print (''' new product has been added''')
        
    # remove from list
    elif user_input == 3:
        food.remove(input("Remove item: "))
        
        print("item has been removed", food)

    #exit
    elif user_input == 0:
        print('''exit''')
        break

    #couriers
    while user_input == 4:

        print (''' ------------View all couriers-------------

        [1]To view couriers

        [2]Add to courier

        [3]Delete courier
        
        [4]Exit courier menu''')

        #couriers list
        courier_input = int(input("please enter option number:"))
        if courier_input == 1:
                        file=open("couriers.txt", 'r')
                        contents=file.read()
                        print(contents)

        elif courier_input == 2:
            with open("couriers.txt", 'w') as file:
                content = input("Add courier name: ")
                file.write(content)
                file.close()
            print("courier name has been added")

            break




                

    
    
    




    



