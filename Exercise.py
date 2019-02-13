#-----------------------
# Exercise while
#-----------------------
'''
i = 0
star = '*'
while True:
    i += 1
    print(star * i)
    if i >= 5:
        break;
'''
#-----------------------
# Exercise for
#-----------------------
'''
sum = 0
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for i in range(len(A)):
    sum += A[i]
avg =  sum/len(A)
print("Average is %.2f" % avg)
'''
#-----------------------
# Exercise string indexing
#-----------------------
'''
motto = "Life is too short. You need Python"
print(motto[19:-7])
print(motto[0:1])
print(motto[0:-1])
print(motto[-1:5]) # nothing printed
'''
#-----------------------
# Exercise print
#-----------------------
'''
a = [1, 2, 3]
print(a)

print("life" "is" "too" "short")
print("life" + "is" + "too" + "short")
print("life", "is", "too", "short")
print("life","is","too","short")

for i in range(10):
    print(i, end='')
print('')
for i in range(10):
    print(i, end=' ')
'''
#-----------------------
# Exercise file I/O #1
#-----------------------
'''
def fib(n):
    if (n == 0): return 0
    if (n == 1): return 1
    return fib(n-1) + fib(n-2)

while True:
    arg = int(input("Input Fibonacci number: "))
    if (arg < 0):
        break
    print("result is %d" % fib(arg))
'''
#-----------------------
# Exercise file I/O #2
#-----------------------


#-----------------------
# Exercise Input argument using sys module
#-----------------------


