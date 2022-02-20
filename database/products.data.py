from itertools import product
import pymysql
import os
import csv
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

connection = pymysql.connect(
    host = host,
    user = user,
    password = password,
    database = database,
)
cursor = connection.cursor()

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

        [3]To update product

        [4]To remmove a product''')

        #PRODUCT MENU
        #input to get product list
            product_menu = int(input("Enter product menu option: "))
            if product_menu == 1:
                cursor.execute("SELECT * FROM products")
                product_connect = cursor.fetchall()
                for x in product_connect:
                    print(x)

            if product_menu == 2:
                new_product = input("Enter product: ")
                new_price = input("Enter price: ")
                sql = "INSERT INTO products (name, price) VALUES (%s, %s)"
                val = (new_product, new_price)
                cursor.execute(sql, val)
                product_dictionary ={"name":new_product, "price":new_price}
                print("This is your new Product",product_dictionary)
                
            if product_menu == 3:
                sql = ("SELECT * id FROM products WHERE id = %s")
                cursor.execute(sql)
                myresult = cursor.fetchall()
                for x in myresult:
                    print(x)
                select_id = int(input("Enter id: "))
                val = (select_id)

                # sql_update_name = 'UPDATE products SET product_name = %s WHERE id = %s'
                # val_update_name = (new_product, select_id)
                # cursor.execute(sql_update_name,val_update_name)



                connection.commit()
            #cursor.close()
            #connection.close()