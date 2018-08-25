'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    dict_list = []
    for each_key in dictionary:
        dict_list.append([each_key, dictionary[each_key]])
    dict_list = sorted(dict_list)
    print(dict_list)

def main():
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
