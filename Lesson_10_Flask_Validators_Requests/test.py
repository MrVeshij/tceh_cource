import datetime as dt

# listdate = [dt.date(2018,8,i)for i in range(1,32)]
# print(list(listdate))
# print(listdate[0])
#
# x = []
# for i in listdate:
#     x.append(i)
#
# print(x)

listdate = []

for i in range(1,32):
    listdate.append(str(dt.date(2018,8,i)))

print(listdate)