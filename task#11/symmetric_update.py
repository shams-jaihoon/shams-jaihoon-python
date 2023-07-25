# Remove the items that are present in both sets, AND insert the items that is not present in both sets:

# Return a set that contains all items from both sets, except items that are present in both sets:

pythonStudentEven = {"esmat", "zafar", "shams", "husna", "yousuf"}
pythonStudentOdd = {"esmat", "younus", "akbar", "samim", "shukiba","shams"}

pythonStudentEven.symmetric_difference_update(pythonStudentOdd)

print(pythonStudentEven)


