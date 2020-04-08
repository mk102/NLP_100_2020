# -*- coding: utf-8 -*-

# define packages
import random

# write code...
def main():
	text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

	text_s = text[0]
	text_g = text[-1]
	text = [t for t in text[1:-1].split(" ") if t != ""]
	text_len = list(map(lambda x: len(x), text))

	text_rand = "".join(random.sample("".join([t for t in text if len(t) > 4]), len("".join([t for t in text if len(t) > 4]))))
	ans = []
	idx = 0
	for i, l in enumerate(text_len):
		if l > 4:
			ans.append(text_rand[idx:idx+l])
			idx += l
		else:
			ans.append(text[i])

	print(text_s + " " + " ".join(ans) + " " + text_g)

	return 0

if __name__ == "__main__":
	main()