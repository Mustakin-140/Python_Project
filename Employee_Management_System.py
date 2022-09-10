#Employee Management System using Python & MySQL
from os import system
import re
# importing mysql connector
import mysql.connector

#making connection
con = mysql.connector.connect(host="localhost",user="root",password="root",database="employee")

#make a regular expression for validation an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#for validating a phone number
Pattern = re.compile("(0|91)?[7-9][0-9]{9}")


#function to Add_Employee
def Add_Employ():
    print("{:>60}".format("-->> Add Employee Record <<--"))
    Id = input("Enter Employee ID: ")
    #checking if employee id exists or not
    if(check_employee(Id) == True):
        print("Employee ID Already Exits in Our Database\n Try Again...")
        press = input("Press Any Key to Continue...")
        Add_Employ()

    Name = input("Enter Employee Name: ")
    # checking if employee id exists or not
    if (check_employee(Name) == True):
        print("Employee Name Already Exits in Our Database\n Try Again...")
        press = input("Press Any Key to Continue...")
        Add_Employ()
    Email = input("Enter Employee Email: ")
    if(re.fullmatch(regex,Email)):
        print("Valid Email")
    else:
        print("Invalid Email")
        press = input("Press Any Key to Continue...")
        Add_Employ()
    Phone = input("Enter Employee Phone Number: ")
    if(Pattern.match(Phone)):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
        press = input("Press Any Key to Continue...")
        Add_Employ()

        Address = input("Enter Employee Address: ")
        Post = input("Enter Employee Post: ")
        Salary = input("Enter Employee Salary: ")

        data = (Id,Name,Email,Phone,Address,Post,Salary)

        #inserting Employee Datails in the Employee(empdata) Table
        sql = 'insert into empdata values(%s,%s,%s,%s,%s,%s,%s)'
        c = con.cursor()

        #executing SQL query
        c.execute(sql,data)

        #commit() method to make changes in the table
        con.commit()
        print("Successfully Added to the Employee Record...")
        press = input("Press Any Key to Continue...")
        menu()

#function to check if Employee with given name exist or not
def check_employee_name(employee_name):
    #query to select all rows from employee(empdata) table
    sql = 'select * from empdata where Name = %s'
    #making cursor buffered to make rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_name,)
    #Execute the sql query
    c.execute(sql,data)

    #rowcount method to find number of rows with given values
    r = c.rowcount
    if r == 1:
        return  True
    else:
        return False



# function to check if Employee with given name exist or not
def check_employee(employee_id):
    # query to select all rows from employee(empdata) table
    sql = 'select * from empdata where Id = %s'
    # making cursor buffered to make rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)
    # Execute the sql query
    c.execute(sql, data)

    # rowcount method to find number of rows with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


#function to Display_Employ
def Display_Employ():
    print("{:>60}".format("-->> display Employee Record <<--"))
    #query to select all rows from employee(empdata) table
    sql = 'select * from empdata'
    c = con.cursor()

    #execute the sql query
    c.execute(sql)

    #fetching all details of all the employees
    r = c.fetchall()
    for i in r:
        print("Employee Id: ",i[0])
        print("Employee Name: ",i[1])
        print("Employee Email Id: ",i[2])
        print("Employee Phone no: ",i[3])
        print("Employee Address: ",i[4])
        print("Employee Post: ",i[5])
        print("Employee Salary: ",i[6])
        print("\n")
    press = input("Press Any Key to Contimue...")
    menu()

