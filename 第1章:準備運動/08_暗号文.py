# -*- coding: utf-8 -*-

# define packages
import re
# write code...


def cipher(text):
	ci_text = ""
	for t in text:
		if re.search("[a-z]", t):
			ci_text += chr(219-ord(t))
		else:
			ci_text += t
	return ci_text


def main():
	print(cipher("AbCd"))
	return 0


if __name__ == "__main__":
	main()