# #simple for loop
#
# # for i in range(10):
# #     print(i)
#
# #------------------------------------
# #print even or odd number
# for i in range(10):
#     if i%2==0:
#         print(i)
# #-----------------------------------------
# #range with list, only  in 3.x
# populate the list with the range of values
#list(range(5))
# list(range(2,5))
# list(range(0,10,2))
# list(range(-5,5))
# list(range(-5,5,2))
# #-----------------------------------------
# #iterate  through the string
a="amrita saxena"
for i in range(len(a)):
    print(a[i])
    print(end=' ')
# # -----------------------------------------
#
# # iterate  through the string, skip elements-method-1-better performance - in mem
# a = "amrita saxena"
# for i in range(0,len(a),2):
#     print(a[i], end=' ')
#
# # -----------------------------------------

# # iterate  through the string, skip elements-method-2--use the slice concept - creates a strind obj
a = "amrita saxena"
for i in a[::2]:
    print(i, end=' ')
#
# # -----------------------------------------
#
#
# #find the lenghth of the  string and use it as list values from the range
# name="amrita"
# print(list(range(len(a))))
#
# -----------------------------------------
#change a list as it is being traversed,giving everyone a raise in an employee database list
# l=[1,2,3,4,5]
# for x in range(len(l)):
#     l[x] += 10
# print(l)
