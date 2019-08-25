#!usr/bin/python3
# checker
import os

def checker(card):
	cc = card
	odd = 0
	even_list = cc[::2]
	even = 0

	for i in cc[::-2]:
		odd += int(i)
	for i in even_list[::-1]:
		multi = int(i) * 2
		i = multi
		if i > 9:
			i -= 9
		even += i
	sum = odd + even
	return sum

def main():
	path = os.getcwd()
	cc = open(path+"/cc.txt", "r")
	for i in cc:
		c = []
		m = []
		y = []
		cvv = []
		r = []
		for x in range(0, 16):
			c.append(i[x])
		for x in range(17, 19):
			m.append(i[x])
		for x in range(20, 24):
			y.append(i[x])
		for x in range(25, 28):
			cvv.append(i[x])

		r.append("".join(c))
		r.append("".join(m))
		r.append("".join(y))
		r.append("".join(cvv))

		run = checker(r[0])
		if run % 10 == 0:
			print("Valid:",r[0])
			w = open(path+"/valid.txt", "a")
			w.write("|".join(r))
			w.write("\n")

		else:
			print("Invalid:",r[0])
			w = open(path+"/invalid.txt", "a")
			w.write("|".joinr(r))
			w.write("\n")

if __name__ == "__main__":
	main()

else:
	main()
