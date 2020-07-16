#skip odd numbers or print even numbers

# Because continue jumps to the top of the loop, you don’t need to nest the print statement
# here inside an if test; the print is only reached if the continue is not run.

x=10
while x:
    x=x-1
    #if(x%2 ==0):
        #print   use this or the code below with continue
    if(x%2 !=0):continue
    print(x, end='   ')


