###############################################################################
# This pyton file has functions to calculate the excel cell address
#
# get_formula: 
# Function that calculates the cell address, at a given offset from the 
# starting cell   
#     Example: "Sheet1!$A$1:$B$10" is the return value when 
#     sheet_name = "Sheet1", start_cell = "A1", num_row = 10, num_col = 2
#
# The following two functions are helper functions for get_formula
# conv_to_number: 
# Function to convert a given excel column name to corresponding column number.     
#     Example: "AA" gives 27, "BA" gives 53, "NY" gives 389, "TN" gives 534 
#
# conv_to_letter: 
# Function to get the excel column name, given its column number.   
#     i.e Reverse operation of conv_to_number    
#
###############################################################################

import re

def get_formula(sheet_name, start_cell, num_row = 1, num_col = 1, end_cell="A1"):
    if(end_cell == "A1"):
        end_cell = start_cell
    start_cell = start_cell.upper()
    end_cell = end_cell.upper()
    m = re.match(r"([a-zA-Z]+)([0-9]+)", start_cell)
    letter_value = m.group(1)
    number_value = m.group(2)
    start_addr = "$" + letter_value + "$" + number_value
    if(end_cell == start_cell):
        letter_value = conv_to_letter(conv_to_number(letter_value) + num_col - 1)
        number_value = str(eval(number_value) + num_row - 1)
        end_addr = "$" + letter_value + "$" + number_value
    else:
        m = re.match(r"([a-zA-Z]+)([0-9]+)", end_cell)
        letter_value = m.group(1)
        number_value = m.group(2)
        end_addr = "$" + letter_value + "$" + number_value
    ref_addr = start_addr + ":" + end_addr
    formula_string = sheet_name + "!" + ref_addr
    return formula_string

def conv_to_letter(in_num):
    in_num -= 1
    first_letter = ""
    second_letter = ""
    if(in_num >= 702):
        first_num = ((in_num - 26) // 676) % 26 
        if (first_num == 0): first_num = 26
        first_num += 64
        first_letter = chr(first_num)
    if(in_num >= 26):    
        second_num = (in_num // 26) % 26
        if (second_num == 0): second_num = 26
        second_num += 64
        second_letter = chr(second_num)
    third_num = (in_num % 26) + 64
    third_letter = chr(third_num + 1)
    letter_combo = first_letter + second_letter + third_letter
    return letter_combo

def conv_to_number(in_str):
    in_str = in_str.upper()
    excel_num = 0
    i = 1
    while(i <= len(in_str)):
        excel_num = excel_num * 26
        excel_num = excel_num + ord(in_str[i - 1 : i]) - 64
        i = i + 1
    return excel_num
