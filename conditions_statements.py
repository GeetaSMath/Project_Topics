# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal  to: a > = b

# checking condition when have one condition  greater .
a = 5
b = 20
if b > a:
  print("b is greater than a")

# checking condition one condition if previous one not true and next will pass .

a = 5
b = 5
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# checking condition which is not preceded, will pass to else part.
a = 5
b = 20
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# while loop.
i = 1
while i < 5:
  print(i)
  i += 1

# using break condition.
i = 1
while i < 5:
  print(i)
  if i == 2:
    break
  i += 1

# for loop.
val = ['geeta','math','karnataka']
for x in val:
    print(x)
for x in 'geeta':
    print(x)

# for loop with break condition
fruits = ['geeta','math','karnataka']
for x in fruits:
    print(x)
    if x == "math":
        break

#  PYTHON FUNCTION

def add_numbers(n1, n2):
    result = n1 +n2
    return result
number1 = 3
number2 = 4
result = add_numbers(number1,number2)
print("the sum is", result)

def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subject = len(marks)
    average_marks = sum_of_marks/total_subject
    return average_marks

marks = [55,64,75,80]
average_marks = find_average_marks(marks)
print("your marks", average_marks)


def compute_grade(average_marks):
    if average_marks >=80:
        grade = 'A'
    elif average_marks >=60:
        grade = 'B'
    elif average_marks >=50:
        grade = 'C'
    else:
        grade = 'F'
    return grade

tuple= (1,2,3,3,3)
x=tuple.index(3)
print(x)