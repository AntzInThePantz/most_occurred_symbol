#!/usr/bin/env python3
from operator import itemgetter
import os
import psutil
import sys
import time
import traceback

def most_occurred_letter(string, case_sensitive=True):
    """returns the most occurred symbol for a given string"""
    if not case_sensitive:
        string = string.lower()
    occurrences = {}
    for symbol in string:
        if symbol in occurrences:
            occurrences[symbol] += 1
        else:
            occurrences[symbol] = 1
    return max(occurrences.items(), key=itemgetter(1))[0]

def main():
    print("This Programm shows you the Symbol with the most occurrences")
    string = input("Please insert your String: ")
    case_sensitive = input("Should case sensitivity matter? [Y/n]")
    start = time.time()
    if case_sensitive.lower() == "y" or case_sensitive == "":
        print("Symbol '{}' had the most occurrences".format(most_occurred_letter(string)))
        end = time.time()
    elif case_sensitive.lower() == "n":
        print("Symbol '{}' had the most occurrences".format(
            most_occurred_letter(string,
            case_sensitive=False)))
        end = time.time()
    else:
        print("Abort")
        exit()
    print("Finding the the Symbol that occurred most needed {} seconds".format(end-start))
    process = psutil.Process(os.getpid())
    memory_use = process.memory_info()
    print("Memory Usage of this Program:\n{}".format(memory_use))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
    except:
        print("Died unexpectedly.\n")
        traceback.print_exc()
        sys.exit(1)
