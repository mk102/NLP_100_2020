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
	text = "I am an NLPer"

	ans_letter, ans_vocab = n_gram(text, 2)
	print("単語bi-gram:", ans_vocab)
	print("文字bi-gram:", ans_letter)

	return 0

if __name__ == "__main__":
	main()