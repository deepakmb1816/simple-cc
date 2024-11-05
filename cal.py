list=[67,78,90,89,90,59]
def cal_avr(list):
    return sum(list) / len(list) if list else 0
avr_grade = cal_avr(list)
with open("avr_grade.txt", "w") as file:
    file.write(f"The average grade is: {avr_grade:.2f}")
print("Average grade calculated and written to 'average_grade.txt'")