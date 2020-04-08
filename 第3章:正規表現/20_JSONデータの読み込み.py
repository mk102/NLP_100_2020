# -*- coding: utf-8 -*-

# define packages
import gzip
import json
import re
# write code...


def main():
	wiki_texts = []
	with gzip.open("./jawiki-country.json.gz", mode = "rt", encoding = "utf-8") as fi:
		for line in fi:
			json_data = json.loads(line)
			if re.search(r".*イギリス.*", json_data["title"]):
				wiki_texts.append(json_data["text"])

	with open("UK.txt", "w", encoding = "utf-8") as f:
		f.writelines(wiki_texts)
	return 0


if __name__ == "__main__":
	main()