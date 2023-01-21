import socket
import re
import math
a=1
def prime_factor(n):
    sum=0
    while n % 2 == 0:
        sum+=2
        n = n/2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            sum+=i
            n=n/i
    if n>2:
        sum+=n
    return sum
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("chall.ctfs.me", 1009))
r1=s.recv(1024)
s.send('mohamed\n')
r2=s.recv(1024)
q = s.recv(1024)
#print q
regex = r"([a-zA-Z]+)"
k = int(q.find("{0} :".format(a)))
z = int(q.find("Sum"))
num = int(q[k+4:z-1])
p = prime_factor(num)
print p
s.send("{0}\n".format(p))
q= s.recv(2024)
print q
k = int(q.find("{0} :".format(2)))
num = int(q[k+4:])
p = prime_factor(num)
s.send("{0}\n".format(p))
print s.recv(1024)
q = s.recv(512)
print q
k = int(q.find("{0} :".format(3)))
z = int(q.find("Sum"))
num = int(q[k+4:z])
print num
p = prime_factor(num)
s.send("{0}\n".format(p))
q = s.recv(1024)
print q
print s.recv(1024)
k = int(q.find("{0} :".format(4)))
num = int(q[k+4:])
p = prime_factor(num)
s.send("{0}\n".format(p))
q = s.recv(1024)
print q
print s.recv(1024)
k = int(q.find("{0} :".format(5)))
num = int(q[k+4:])
p = prime_factor(num)
s.send("{0}\n".format(p))
q = s.recv(1024)
print q
print s.recv(1024)
k = int(q.find("{0} :".format(6)))
num = int(q[k+4:])
p = prime_factor(num)
s.send("{0}\n".format(p))
q = s.recv(1024)
print q
print s.recv(1024)
k = int(q.find("{0} :".format(7)))
num = int(q[k+4:])
p = prime_factor(num)
s.send("{0}\n".format(p))
q = s.recv(1024)
print q
print s.recv(1024)
k = int(q.find("{0} :".format(8)))
num = int(q[k+4:])
p = prime_factor(num)
s.send("{0}\n".format(p))
q = s.recv(1024)
print q
print s.recv(1024)
k = int(q.find("{0} :".format(9)))
num = int(q[k+4:])
p = prime_factor(num)
s.send("{0}\n".format(p))
q = s.recv(1024)
print q
print s.recv(1024)
k = int(q.find("{0} :".format(10)))
num = int(q[k+4:])
p = prime_factor(num)
s.send("{0}\n".format(p))
q = s.recv(1024)
print q
print s.recv(1024)
print s.recv(1024)
s.send("kiw\n")
print s.recv(1024)
