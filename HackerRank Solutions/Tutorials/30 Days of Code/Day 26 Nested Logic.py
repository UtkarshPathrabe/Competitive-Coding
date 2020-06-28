Actual_Date = map(int, raw_input().split(' '))
Expected_Date = map(int, raw_input().split(' '))
fine = 0
if Expected_Date[2] < Actual_Date[2]:
    fine = 10000
elif (Expected_Date[2] == Actual_Date[2]) and (Expected_Date[1] < Actual_Date[1]):
    fine = 500 * (Actual_Date[1] - Expected_Date[1])
elif (Expected_Date[2] == Actual_Date[2]) and (Expected_Date[1] == Actual_Date[1]) and (Expected_Date[0] < Actual_Date[0]):
    fine = 15 * (Actual_Date[0] - Expected_Date[0])
print fine