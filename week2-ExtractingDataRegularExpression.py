
import re


file = open('regex_sum_94616.txt')


text = file.read()

numbers = re.findall('[0-9]+', text)
print(numbers)
total = sum(int(num) for num in numbers)

print(total)
file.close()
