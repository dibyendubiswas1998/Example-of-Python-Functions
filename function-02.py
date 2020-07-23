# Customer Account Banking Systems:


def default():
    print()
    sta = "STATE BANK OF INDIA"
    print(sta.center(50, '-'))
    print()
    print(f"Savings Bank Account")
    print(f"Branch: Hakimpara (Siliguri)            Branch Code: 254012")
    print(f"CIF No: 45954879658")
    print(f"IFSC Code: SBIN0007123")


def customer_list():
    default()
    print()
    print(f"Account Holder Name             Account No")
    print()
    print(f"Aloke Kumar Sengupta            12345678962")
    print(f"Dibyendu Biswas                 33882869164")
    print(f"Aksah Kumar Paul                98564567896")
    print(f"Shipra Biswas                   35847567896")
    print(f"Jyotermoy Roy                   88896567896")
    print(f"Ram Kumar Das                   55684567896")
    print(f"Ratan Paul Kumar                01288567896")
    print(f"Debashis Kumar Sengupta         67894567896")
    print(f"Susmita  Sengupta               32548567896")


def transaction():
    print()
    ac = int(input("Enter Account Number: "))
    if ac == 123456:
        default()
        print(f"A/c No: 1234567896")
        print(f"Account Holder Name: Aloke Kumar Sengupta")
        print()
        ta = input("Transaction Duration(yearly/half yr/queterly): ")
        if ta in ('yearly', 'Yearly', 'YEARLY'):
            print()
            print("Your Yearly Transaction(s) is/are: ")
            print()
            print(f"Your Openning Balance is: 65000.00")
            print(f"05/01/2020:     1200(wd)    ----(dp)    65000(b)")
            print(f"10/01/2020:     ----(wd)     500(dp)    70000(b)")
            print(f"30/01/2020:     ----(wd)    2000(db)    72000(b)")
            print(f"08/02/2020:     6500(wd)    ----(db)    65500(b)")
            print(f"21/02/2020:     1200(wd)    ----(db)    64300(b)")
            print(f"05/03/2020:     ----(wd)    1000(db)    65300(b)")
            print(f"27/03/2020:     2000(wd)    ----(db)    63300(b)")
            print(f"06/04/2020:     3300(wd)    ----(db)    60000(b)")
            print(f"08/04/2020:     5000(wd)    ----(db)    55000(b)")
            print(f"12/04/2020:     ----(wd)    1000(db)    56000(b)")
            print(f"20/04/2020:     1200(wd)    ----(db)    64800(b)")
            print(f"Your Closing Balance is: 64800.00")
        elif ta in ('half yr', 'Half yearly', 'half yearly', 'hy', 'hyr'):
            print("Your Half Yearly Transaction(s) is/are: ")
            print()
            print(f"Your Openning Balance is: 65000.00")
            print(f"05/01/2020:     1200(wd)    ----(dp)    65000(b)")
            print(f"10/01/2020:     ----(wd)     500(dp)    70000(b)")
            print(f"30/01/2020:     ----(wd)    2000(db)    72000(b)")
            print(f"08/02/2020:     6500(wd)    ----(db)    65500(b)")
            print(f"21/02/2020:     1200(wd)    ----(db)    64300(b)")
            print(f"05/03/2020:     ----(wd)    1000(db)    65300(b)")
            print(f"27/03/2020:     2000(wd)    ----(db)    63300(b)")
            print(f"06/04/2020:     3300(wd)    ----(db)    60000(b)")
            print(f"08/04/2020:     5000(wd)    ----(db)    55000(b)")
            print(f"Your Closing Balance is: 55000.00")
        elif ta in ('queterly', 'qurly', 'qrl', 'qtly'):
            print("Your Queterly Transaction(s) is/are: ")
            print()
            print(f"Your Openning Balance is: 65000.00")
            print(f"05/01/2020:     1200(wd)    ----(dp)    65000(b)")
            print(f"10/01/2020:     ----(wd)     500(dp)    70000(b)")
            print(f"30/01/2020:     ----(wd)    2000(db)    72000(b)")
            print(f"08/02/2020:     6500(wd)    ----(db)    65500(b)")
            print(f"21/02/2020:     1200(wd)    ----(db)    64300(b)")
            print(f"05/03/2020:     ----(wd)    1000(db)    65300(b)")
            print(f"27/03/2020:     2000(wd)    ----(db)    63300(b)")
            print(f"Your Closing Balance is: 63300.00")
        else:
            "break"
    elif ac == 33882869164:
        default()
        print(f"A/c No: 33882869164")
        print(f"Account Holder Name: Dibyendu Biswas")
        print()
        ta = input("Transaction Duration(yearly/half yr/queterly): ")
        if ta in ('yearly', 'Yearly', 'YEARLY'):
            print("Your Yearly Transaction(s) is/are: ")
            print()
            print(f"Your Openning Balance is: 65000.00")
            print(f"05/01/2020:     1200(wd)    ----(dp)    65000(b)")
            print(f"10/01/2020:     ----(wd)     500(dp)    70000(b)")
            print(f"30/01/2020:     ----(wd)    2000(db)    72000(b)")
            print(f"08/02/2020:     6500(wd)    ----(db)    65500(b)")
            print(f"21/02/2020:     1200(wd)    ----(db)    64300(b)")
            print(f"05/03/2020:     ----(wd)    1000(db)    65300(b)")
            print(f"27/03/2020:     2000(wd)    ----(db)    63300(b)")
            print(f"06/04/2020:     3300(wd)    ----(db)    60000(b)")
            print(f"08/04/2020:     5000(wd)    ----(db)    55000(b)")
            print(f"12/04/2020:     ----(wd)    1000(db)    56000(b)")
            print(f"20/04/2020:     1200(wd)    ----(db)    64800(b)")
            print(f"Your Closing Balance is: 64800.00")
        elif ta in ('half yr', 'Half yearly', 'half yearly', 'hy', 'hyr'):
            print("Your Half Yearly Transaction(s) is/are: ")
            print()
            print(f"Your Openning Balance is: 65000.00")
            print(f"05/01/2020:     1200(wd)    ----(dp)    65000(b)")
            print(f"10/01/2020:     ----(wd)     500(dp)    70000(b)")
            print(f"30/01/2020:     ----(wd)    2000(db)    72000(b)")
            print(f"08/02/2020:     6500(wd)    ----(db)    65500(b)")
            print(f"21/02/2020:     1200(wd)    ----(db)    64300(b)")
            print(f"05/03/2020:     ----(wd)    1000(db)    65300(b)")
            print(f"27/03/2020:     2000(wd)    ----(db)    63300(b)")
            print(f"06/04/2020:     3300(wd)    ----(db)    60000(b)")
            print(f"08/04/2020:     5000(wd)    ----(db)    55000(b)")
            print(f"Your Closing Balance is: 55000.00")
        elif ta in ('queterly', 'qurly', 'qrl', 'qtly'):
            print("Your Queterly Transaction(s) is/are: ")
            print()
            print(f"Your Openning Balance is: 65000.00")
            print(f"05/01/2020:     1200(wd)    ----(dp)    65000(b)")
            print(f"10/01/2020:     ----(wd)     500(dp)    70000(b)")
            print(f"30/01/2020:     ----(wd)    2000(db)    72000(b)")
            print(f"08/02/2020:     6500(wd)    ----(db)    65500(b)")
            print(f"21/02/2020:     1200(wd)    ----(db)    64300(b)")
            print(f"05/03/2020:     ----(wd)    1000(db)    65300(b)")
            print(f"27/03/2020:     2000(wd)    ----(db)    63300(b)")
            print(f"Your Closing Balance is: 63300.00")
        else:
            "break"
    else:
        "break"