#function to Update_Employ
def Update_Employ():
    print("{:>60}".format("-->> Update Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    #checking if employee Id exists or not
    if(check_employee(Id) == False):
        print("Employee Record does not exist here\n Try again")
        press = input("Press Any Key to Continue...")
        menu()
    else:
        Email = input("Enter Employee Email: ")
        if(re.fullmatch(regex,Email)):
            print("Valid Email")
        else:
            print("Invalid Email")
            press = input("Press any key to continue...")
            Update_Employ()
        Phone = input("Enter Employee Phone number: ")
        if(Pattern.match(Phone)):
            print("Valid Phone Number")
        else:
            print("Invalid Phone Number")
            press = input("Press Any Key to Continue...")
            Update_Employ()
        Address = input("Enter Employee Address: ")
        #Updating employee details in empdata table
        sql = 'UPDATE empdata set Email=%s, Phone=%s, Address=%s where Id =%s'
        data = (Email,Phone,Address,Id)
        c = con.cursor()

        #executing the sql query
        c.execute(sql,data)

        #commit() method to make change in the table
        con.commit()
        print("Updated Employee Record")
        press = input("Press Any Key to Continue...")
        menu()

#function to Promote_Employ
def Promote_Employ():
    print("{:>60}".format("-->> Promote Employee Record <<-- \n"))
    Id = input("Enter Employee Id: ")
    #checking if employee Id exists or not
    if(check_employee(id) == False):
        print("Employee Record does not exist\n Try again")
        press = input("Press Any Key to Continue...")
        menu()
    else:
        Amount = int(input("Enter Increase Salary: "))
        #query to fetch salary of Employee with given data
        sql = 'select Salary from empdata where id=%s'
        data = (Id,)
        c = con.cursor()

        #excuting the sql query
        c.execute(sql,data)
        #fetching salary of Employee with given id
        r = c.fetchone()
        t = r[0]+ Amount

        #query to update Salary of Employee with given id
        sql = 'update empdata set Salary = %s where Id = %s'
        d= (t,Id)

        #executing the sql query
        c.execute(sql,d)

        #commit() method to make changes in the table
        con.commit()
        print("Employee Promoted")
        press = input("Press Any Key to Continue...")
        menu()

#function to remove employee
def Remove_Employ():
    print("{:>60}".format("-->> Remove Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    #checking if employee id exists or not
    if(check_employee(Id) == False):
        print("Employee Record does not exist \n Try again")
        press = input("Press Any Key to Continue...")
        menu()
    else:
        #query to delete employee from empdata table
        sql = 'delete from empdata where Id =%s'
        data = (Id,)
        c = con.cursor()

        #executing sql query
        c.execute(sql,data)

        #commit() method to make changes in the table
        con.commit()
        print("Employee removed")
        press = input("Press Any Key to Continue...")
        menu()

#function to search employee
def Search_Employ():
    print("{:>60}".format("-->> Search Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking if employee id exists or not
    if (check_employee(Id) == False):
        print("Employee Record does not exist \n Try again")
        press = input("Press Any Key to Continue...")
        menu()
    else:
        # query to delete employee from empdata table
        sql = 'select * from empdata where Id =%s'
        data = (Id,)
        c = con.cursor()

        # executing sql query
        c.execute(sql, data)

        #fetching all details of all employee
        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Email Id: ", i[2])
            print("Employee Phone no: ", i[3])
            print("Employee Address: ", i[4])
            print("Employee Post: ", i[5])
            print("Employee Salary: ", i[6])
            print("\n")

        press = input("Press Any Key to Continue...")
        menu()


#menu function to display menu
def menu():
    system("cls")
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> Employee Management System <<--"))
    print("{:>60}".format("************************************"))

    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. Exit\n")
    print("{:>60}".format("-->> Choose Options: [1/2/3/4/5/6/7] <<--"))
    ch = int(input("Enter your choice: "))
    if ch == 1:
        system("cls")
        Add_Employ()

    elif ch == 2:
        system("cls")
        Display_Employ()
    elif ch == 3:
        system("cls")
        Update_Employ()
    elif ch == 4:
        system("cls")
        Promote_Employ()
    elif ch == 5:
        system("cls")
        Remove_Employ()
    elif ch == 6:
        system("cls")
        Search_Employ()
    elif ch == 7:
        system("cls")
        print("{:>60}".format("Have a nice day "))
        exit(0)

    else:
        print("Invalid choice!")
        press = input("Press any key to continue...")
        menu()

#calling menu function
menu()
