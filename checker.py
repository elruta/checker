#!usr/bin/python3
# checker
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
	while True:
		cc = str(input("Enter Id:"))

		run = checker(cc)

		if run % 10 == 0:
			print("Valid")
		else:
			print("Invalid")

if __name__ == "__main__":
	main()
