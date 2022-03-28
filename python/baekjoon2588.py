a,b= input().split()
a= int(a)
b= int(b)
c= b%10 #b의 일의자리
d= (b%100)//10 #b의 십의자리
e= b//100 #b의 백의자리
print(a*c)
print(a*d)
print(a*e)
print(a*b)