# nested-if
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "member" and password == "1234": #if หลัก
    print("Login successful!")
    serviece = input("Enter your service (1-2): ")
    if serviece == "1": #if ย่อย
        print("ถอนเงิน")
    elif serviece == "2": #elif ย่อย
        print("ฝากเงิน")
    else:
        print("หมายเลขบริการไม่ถูกต้อง!")
else:
    print("Invalid account!")
