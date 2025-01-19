# Import the haslib library to calculate hashes from strings
import hashlib
# Import string library to use the ascii alphabet
import string
# Use itertools to generate combinations
import itertools
# Import time library to measure the execution time of a function
import time

from resources.hash import md5_hash

# Alphabet with first lowercase letters
ascii_lowercase_letters = string.ascii_lowercase
# Alphabet with first lowercase letters
ascii_uppercase_letters = string.ascii_uppercase
# Alphabet with uppercase and lowercase letters
ascii_all_letters = string.ascii_letters


# User Input
def user_input():
    md5_hash = input("Enter MD5 hash: ")
    # num_of_letters = int(input("Enter number of letters: "))
    len_of_keyword = int(input("Enter the length of your keyword: "))
    # Ask User if the Keyword contains uppercase letters and validate his answer
    while True:
        try:
            uppercase = str(input("Does your keyword include uppercase letters? Answer with yes or no: ").lower())
            if uppercase == 'yes':
                uppercase = True
                break
            elif uppercase == 'no':
                uppercase = False
                break
            else:
                print("Please enter yes or no")
                continue
        except ValueError:
            print("Invalid answer! Please enter yes or no.")
    return md5_hash, len_of_keyword, uppercase


def define_num_of_letters(uppercase):
    # if uppercase == True:
    #     len_of_combination = 52
    # else:
    #     len_of_combination = 26
    # return len_of_combination

    # shorthand
    return 52 if uppercase else 26


def combinations(iterable, r):
    # combinations('ABCD', 2) → AB AC AD BC BD CD
    # combinations(range(4), 3) → 012 013 023 123

    # Import Code-Snippet from: https://docs.python.org/3/library/itertools.html#itertools.combinations get all possible combinations of the given letters
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))

    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


# calculate number of possibilities
def calculate_possibilities(num_of_letters, len_of_keyword):
    result = num_of_letters ** len_of_keyword
    return result


# Calculate md5 hash
def calculate_md5(keyword):
    # Erstelle ein hashlib Objekt für den MD5 Algorithmus
    md5_hash = hashlib.md5()

    # Codiere den Text in Bytes, da hashlib nur Bytes akzeptiert
    encoded_keyword = keyword.encode('utf-8')

    # Aktualisiere den Hash mit dem codierten Text
    md5_hash.update(encoded_keyword)

    # Gib den Hash als hexadezimale Zeichenkette zurück
    return md5_hash.hexdigest()

def decrypt_md5_hash(hash, len_of_keyword, uppercase):
    # call the num_of_letters function and save the return value into the variable
    num_of_letters = define_num_of_letters(uppercase)
    # call the calculate_possibilities function, provide it with arguments num_of_letters and len_of_combinations and save the return value into tha variable
    possibilities = calculate_possibilities(num_of_letters, len_of_keyword)
    # keyword = ("aavc")

    # call the itertools function, get all combinations and save them into the combinations variable
    if uppercase == True:
        combinations = itertools.product(ascii_all_letters, repeat=len_of_keyword)
    else:
        combinations = itertools.product(ascii_lowercase_letters, repeat=len_of_keyword)

    # initialize an empty list to safe all combinations inside of it
    list_of_combinations = []
    # loop through all combinations saved inside the combinations variable, join each combination to one string together and safe combination for combination inside the empty list_of_combinations
    for combination in combinations:
        combination = ''.join(combination)
        list_of_combinations.append(combination)

    # compare each generated hash from a combination in the list with the given hash from the user
    def compare_hash():
        # loop through the list of all combinations
        for keyword in list_of_combinations:
            # generate a md5 hash for each combination in the list and save it inside the md5_hash variable
            md5_hash = calculate_md5(keyword)
            # compare each hash generated from each combination
            # if the generated hash from a combination matches the given hash from the user we found the keyword
            if md5_hash == hash:
                return keyword

    # call the compare function and save the returned keyword inside the keyword variable
    keyword = compare_hash()

    info = f"""
    Your MD5 hash is {hash}
    Your keyword contains {len_of_keyword} letters
    The number of possible combinations is {num_of_letters}^{len_of_keyword} -> {possibilities}
    Your Keyword is {keyword}
    """
    print(info)
    for i in range(1000000):
        pass


def main():
    # call user_input function and save the returned values of the function into variables
    hash, len_of_combination, uppercase = user_input()

    # Start measure the time
    start_time = time.perf_counter()

    # Call the decrypt function
    decrypt_md5_hash(hash, len_of_combination, uppercase)

    # Capture the time that has elapsed since the function was started.
    end_time = time.perf_counter()

    # Calculate the execution time of the decrypt function.
    # We use the time it takes the function to decrypt a hash to abort it if it takes to long
    execution_time = (end_time - start_time)
    print(f"Execution time: {execution_time} seconds")
    if execution_time > 3:
        exit()


if __name__ == "__main__":
    main()
