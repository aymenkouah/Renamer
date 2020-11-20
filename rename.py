import os
import math

# Functions


def file_number(dir):
    number = 0
    for f in os.scandir(dir):
        number += 1
    return number


def number_of_digits(number):
    return int(math.log10(number)) + 1


def suffix_generator(number, digits):
    number = str(number)
    if len(number) < digits:
        return (digits - len(number)) * "0" + number

    return number


def rename(dir, init_suffix, prefix, extension):
    suffix_length = number_of_digits(file_number(dir)) + 1
    file_numb = init_suffix

    for file in os.listdir(dir):
        suffix = suffix_generator(file_numb, suffix_length)
        os.rename(dir + f'\\{file}', dir + f"\\{prefix}{suffix}.{extension}")
        file_numb = int(file_numb) + 1


# Variables

dirpath = r""

prefix = ""

extension = ""

file_numb = 0

# Main code

dirpath += input("Enter the directory path: ")
dirpath = r"%s" %dirpath
prefix += input("Enter files' prefix: ")
extension += input("Enter the extension: ")
file_numb = int(input("enter the initial number: "))

rename(dirpath, file_numb, prefix, extension)
