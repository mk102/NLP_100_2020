# -*- coding: utf-8 -*-

# define packages

# write code...
def n_gram(text, n):
	if type(text) is str:
		text = text.replace(".", " ").split(" ")

	ans_vocab = []
	for i in range(len(text)-n+1):
		ans_vocab.append([text[j] for j in range(i, i+n)])

	ans_letter = []
	text = "".join(text)
	for i in range(len(text) - n + 1):
		ans_letter.append([text[j] for j in range(i, i + n)])

	return ans_letter, ans_vocab

def main():
	text_x = "paraparaparadise"
	text_y = "paragraph"

	X, _ = n_gram(text_x, 2)
	Y, _ = n_gram(text_y, 2)

	X = ["".join(x) for x in X]
	Y = ["".join(y) for y in Y]

	print("XとYの和集合:", set(X) | set(Y))
	print("XとYの積集合:", set(X) & set(Y))
	print("XとYの差集合:", set(X) - set(Y))
	print("seがXに含まれる:", "se" in X)
	print("seがYに含まれる:", "se" in Y)
	return 0

if __name__ == "__main__":
	main()