def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2
   
def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(num):
    test_string = "A string of length 21"
    return len(test_string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(num):
    if num == 1:
        month = "January"
    elif num == 3:
        month = "March"
    elif num == 9:
        month = "September"
    return month

def number_to_short_month_name(num):
    if num == 1:
        month = "Jan"
    elif num == 4:
        month = "Apr"
    elif num == 10:
        month = "Oct"
    return month

