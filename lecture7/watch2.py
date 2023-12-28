import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    matches = re.search(r"^(<iframe .+)?(http|https):\/\/(www\.)?youtube\.com\/embed\/(\w+)(.+)?\"(.+)?><\/iframe>$", s)
    if matches:
        video_id = matches.group(4)
        return f"https://youtu.be/{video_id}"
    else:
        return None

if __name__ == "__main__":
    main()