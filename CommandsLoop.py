# break / continue

# for counter in range(1,11):
#     if counter == 5:
#         break #หยุดเมื่อถึง 5
#     print(counter)

# for counter in range(1,11):
#     if counter == 5:
#         continue #กระโดดข้าม 5
#     print(counter)

for counter in range(1,11):
    if counter %2 == 0: #หาร 2 ลงตัว
        continue
    print(counter)

print("จบการทำงาน")