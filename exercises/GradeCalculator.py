# Function to calculate grade based on score
# input
score = int(input("Enter your score: "))
print("Your score is:", score)
grade = "None"

# process
if score >= 80 and score <= 100:
    grade = "A"
elif score >= 70 and score < 80:
    grade = "B"
elif score >= 60 and score < 70:
    grade = "C"
elif score >= 50 and score < 60:
    grade = "D"
elif score >= 0 and score < 50:
    grade = "F"
else:
    grade = "N (Invalid score)"

# output
print("Your grade is:", grade)