import mysql.connector

def reg_user():
    print("----------registration---------")
    name = input("enter your  name: ")
    gender = input("Define your Gender: ")
    address = input('Enter your Address: ')
    contact_number = input('Enter your contect Number: ')
    car_compeny = input('Enter Car Company Name: ')
    car_model = input('Enter Car Model: ')
    manufacturing_year = input('Enter car manufacturing_year:  ')
    email_address = input('Enter your Email Adress: ')
    password = input("enter password: ")

    try:
        mydb=mysql.connector.connect(host='localhost',user='root',
                                    password='jay123',
                                    database='car_project2',
                                    auth_plugin= 'mysql_native_password')
        if mydb.is_connected():
            print("Successfully Connected with Database")
        cursor=mydb.cursor()
        # query1 = "create table users1(username varchar(20),pass varchar(20), name varchar(20),email varchar(20));" already created in mysql workbanch
        # cursor.execute(query1) 
        query2 = "insert into user_reg(name,gender,address,contact_number,car_compeny,car_model,manufacturing_year,email_address,password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
        data = (name, gender, address, contact_number, car_compeny, car_model, manufacturing_year, email_address, password)
        cursor.execute(query2, data)
        mydb.commit()
        print("----------------Your regitration succesfully Done----------------")

        user_id = cursor.lastrowid

        print("Here Are your regitration ID:")
        print(user_id)
        # print(f"Name: {name}")
        # print(f"Gender: {gender}")
        # print(f"Address: {address}")
        # print(f"Contact Number: {contact_number}")
        # print(f"Car Company: {car_compeny}")
        # print(f"Car Model: {car_model}")
        # print(f"Manufacturing Year: {manufacturing_year}")
        # print(f"Email Address: {email_address}")
        
        
    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
            print("Connection closed")

def login_ser():
    print("---------Login--------")
    email_address = input("enter email adress: ")
    password = input("enter password: ")
    try:
        mydb=mysql.connector.connect(host='localhost',user='root',
                                    password='jay123',
                                    database='car_project2',
                                    auth_plugin= 'mysql_native_password')
        
        cursor=mydb.cursor()
        query1 = "select * from user_reg where email_address = %s and password = %s"
        cursor.execute(query1,(email_address, password))
        user = cursor.fetchone()
        if user:
            print("Login Succesfully")
        else:
            print("Enter correct Username and password")

    except mysql.connector.Error as err:
        print(f"Error:{err}")
    finally:
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()
            print("Connection closed")


def get_car_info():
    print("\n")
    user_id = int(input("Enter user registration ID: "))
    mydb=mysql.connector.connect(host='localhost',user='root',
                                    password='jay123',
                                    database='car_project2',
                                    auth_plugin= 'mysql_native_password')
    cursor=mydb.cursor()
    
    # SQL query to retrieve car information
    query = """
    SELECT ur.car_compeny, ur.car_model, cm.part, cm.price
    FROM user_reg ur
    JOIN car_models cm ON ur.car_model = cm.model
    WHERE ur.user_id = %s
    """
    
    cursor.execute(query, (user_id,))
    
    # Fetch all rows
    results = cursor.fetchall()
    
    # Print car information
    if results:
        print("Car Information:")
        print(f"Car Brand: {results[0][0]}")
        print(f"Car Model: {results[0][1]}")
        print("Parts and Prices:")
        for row in results:
            print(f"Part: {row[2]}, Price: {row[3]}")
    else:
        print("No car information found for the provided user ID.")

while True:
    print("user auth systm")
    print("1. register user")
    print("2. login")
    print("3. see car info")
    print("4. exit")
    choice = int(input("enter your choice 1/2/3: "))


    if choice==1:
        reg_user()
    elif choice==2:
        login_ser()
    elif choice==3:
        get_car_info()
    elif choice==3:
        print("Exited program")
        break
    else:
        print("enter correct values")


# try:
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         passwd="jay123",
#         database="car_project2",
#         auth_plugin='mysql_native_password'
#     )
#     cursor=mydb.cursor()

#     cursor.execute("show databcases")
#     db=cursor.fetchall()
#     if db:
#         for i in db:
#             print(i)


#     if mydb.is_connected():
#         print("Database connection successful.......")

# finally:
#     if 'mydb' in locals() and mydb.is_connected():
#         mydb.close()
#         print("Connection closed")