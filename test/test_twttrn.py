from twttrn import shorten

def main():
    test_avoiden_vowls()

def test_avoiden_vowls():
    assert shorten("cocokakakaabcde") == "cckkkbcd"

if __name__ == "__main__":
    main()