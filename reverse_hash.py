import hashlib
import string
import itertools
import sys

ascii_lowercase_letters = string.ascii_lowercase
ascii_uppercase_letters = string.ascii_uppercase
ascii_all_letters = string.ascii_letters
try_limit = 50000000

# User Input
def user_input():
    md5_hash = input("Enter MD5 hash: ")
    len_of_keyword = int(input("Enter the length of your keyword: "))

    while True:
        uppercase = str(input("Does your keyword include uppercase letters? Answer with yes or no: ").lower())
        if uppercase == 'yes':
            uppercase = True
            break
        elif uppercase == 'no':
            uppercase = False
            break
        else:
            print("Invalid answer! Please enter yes or no.")
            continue
            
    print(f"Your MD5-Hash is {md5_hash}")
    print(f"Your Keyword contains {len_of_keyword} letters")
    print(f"The number of possible combinations is {52 ** len_of_keyword if uppercase else 26 ** len_of_keyword}")
    return md5_hash, len_of_keyword, uppercase

# Generate md5 hash
def calculate_md5(keyword):
    md5_hash = hashlib.md5()
    encoded_keyword = keyword.encode('utf-8')
    md5_hash.update(encoded_keyword)
    return md5_hash.hexdigest()

# Decrypt md5 hash
def decrypt_md5_hash(hash, len_of_keyword, uppercase):
    combinations = itertools.product(ascii_all_letters, repeat=len_of_keyword) if uppercase else itertools.product(ascii_lowercase_letters, repeat=len_of_keyword)
    count = 0
    print("Brute forcing...")
    for combination in combinations:
        count += 1
        if count > try_limit:
            print("Too many combinations. Please try again with a different keyword.")
            sys.exit()
        keyword = ''.join(combination)
        if calculate_md5(keyword) == hash:
            print(f"Your Keyword is: {keyword}")
            print(f"Tries to get: {count}")
            break

def main():
    hash, len_of_combination, uppercase = user_input()
    decrypt_md5_hash(hash, len_of_combination, uppercase)

if __name__ == "__main__":
    main()
