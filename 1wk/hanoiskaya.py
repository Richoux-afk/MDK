def moveTower(n, A, B, C):
    if n >= 1:
        moveTower(n - 1, A, C, B)
        moveDisk(A,B)
        moveTower(n - 1, C, B, A)
    

def moveDisk(A, B):
    print("переместите диск","с",A,"на",B)

n = int(input())
moveTower(n,"A","B","C")



