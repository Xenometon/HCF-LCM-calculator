# Programme to find HCF and Lcm of two numbers #
n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
hcf=1
for c in range (1,min(m,n)+1):
    if m%c==0 and n%c==0:
        hcf=c
        lcm=m*n/hcf
        print("HCF:-",hcf)
        print("LCM=",lcm)
#End of the program