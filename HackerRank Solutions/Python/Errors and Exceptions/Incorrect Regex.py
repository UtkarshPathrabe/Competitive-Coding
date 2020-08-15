import re
for i in range(int(input())):
    try:
        s = input()
        re.compile(s)
    except:
        print("False")
        continue
    print("True")