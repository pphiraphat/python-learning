# data types
# 10//int
# 99.99//float
# 3+5j//complex

# การวสร้างตัวแปร คือการสร้างตัวแปรเพื่อเก็บข้อมูลต่างๆ โดยตัวแปรจะมีชื่อและค่าที่กำหนดให้กับมัน
name = "Phiraphat" #string
# age = 21 #int
# name, age = "Phiraphat", 21 #tuple
# print(name, age) #print variable

# เก็บข้อมูลนักเรียน (input)
# name = "OpenAI"
# # NAME = "ChatGPT"
# # 1name = "Phiraphat" ไม่สามารถตั้งชื่อตัวแปรด้วยตัวเลขนำหน้าได้
# # class = "Python" วไม่สามารถตั้งชื่อตัวแปรด้วยคำสงวนของภาษาได้
# age = 21
# grade = 4.0
# status = True
# class1 = "Python" #สามารถตั้งชื่อตัวแปรด้วยคำสงวนของภาษาได้โดยการเติมตัวเลขหรือตัวอักษรต่อท้าย
name, age, grade, status, class1 = "OpenAI", 21, 4.0, True, "Python" #สามารถสร้างตัวแปรหลายตัวพร้อมกันได้

# แสดงผลลัพธ์ของตัวแปร (output)
print("ชื่อนักเรียน", name) # จะดึงค่าของตัวแปร name ที่อยู่ล่างสุดมาแสดงผลลัพธ์ ผลลัพธ์ที่ได้คือ OpenAI
# print(NAME) # จะดึงค่าของตัวแปร NAME ผลลัพธ์ที่ได้คือ ChatGPT
print("อายุ", age) # จะดึงค่าของตัวแปร age ผลลัพธ์ที่ได้คือ 21
print("เกรด", grade) # จะดึงค่าของตัวแปร grade ผลลัพธ์ที่ได้คือ 4.0
print("สถานะ", status) # จะดึงค่าของตัวแปร status ผลลัพธ์ที่ได้คือ True
print("ชั้นเรียน", class1) # จะดึงค่าของตัวแปร class1 ผลลัพธ์ที่ได้คือ Python

# แสดงชนิดข้อมูลของตัวแปร
print(type(name))
print(type(age))
print(type(grade))
print(type(status))
