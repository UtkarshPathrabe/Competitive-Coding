import sys
binary_N = '{0:b}'.format(int(raw_input().strip()))
max_ones, ones = 0, 0

for i in range(len(binary_N)):
    if binary_N[i] == '1':
        ones += 1
        if max_ones < ones:
            max_ones = ones
    else:
        ones = 0

print max_ones