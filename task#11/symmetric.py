# Return a set that contains all items from both sets, except items that are present in both sets:

pythonStudentEven = {"esmat", "zafar", "shams", "husna", "yousuf"}
pythonStudentOdd = {"esmat", "younus", "akbar", "samim", "shukiba","shams"}

ucaStudents = pythonStudentEven.symmetric_difference(pythonStudentOdd)

print(ucaStudents)


