import csv
rec_fields = ['ID','Name','Age','Department','Email','Phone']
sms_database = 'students.csv'
def show_menu():
    print("---------------------------")
    print("Welcome to Student Management System")
    print("---------------------------")
    print("1. Add New Student")
    print("2. View Students Details")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")
def create_record():
    print("---------------------------")
    print("Add Student Information")
    print("---------------------------")
    global rec_fields
    global sms_database
    stud_data = []
    for field in rec_fields:
        value = input("Enter " + field + ": ")
        stud_data.append(value)

    with open(sms_database, "a",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([stud_data])
    print("Data saved successfully")
    input("Press any key to continue")
    return
def display_student():
    global rec_fields
    global sms_database
    print("----Student Records----")
    with open(sms_database,"r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for k in rec_fields:
            print(k,end='\t |')
        print("\n---------------------------------------")
        for row in reader:
            for item in row:
                print(item,end="\t |")
            print("\n")
    input("Press any key to continue")

def search_record():
    global rec_fields
    global  sms_database
    print("---Search Student---")
    id = input("Enter ID to search: ")
    with open(sms_database,"r",encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row)>0:
                if id == row[0]:
                    print("----- Student Found -----")
                    print("ID: ",row[0])
                    print("Name: ",row[1])
                    print("Age: ",row[2])
                    print("Department: ",row[3])
                    print("Email: ",row[4])

        else:
            print("ID not found in our database")
    input("Press any key to continue")

def update_record():
    global rec_fields
    global sms_database

    print("-----Update Student-----")
    roll = input("Enter ID to update: ")
    idx_student = None
    updated_rec = []
    with open(sms_database,"r",encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    idx_student = counter
                    print("Student Found: at index ",idx_student)
                    stud_data = []
                    for field in rec_fields:
                        value = input("Enter " + field+": ")
                        stud_data.append(value)
                    updated_rec.append(stud_data)
                else:
                    updated_rec.append(row)
                counter +=1
    if idx_student is not None:
        with open(sms_database,"w",encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_rec)
    else:
        print("Roll No. not found in our database")
    input("Press any key to continue")

def delete_record():
    global  rec_fields
    global sms_database

    print("----- Delete Student-----")
    roll = input("Enter ID to delete: ")
    stud_locate = False
    updated_rec = []
    with open(sms_database,"r",encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll !=row[0]:
                    updated_rec.append(row)
                    counter+=1
                else:
                    stud_locate = True
    if stud_locate is True:
        with open(sms_database,"w",encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_rec)
        print("ID:  ", id,"deleted successfully")
    else:
        print("ID not found in our database")
    input("Press any key to continue")
while True:
    show_menu()
    option  = input("Enter your option: ")
    if option == '1':
        create_record()
    elif option == '2':
        display_student()
    elif option == '3':
        search_record()
    elif option == '4':
        update_record()
    elif option == '5':
        delete_record()
    else:
        break
