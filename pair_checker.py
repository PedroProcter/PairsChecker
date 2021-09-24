"""
    Author: Pedro Procter
    Goal: Check if all the pairs in a string are written and arranged correctly
"""

#Return True if all the pairs in the string are written and arranged correctly other ways it return False
def check_pairs(target_string:str):
    #Replace in each step the pairs that are complete 
    for char in target_string:
        #Checks if the string is empty (This means that everything was correct)
        if target_string == "":
            return True
        #Replaces the pairs it encounter with and empty string
        else:
            target_string = target_string.replace("()", "")
            target_string = target_string.replace("[]", "")
            target_string = target_string.replace("{}", "")

    return False


def main():
    print(check_pairs("({}){{}}[][][][]"))

if __name__ == '__main__':
    main()

