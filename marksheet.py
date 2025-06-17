name = "Amit Kumar"

marks1 = eval(input("Enter the marks of English : "))
marks2 = eval(input("Enter the marks of Science : "))
marks3 = eval(input("Enter the marks of Mathematics : "))

print (" Student Name: " + name)
print ("Marks in English: " + str(marks1))
print("Marks in Science: " + str(marks2))
print("Marks in Mathematics: " + str(marks3))

total_marks = marks1 +marks2 + marks3
print("Total Marks: " + str(total_marks))

percentage = (total_marks /300)*100
print(" Percentage: " + str(percentage)+"%")