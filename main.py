#!/usr/bin/python3

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

def main():
    array1 = load_file_to_list('essay-1.txt')
    array2 = load_file_to_list('essay-2.txt')

    print("Array1:", array1)
    print("Array2:", array2)

if __name__ == '__main__':
    main()