def exsisting_acc():
    print()
    ac = int(input("Enter Account Number: "))
    if ac == 123456:
        default()
        print(f"Name: Aloke Kuamr Biswas")
        print(f"Father's Name: Surendra Kr Biswas")
        print(f"Gender: Male")
        print(f"DOB: 16/03/65")
        print(f"Aadhar Card No: 125469578965         Pan No: No")
        print(f"E-mail id: aloke.biswas@gmail.com")
        print(f"Present Address: Hakimpara, Siliguri Darjeeling")
        print(f"Permanent Address: Hakimpara, Siliguri Darjeelimg")
        print(f"Phone Number: 9476259664")
        print(f"Insurance Percentage: Not Applied")
        print(f"Inter Banking: Applied")
        print(f"ATM Card: Not Applied")
    elif ac == 33882869164:
        print()
        default()
        print(f"Name: Dibyendu Biswas")
        print(f"Father's Name: Tapan Kumar Biswas")
        print(f"Gender: Male")
        print(f"DOB: 12/03/1998")
        print(f"Aadhar Card No: 547069621112         Pan No: SK8795")
        print(f"E-mail id: dibyendubiswas@gmail.com")
        print(f"Present Address: Ashrampara Saradamoni Road, Siliguri Darjeeling")
        print(f"Permanent Address: Ashrampara Saradamoni Road, Siliguri Darjeeling")
        print(f"Phone Number: 9476289669")
        print(f"Insurance Percentage: Not Applied")
        print(f"Inter Banking: Applied")
        print(f"ATM Card: Applied")
    else:
        "break"


