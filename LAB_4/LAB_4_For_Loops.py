# number of attempts, that the user will input, will start at 1 and not 0 cause 1 is where it starts + includes /4 semesters
avg_sum = 0
n = 0
semester_number = 1

# CREATES RANGE - input amount of students PER SEMESTER (/4)
for n in range(4):
    student_num = int(input("Enter number of students for semester " + str(semester_number) + ": "))
    semester_number += 1
    avg_sum += student_num
    n += 1
    avg = avg_sum / 4
# After input of the 4 semesters, will calculate and print the average amongest the 4 semesters
print("The average is: " + str(avg) + ' for Programming Logic course over the last four semesters.')
