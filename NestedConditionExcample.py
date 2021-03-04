uname = input("UserName : ")
password = input ("password : " )
if uname == "Warakorn" and password == "P@ssw0rd":
    print("Login Success")
    print("****** Welcome To TorToey Calculate ******")
    print(" Select No 1. Vat Calculator")
    print(" Select No 2. Price Calculator")
    userselected = int(input(" Select No >> "))
    if userselected == 1:
        price = int (input("Price (THB): "))
        vat = 7
        result = price+(price*7/100)
        print("Detail :",price,"X7/100",result ,"THB")
    elif userselected == 2:
        Fnumber = input ("Select First Number : ")
        Lnumber = input ("Select Last Number : ")
        Total = int(Fnumber) + int(Lnumber)
        print("Total First No. + Last No. = ",Total)
    else:
        print("Error! Your Select No. 1 or 2")
else:
    print("Error! Please Check UserName Or Password")

