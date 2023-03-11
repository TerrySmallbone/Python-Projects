with open("file1.txt") as file1:
  file1_list = [num.strip() for num in file1]
  
with open("file2.txt") as file2:
  file2_list = [num.strip() for num in file2]
# print(file1_list)
# print(file2_list)

result = [num for num in file1_list if num in file2_list]

# Write your code above 👆

print(result)


