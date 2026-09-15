# เจาะลึก String
# frame = "Phiraphat"
# lname = "Boonsodakorn"

# fullname = frame + lname
# print(fullname)

# address = """
# ที่อยู่ 123
# หมู่ 5
# ซอย 5/6
# จังหวัด ขอนแก่น
# 12345
# """
# print(address)

# year = 2547
# salary = 30000
# # message = "เกิดเมื่อปี พ.ศ." + str(year)
# message = f"เกิดเมื่อปี พ.ศ. {year}" #ทำงานได้ผลลัพธ์เหมือนกัน
# age = f"ปีนี้คุณมีอายุ {2569-year} ปี"
# data = f"เงินเดือนของผม = {salary:.2f}"

# print(message)
# print(age)
# print(data)

text = "HelloPython" #0-10, -1 to -11
print(len(text))
print(text[0])
print(text[-1])

# for c in text:
#     print(c)

print(text[5:])
print(text[-6:]) #ไล่จากขวาไปซ้าย ตัวขวาสุดจะเริ่มที่ -1
print(text[:5])
print(text[3:7]) #ต้องการแสดง lopy ไล่จากซ้ายไปขวาเริ่มที่ 0 ตัวสุดท้าย +1 เสมอ
print(text[-8:-4])