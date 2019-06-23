import time

def rec_russion_org(a,b):
    if a == 0: return 0
    if a % 2 == 0: return 2*rec_russion_org(a/2,b)
    return b + 2*rec_russion_org((a-1)/2,b)
    

def russion(a,b):
    res = 0
    while a!=0:
        if a%2==1:
            res += b
        a = a>>1
        b = b<<1        
    return res
    
def rec_russion(a,b):
    res = 0
    if a==0:
        return 0
    if a%2==1:
        res += rec_russion(a>>1,b<<1) + b
    else:
        res += rec_russion(a>>1,b<<1)
        
    return res
  
t = time.time()   
print(rec_russion_org(1234567891234512345678912345123456789123451234567891234512345678912345123456789123451234567891234512345678912345,1234567891234512345678912345123456789123451234567891234512345678912345123456789123451234567891234512345678912345))
t = time.time() - t
print("time",t)
  
t = time.time()   
print(rec_russion(1234567891234512345678912345123456789123451234567891234512345678912345123456789123451234567891234512345678912345,1234567891234512345678912345123456789123451234567891234512345678912345123456789123451234567891234512345678912345))
t = time.time() - t
print("time rec",t)

t = time.time()   
print(russion(1234567891234512345678912345123456789123451234567891234512345678912345123456789123451234567891234512345678912345,1234567891234512345678912345123456789123451234567891234512345678912345123456789123451234567891234512345678912345))
t = time.time() - t
print("time",t)


def mult(a,b):

   res = 0
   
   for i in range (a):
        res += b 
   
   return res
   
def rec_mult(a,b):

   res = 0
   if a == 0:
        return 0
   if a == 1:
        return b
   first = int(a/2)
   sec = a - first
   res += rec_mult(first,b)
   res += rec_mult(sec,b)
   return res
   
t = time.time()   
#print(rec_mult(12345678,1234567))
t = time.time() - t
print("time rec",t)

t = time.time()   
#print(mult(12345678,1234567))
t = time.time() - t
print("time",t)