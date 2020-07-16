#check the number is even or odd
num = [0,1,2,3,4,5,6,7,8,9]
i=0
while i < len(num):
    if num[i]%2==0:
        print("Even Number", num[i])
        break;
        #continue
    i=i+1
else:
    print("Odd Number", num)

