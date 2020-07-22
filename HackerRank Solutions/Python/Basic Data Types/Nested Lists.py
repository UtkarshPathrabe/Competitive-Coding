marksheet=[]
scorelist=[]

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet+=[[name,score]]
        scorelist+=[score]
    secondLowestScore = sorted(list(set(scorelist)))[1]
    for n, s in sorted(marksheet):
        if s==secondLowestScore:
            print(n)