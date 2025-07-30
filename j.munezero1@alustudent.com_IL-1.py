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
    """
    Counts how many times a given word appears in the provided array (list).

    Parameters:
    word (str): The word to count.
    array (list): The list of words to search through.

    Returns:
    int: The number of times the word appears in the array.
    """
    i = 0  # Initialize a counter
    for item in array:
        if item == word:
            i += 1  # Increment counter if word matches
    return i  # Return the total count


def overall_fn(anarray, array1, array2):
    """
    Prints how many times each word in 'anarray' appears in both array1 and array2.

    Parameters:
    anarray (list): A list of words to search for.
    array1 (list): The first dataset (e.g., Essay 1).
    array2 (list): The second dataset (e.g., Essay 2).

    Returns:
    None: Outputs results directly via print.
    """
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

    """Finding the lengths of the arrays"""
    common_words = len(inters_array)
    all_words = len(union_array)
    essay1_words = len(array1)
    essay2_words = len(array2)
    # Start an infinite loop to keep the menu running until the user chooses to quit
    while True:
        try:
            # Display menu options to the user
            print("Enter a number from 1-4")
            print()
            print("[1] Search for common words")
            print("[2] Overall statistics")
            print("[3] Calculate Plagiarism Percentage")
            print("[4] Quit")
            
            # Get user input and remove leading/trailing whitespace
            prompt = input(">> ").strip()

            # Option 1: Search for a specific word
            if prompt == "1":
                print("======================")
                print("TYPE A WORD TO SEARCH FOR")
                print("=======================")
                # Get the word to search for, cleaned to lowercase
                searching = input(">> ").strip().lower()

                # Check where the word appears
                if searching in inters_array: 
                    print(f"{searching} appears: {howmany_word_appears(searching, array1)} times in array 1")
                    print(f"{searching} appears: {howmany_word_appears(searching, array2)} times in array 2")
                elif searching in array1:
                    print(f"{searching} appears in Essay1 only")
                elif searching in array2:
                    print(f"{searching} appears in Essay2 only")
                else:
                    print("This word doesn't appear in either essay.")
                print("======================")

            # Option 2: Show overall word statistics
            elif prompt == "2":
                print("======================")
                print("OVERALL STATISTICS")
                print("=======================")
                print(f"There are {common_words} words in common")
                print(f"Essay1 has {essay1_words - common_words} unique words")
                print(f"Essay2 has {essay2_words - common_words} unique words")
                # Print how many times each common word appears in both essays
                overall_fn(inters_array, array1, array2)
                print("=======================")

            # Option 3: Calculate and display plagiarism percentage
            elif prompt == "3":
                print("======================")
                print("PLAGIARISM PERCENTAGE")
                print("=======================")
                if all_words == 0:
                    # Handle division by zero case
                    print("Error: Cannot calculate percentage because total word count is zero.")
                else:
                    plagiarism_percentage = (common_words * 100) / all_words
                    print(f"The plagiarism percentage is {plagiarism_percentage:.2f}%")
                    print("=======================")
                    if plagiarism_percentage < 50:
                        print("Nice work. There's no plagiarism")
                    else:
                        print("Oops. Plagiarism alert please resubmit.")
                    print("======================")

            # Option 4: Exit the program
            elif prompt == "4":
                print("======================")
                print("EXITING! BYEBYE")
                print("=======================")
                break  # Exit the loop and program

            # Handle invalid input (not 1–4)
            else:
                print("Invalid input. Please enter a number between 1 and 4.")
                print("=======================")

        # Handle invalid numeric conversions (though not used here, good practice)
        except ValueError:
            print("Invalid input! Please enter a valid number or word.")
            print("=======================")

        # Handle Ctrl+C interruption and exit cleanly
        except KeyboardInterrupt:
            print("\nInterrupted by user. Exiting...")
            break

        # Catch any other unexpected errors to avoid crashing
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("=======================")


if __name__ == '__main__':
    main()
