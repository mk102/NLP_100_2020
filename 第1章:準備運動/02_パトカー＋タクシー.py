# -*- coding: utf-8 -*-

# define packages

# write code...
def main():
	text_1 = "パトカー"
	text_2 = "タクシー"

	text = "".join(i+j for i, j in zip(text_1, text_2))
	print(text)
	return 0

if __name__ == "__main__":
	main()