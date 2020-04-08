# -*- coding: utf-8 -*-

# define packages

# write code...
def main():
	text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
	print(list(map(lambda x: len(x), text[:-1].split(" "))))
	return 0

if __name__ == "__main__":
	main()