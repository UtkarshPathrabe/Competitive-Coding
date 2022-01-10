# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N = int(input())
Student = namedtuple('Student', ','.join(input().split()))
currentSum, count = 0, 0
for i in range(N):
    entry = input().split()
    student = Student(entry[0], entry[1], entry[2], entry[3])
    currentSum += int(student.MARKS)
    count += 1
print(currentSum / count)