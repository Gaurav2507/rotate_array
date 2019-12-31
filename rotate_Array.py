def reverse(arr, st, en):
    while(st<en):
        arr[st], arr[en] = arr[en], arr[st]
        st += 1
        en -= 1

def rotate(arr, d):
    size=len(arr)
    d %= size
    reverse(arr, 0, size-1)
    reverse(arr, 0, size-d-1)
    reverse(arr, size-d, size-1)

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
d=int(input())
rotate(arr, d)
print(*arr)
