# -*- coding: utf-8 -*-

# define packages

# write code...
def main():
	text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
	ans = {}
	stop_idx = [1, 5, 6, 7, 8, 9, 15, 16, 19]
	for i, t in enumerate(text.replace(".", "").split(" ")):
		if i+1 in stop_idx:
			ans[t[0]] = i
		else:
			ans[t[:2]] = i
	print(ans)
	return 0

if __name__ == "__main__":
	main()