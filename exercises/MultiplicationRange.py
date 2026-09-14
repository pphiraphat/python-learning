# แม่สูตรคูณแบบกำหนดช่วง
start = int(input("แม่สูตรคูณเริ่มต้น :"))
end = int(input("แม่สูตรคูณแม่สุดท้าย :"))

for number in range(start, end+1): #2-12
    print("สูตรคูณแม่ :", number)
    print("-----------")
    for i in range(1,13):
        print(number, "x", i, "=", number*i)
        print("-----------")