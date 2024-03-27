file_name: str
file_name = "input1.txt"

data = open(file_name, "r")
target_value = int(data.readline())

value = data.readline()


count = 0

while value != "":
    if int(value) == target_value:
      count +=1
    value = data.readline()




# Print the count of numbers that match the target value.
print("{} values matched the target value of {}.".format(count, target_value))
