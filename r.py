import random
r = random.randint(1,100)
while True:
	n = input('請猜數字：')
	if int(n) == r:
		print('終於猜對了！')
		break
	elif int(n) > r:
		print('比答案大')
	elif int(n) < r:
		print('比答案小')