year=int(input('年份:'))
moth=int(input('月份'))
day=int(input('日：'))
num=0
lst1=[31,28,31,30,31,30,31,31,30,31,30,31]
lst2=[31,29,31,30,31,30,31,31,30,31,30,31]
if year%400==0 or year%4==0 and year%100!=0:
	for i in range(moth-1):
		num+=lst2[i]
else:
	for i in range(moth-1):
		num+=lst1[i]
print(num+day)