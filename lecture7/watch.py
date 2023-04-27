import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    url_pattern = re.search(r"^<iframe(.+)(https?:\/\/(www\.)?youtube\.com\/embed\/)([a-z_A-Z_0-9]+)(.+)></iframe>$", s)
    if url_pattern:
        #split_url = url_pattern.groups()
        #print(split_url)
        last_part = (url_pattern.group(4))
        #print(last_part)
    return "https://youtu.be/"+last_part


if __name__ == "__main__":
    main()