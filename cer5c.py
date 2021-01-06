cnt = 0
sum = 0
for nums in [23,45,32,45,6,76,8745,3,32,4,335,5,45] :
	cnt = cnt + 1
	sum = sum + nums
	print(cnt ,sum ,nums)

print('average : ',sum / cnt)
