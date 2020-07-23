if __name__ == '__main__':
    N = int(input())
    arr = [];
    for i in range(0,N):
        cmd = input().split();
        if cmd[0] == "insert":
            arr.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == "append":
            arr.append(int(cmd[1]))
        elif cmd[0] == "pop":
            arr.pop();
        elif cmd[0] == "print":
            print (arr)
        elif cmd[0] == "remove":
            arr.remove(int(cmd[1]))
        elif cmd[0] == "sort":
            arr.sort();
        else:
            arr.reverse();