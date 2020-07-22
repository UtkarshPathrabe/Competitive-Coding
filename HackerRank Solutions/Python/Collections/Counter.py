from collections import Counter

def main():
    X = int(input())
    sizeCount = Counter(map(int, input().split()))
    earned = 0
    N = int(input())
    for _ in range(N):
        size, price = map(int, input().split())
        if(size in sizeCount and sizeCount[size]):
            sizeCount[size] -= 1
            earned += price
    print(earned)

if __name__ == '__main__':
    main()