def create_acc0unt():
    global gender, faname1, mn, per, ibaa
    default()
    print()
    name = input("First Name: ")
    na1 = input("Have you Middle Name: ")
    if na1 in ('Yes', 'Y', "YES", 'y', 'yes'):
        mn = input("Middle Name:  ")
    elif na1 in ('no', 'No', 'n', 'NO', 'nO'):
        mn = ""
        "break"
    else:
        "break"
    lname = input("Last Name: ")
    faname = input("Father's First Name:  ")
    fn = input("Have your Father's Middle Name: ")
    if fn in ('Yes', 'Y', "YES", 'y', 'yes'):
        faname1 = input("Father's Middle Name:  ")
    elif fn in ('no', 'NO', 'n', 'nO', 'No'):
        faname1 = ""
    else:
        "break"
    faname2 = input("Father's Last Name:  ")
    gen = input("Gender(Male/Female/Other): ")
    if gen in ('Male', 'Female', 'Other'):
        gender = gen
    else:
        print("Wrong Choice")
        "break"

    dob = int(input("DOB(dd/mm/yy): "))
    aad = int(input("Aadhar Card No.: "))
    pan = input("Have you Pan card: ")

    if pan in ('Yes', 'Y', "YES", 'y', 'yes'):
        pan = input("Pan Card No.: ")
    elif pan in ('no', 'NO', 'n', 'nO', 'No'):
        pan = "Not Have"
    else:
        no = "None"
        "break"
    id = input("Have you E-mail id: ")
    if id in ('Yes', 'Y', "YES", 'y', 'yes'):
        id = input("E-mail id: ")
    elif id in ('no', 'NO', 'n', 'nO', 'No'):
        id = "Not Have"
    else:
        "break"
    present_add = input("Present Address: ")
    permanent_add = input("Present Address same as Permanent Address: ")
    if permanent_add in ('Yes', 'Y', "YES", 'y', 'yes'):
        per = present_add
    else:
        permanent_add = input("Present Address: ")
    ph = int(input("Phone Number: "))

    ins = input("Are you want to do insurance: ")
    if ins in ('Yes', 'Y', "YES", 'y', 'yes'):
        ins1 = input("Insurance For: ")
        if ins1 in ('Father', 'Mother', 'Child', 'wife', 'Grand Child', 'relative', 'Parents', 'parents'):
            ins11 = input("Enter Name: ")
            ins2 = int(input("Percentage: "))
    elif ins in ('no', 'No', 'N', 'n', 'NO', 'nO'):
        ins = "Not Applied"
    iba = input("Are you want to use Internet Banking: ")
    if iba in ('Yes', 'Y', "YES", 'y', 'yes'):
        ibaa = "You Applied"
    else:
        print("None")
        "break"
    atm = input("Are you want ATM Card: ")
    if atm in ('Yes', 'Y', "YES", 'y', 'yes'):
        atm = "You applied"
    else:
        atm = "Not applied"
        "break"
    print()
    check = input("Are you check all information: ")
    print()

    if check in ('Yes', 'Y', "YES", 'y', 'yes'):
        print()
        default()
        print()
        print(f"Name: {name} {mn} {lname}")
        print(f"Father's Name: {faname} {faname1} {faname2}")
        print(f"Gender: {gender}")
        print(f"DOB: {dob}")
        print(f"Aadhar Card No: {aad}         Pan No: {pan}")
        print(f"E-mail id: {id}")
        print(f"Present Address: {present_add}")
        print(f"Permanent Address: {per}")
        print(f"Phone Number: {ph}")
        print(f"Insurance Percentage: {ins}")
        print(f"Inter Banking: {ibaa}")
        print(f"ATM Card: {atm}")
        print()
        print("You Successfully Created Account.")


def calling():
    print("1 For Create an Account.")
    print("2. For Transaction Details.")
    print("3 For Check Existing Account.")
    print("4 For Viewe Customer list")
    print()
    ch = int(input("Enter Your Choice: "))

    if 1 <= ch <= 4:
        if ch == 1:
            create_acc0unt()
        elif ch == 2:
            transaction()
        elif ch == 3:
            exsisting_acc()
        elif ch == 4:
            customer_list()
        else:
            "break"
    else:
        print("wrong Choice.")


for i in range(6):
    print()
    print()
    calling()
