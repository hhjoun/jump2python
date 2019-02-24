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
    print (i, end='')
print('')
for i in range(10):
    print (i, end=' ')
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
'''
f = open("./sample.txt", 'w')
f.write('70\n')
f.write('60\n')
f.write('55\n')
f.write('75\n')
f.write('95\n')
f.write('90\n')
f.write('80\n')
f.write('80\n')
f.write('85\n')
f.write('100')
f.close();

sum = 0
f = open("sample.txt", 'r')
sample = f.readlines()
f.close()

for score in sample:
    sum += int(score)

avg = sum / len(sample)
print("average is %.2f, number of students is %d" % (avg, len(sample)))

f = open("result.txt", 'w')
f.write("average is %.2f. Number of students is %d" % (avg, len(sample)))
f.close();
'''
#-----------------------
# Exercise Input arguments using sys module
#-----------------------
'''
import sys

args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
'''
#-----------------------
# Exercise class
#-----------------------
'''
class FourCal:
    def setdata(self, first, second):
        self.a = first
        self.b = second

    def sum(self):
        return self.a + self.b

cal = FourCal()
cal.setdata(3, 4)
print("sum is %d" % cal.sum())

class HousePark:
    lastname = "Park"
    def __init__(self, firstname):
        self.fullname = self.lastname + ' ' + firstname

    def travel(self, where):
        print("%s travelled %s" % (self.fullname, where))

    def love(self, partner):
        print("%s fell in love with %s" % (self.fullname, partner.fullname))

    def fight(self, partner):
        print("%s fought with %s " % (self.fullname, partner.fullname))

    def __add__(self, partner):
        print("%s and %s got married" % (self.fullname, partner.fullname))

    def __sub__(self, partner):
        print("%s and %s divorced" % (self.fullname, partner.fullname))


class HouseKim(HousePark):
    lastname = "Kim"
    def travel(self, where, day):
        print("%s\ travelled %s during %d" % (self.fullname, where, day))

pey = HousePark("EeungYong")
juliet = HouseKim("Juliet")
pey.travel("USA")
juliet.travel("USA", 10)
pey.love(juliet)
juliet.love(pey)
pey + juliet
pey.fight(juliet)
pey - juliet
'''

#-----------------------
# Exercise thread
#-----------------------
'''
import threading
import time

def say(msg):
    while True:
        time.sleep(1)
        print(msg)

for msg in ['you', 'need', 'python']:
    t = threading.Thread(target=say, args=(msg,))
    t.daemon = True
    t.start()

for i in range(100):
    time.sleep(0.1)
    print(i)
'''
#-----------------------
# Exercise thread class
#-----------------------
'''
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, msg):
        threading.Thread.__init__(self)
        self.msg = msg
        self.daemon = True

    def run(self):
        while True:
            time.sleep(1)
            print(self.msg)

for msg in ['you', 'need', 'python']:
    f = MyThread(msg)
    f.start()

for i in range(100):
    time.sleep(0.1)
    print(i)
'''

#-----------------------
# Regular expression
#-----------------------
import re

#1
p = re.compile("a[.]{3,}b")
ex1 = 'acccb'
ex2 = 'a....b'
ex3 = 'aaab'
ex4 = 'a.cccb'
m = p.search(ex1)
print(m)
m = p.search(ex2)
print(m)
m = p.search(ex3)
print(m)
m = p.search(ex4)
print(m)

#2
p = re.compile("[a-z]+")
m = p.search("5 python")
print("start %d end %d sum %d" % (m.start(), m.end(), m.start() + m.end()))

#3
phone = """
This is phone address
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
Let's find it
"""
#p = re.compile("[a-zA-Z]\s+\d{3}[-]\d{4}[-](\d{4})", re.MULTILINE)
p = re.compile("(^[a-zA-Z]+\s+\d+[-]\d+)[-](\d+)", re.MULTILINE)
print(p.sub("\g<1>-****", phone))
#print(m)
#print(p.sub('****', m.group(1)))

# Simple solution
p = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
print(p.sub("\g<1>-****", phone))

#4


