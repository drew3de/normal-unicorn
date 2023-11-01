#!/bin/python3 

chars = {
	# "o": "%e1%b4%bc",
	# "r": "%e1%b4%bf",
	# "1": "%c2%b9",
	"=": "%e2%81%bc",
	"/": "%ef%bc%8f",
	"-": "%ef%b9%a3",
	"#": "%ef%b9%9f",
	"*": "%ef%b9%a1",
	"'": "%ef%bc%87",
	'"': "%ef%bc%82",
	"|": "%ef%bd%9c"
}

gl = {
	"<": ["%e2%89%ae", "%ef%b9%a4", "%ef%bc%9c", "%uff1c"],
	">": ["%e2%89%af", "%ef%b9%a5", "%ef%bc%9e", "%uff1e"]
}

def gl_replace(encodedpayload):
	payloads = {i: "" for i in range(len(gl[">"]))}
	for i in encodedpayload:
		if i == "<" or i == ">":
			for x in range(len(gl[">"])):
				payloads[x] += gl[i][x]
		else:
			for x in range(len(gl[">"])):
				payloads[x] += i
	for i in range(len(gl[">"])):
		print(payloads[i])

def main():
	while(True):
		payload = input("Payload >> ")
		encodedpayload = ""
		for i in payload:
			if i in chars.keys():
				encodedpayload += chars[i]
			else: 
				encodedpayload += i

		if "<" in encodedpayload or ">" in encodedpayload:
			gl_replace(encodedpayload)
		else:
			print(encodedpayload)


if __name__ == '__main__':
	main()

