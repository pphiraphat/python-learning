# ตัวตำเนินการทางตรรกะ (Logical Operators)
username = input("กรุณาใส่ชื่อผู้ใช้: ")
password = input("กรุณาใส่รหัสผ่าน: ")

# if username == "admin" and password == "1234":
#     print("เข้าสู่ระบบสำเร็จ!")
# else:
#     print("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง!")

# if username == "admin" or password == "1234":
#     print("เข้าสู่ระบบสำเร็จ!")
# else:
#     print("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง!")

if not username == "admin":
    print("เข้าสู่ระบบสำเร็จ!")
else:
    print("ข้อมูลไม่ถูกต้อง!")