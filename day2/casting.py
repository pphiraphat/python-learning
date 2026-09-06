name = input("Enter your name: ") #รับค่าจากผู้ใช้และเก็บไว้ในตัวแปร name
year = int(input("Enter your birth year: ")) #รับค่าจากผู้ใช้และเก็บไว้ในตัวแปร year

print("your name is", name) #แสดงผลลัพธ์ของตัวแปร name
print("your birth year is", year) #แสดงผลลัพธ์ของตัวแปร year
print("your age is", 2026 - year, "years old") #แสดงผลลัพธ์ของตัวแปร year โดยทำการแปลงชนิดข้อมูลของตัวแปร year จาก string เป็น int ก่อนนำไปคำนวณ

print(type(name)) #แสดงชนิดข้อมูลของตัวแปร name
print(type(year)) #แสดงชนิดข้อมูลของตัวแปร year