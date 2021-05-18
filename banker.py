P = 0
R = 0


def calculateNeed(need, maxm, allot):
    for i in range(P):
        for j in range(R):
            need[i][j] = maxm[i][j] - allot[i][j]


def isSafe(avail, need, allot,r):
    visited = [0] * P
    seq = [0] * P
    count = 0
    while (count < P):
        temp = 0
        for i in range(P):
            flag = 1
            if visited[i] == 0:
                for j in range(R):
                    if need[i][j] > avail[j]:
                        flag = 0
                        break
                if flag:
                    seq[count]=i
                    count += 1
                    visited[i] = 1
                    temp = 1
                    for j in range(R):
                        avail[j] += allot[i][j]
        if temp == 0:
            break
    if count < P:
        print("No,Unsafe")
    else:
        if r != -1:
            print("Yes,Safe state P",r,"req,",sep="", end="")
        else:
            print("Yes,Safe state ",sep="", end="")
        for i in range(len(seq)):
            print("P", seq[i],sep="", end="")
            if i != len(seq) - 1:
                print(",",sep="", end="")
            else:
                print("")

# Driver code
while 1:
    P = int(input("No of processes: "))
    R = int(input("No of resources: "))
    print("Enter allocation matrix")
    allot = []
    print("    ", end="")
    for i in range(R):
        if i != R-1:
            print("R", i, " ", sep="", end="")
        else:
            print("R", i, " ", sep="")
    for i in range(P):
        print("P",i,"  ",sep="", end="")
        li = []
        li = list(map(int, input().strip().split()))[:R]
        allot.append(li)
    print("Enter max matrix")
    print("    ", end="")
    maxm = []
    for i in range(R):
        if i != R-1:
            print("R", i, " ", sep="", end="")
        else:
            print("R", i, " ", sep="")
    for i in range(P):
        print("P", i, "  ", sep="", end="")
        li = []
        li = list(map(int, input().strip().split()))[:R]
        maxm.append(li)
    print("Enter available matrix")
    for i in range(R):
        if i != R-1:
            print("R", i, " ", sep="", end="")
        else:
            print("R", i, " ", sep="")
    avail = []
    avail = list(map(int, input().strip().split()))[:R]
    avail1 = []
    for i in range(len(avail)):
        avail1.append(avail[i])
    ne = []
    for i in range(P):
        l = []
        for j in range(R):
            l.append(0)
        ne.append(l)
    calculateNeed(ne, maxm, allot)
    print("Need matrix: ")
    print("    ", end="")
    for i in range(R):
        if i != R - 1:
            print("R", i, " ", sep="", end="")
        else:
            print("R", i, " ", sep="")
    for i in range(P):
        print("P", i, "  ", sep="", end="")
        for j in range(R):
            print(ne[i][j]," ",sep="", end="")
        print("")
    x = input("Is system safe? (y,n)")
    if x == "y":
        isSafe(avail, ne, allot,-1)
    x = input("Is there a request? (y,n)")
    if x == "y":
        index = int(input("Enter index of request process P"))
        print("Enter request matrix: ")
        print("    ", end="")
        for i in range(R):
            if i != R - 1:
                print("R", i, " ", sep="", end="")
            else:
                print("R", i, " ", sep="")
        print("P", index, "  ", sep="", end="")
        req = []
        req = list(map(int, input().strip().split()))[:R]
        q = [[0 for i in range(R)] for i in range(P)]
        calculateNeed(q, maxm, allot)
        for i in range(P):
            f = 0
            for j in range(R):
                if i == index and req[j] <= q[i][j] and req[j] <= avail1[j]:
                    avail1[j] = avail1[j] - req[j]
                    allot[i][j] = allot[i][j] + req[j]
                    f = 1
                elif i == index and req[j] > q[i][j] and req[j] > avail1[j]:
                    f = 0
                    break
            if f and i == index:
                calculateNeed(ne, maxm, allot)
                isSafe(avail1, ne, allot,index)
            elif not f and i == index:
                print("NO,Unsafe")
