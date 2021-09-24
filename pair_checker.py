import re


def check_pairs(target_string:str):
    pairs_tuple = ("()", "[]", "{}")

    for char in target_string:
        if target_string == "":
            return True
        else:
            target_string = target_string.replace("()", "")
            target_string = target_string.replace("[]", "")
            target_string = target_string.replace("{}", "")

    return False


def main():
    print(check_pairs("({}){{}}[][][]["))

if __name__ == '__main__':
    main()

