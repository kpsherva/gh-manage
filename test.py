file = open('numbers.txt', 'r')
file_content = file.readlines()
file_content = [i.strip('\n') for i in file_content]
result = 1
for i in file_content:
    result = result * int(i)
print(result)