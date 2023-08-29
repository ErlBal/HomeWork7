import random
# Bubble
from random import randint

print('Bubble')
N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print('Неотсортированный:')
print(a)

for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print('Отсортированный:')
print(a)

# Selection
print('Selection')
D = 10
arr = []
for i in range(D):
    arr.append(randint(1, 99))
print('Неотсортированный:')

print(arr)
i = 0

while i < D - 1:
    m = i
    j = i + 1
    while j < D:
        if arr[j] < arr[m]:
            m = j
        j += 1

    arr[i], arr[m] = arr[m], arr[i]

    i += 1

print('Отсортированный:')
print(arr)

# Insertion
print('Insertion')
S = 10
array = []
for i in range(S):
    array.append(randint(1, 99))
print('Неотсортированный:')
print(array)
for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and key < array[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key
print('Отсортированный:')
print(array)

# Merge
print('Merge')
def merge(A, temp, frm, mid, to):
    k = frm
    i = frm
    j = mid + 1

    while i <= mid and j <= to:
        if A[i] < A[j]:
            temp[k] = A[i]
            i = i + 1
        else:
            temp[k] = A[j]
            j = j + 1

        k = k + 1

    while i < len(A) and i <= mid:
        temp[k] = A[i]
        k = k + 1
        i = i + 1

    for i in range(frm, to + 1):
        A[i] = temp[i]


def mergesort(A):
    low = 0
    high = len(A) - 1

    temp = A.copy()

    m = 1
    while m <= high - low:

        for i in range(low, high, 2 * m):
            frm = i
            mid = i + m - 1
            to = min(i + 2 * m - 1, high)
            merge(A, temp, frm, mid, to)

        m = 2 * m

T = 10
arrr = []
for i in range(T):
    arrr.append(randint(1, 99))
if __name__ == '__main__':
    A = arrr

    print('Неотсортированный:')
    print(A)
    mergesort(A)
    print('Отсортированный:')
    print(A)
