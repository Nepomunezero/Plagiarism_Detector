#!/usr/bin/python3
import sys

def load_file_to_list(path):
    """
    Reads the entire file, splits on whitespace (spaces, newlines, tabs),
    and returns a list of words.
    """
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    # split() with no arguments splits on any whitespace
    words = text.split()
    return words

def howmany_word_appears(word, array):
    i = 0
    for item in array:
        if item == word:
            i += 1
    return i

def overall_fn(anarray, array1, array2):
    for item in anarray:
            print(f"{item} appears in array 1: {howmany_word_appears(item, array1)} times")
            print(f"{item} appears in array 2: {howmany_word_appears(item, array2)} times")

def main():
    """Main function starts by reading them files"""
    array1 = load_file_to_list('essay-1.txt')
    array2 = load_file_to_list('essay-2.txt')

    """converts everything to lowercase."""
    array1 = [item.lower() for item in array1]
    array2 = [item.lower() for item in array2]

    """Find the intersection and union of them."""
    inters_array = [item for item in array1 if item in array2]
    union_array = array1.copy()
    for item in array2:
        if item not in inters_array:
            union_array.append(item)

    common_words = len(inters_array)
    all_words = len(union_array)
    essay1_words = len(array1)
    essay2_words = len(array2)

    while(True):
        print("Enter a number from 1-4")
        print()
        print("[1] Search for common words")
        print("[2] Overall statistics")
        print("[3] Calculate Plagiarism Percentage")
        print("[4] Quit")
        prompt = str(input(">> "))
        if prompt == "1":
            print("======================")
            print("TYPE A WORD TO SEARCH FOR")
            print("=======================")
            searching = str(input(">> "))
            if searching in inters_array: 
                print(f"{searching} appears: {howmany_word_appears(searching, array1)} times in array 1")
                print(f"{searching} appears: {howmany_word_appears(searching, array2)} times in array 2")
            elif searching in array1:
                print(f"{searching} appears in Essay1 only")
            elif searching in array2:
                print(f"{searching} appears in Essay2 only")
            else:
                print("False")
        elif prompt == "2":
            print("======================")
            print("OVERALL STATISTICS")
            print("=======================")
            print(f"There are {common_words} words in common")
            print(f"Essay1 has {essay1_words - common_words} unique words")
            print(f"Essay2 has {essay2_words - common_words} unique words")
            overall_fn(inters_array, array1, array2)
        elif prompt == "3":
            print("======================")
            print("PLAGIARISM PERCENTAGE")
            print("=======================")
            plagiarism_percentage = (common_words * 100) / (all_words)
            print(f"The plagiarism percenatage is {plagiarism_percentage}")
            print("=======================")
        elif prompt == "4":
            print("======================")
            print("EXITING")
            print("=======================")
            sys.exit(0)
        else:
            print("Please enter a number between 1 and 4.")
        # elif prompt == "":
        #     print("This word doesn't appear anywhere")
        # else:
        #     print (f"the word '{str(prompt)}', appears {howmany_word_appears(str(prompt), array1)} in Essay1")
        #     print (f"the word '{str(prompt)}', appears {howmany_word_appears(str(prompt), array2)} in Essay2")
if __name__ == '__main__':
    main()