# Returns a list of odd products from a list of numbers, using check_odd() callback to filter out any even numbers
def check_odd(number):
  if number % 2 != 0:
    return True
  return False

def find_odd_products(integers):
  odd_integers = list(set(filter(check_odd, integers)))
  odd_products = []
  while len(odd_integers) > 1:
    for ind in range(1, len(odd_integers)):
      odd_products.append([odd_integers[0], odd_integers[ind]])
    odd_integers.pop(0)
  return odd_products

# seq1 = [1,2,3,4,5,6,7,7,8,6]
# seq2 = (9,10,11,12,12,13,14,15,16,17)
# seq3 = {18,19,20,21,22,23,25,26,29}

# print(find_odd_products(seq1))
# print(find_odd_products(seq2))
# print(find_odd_products(seq3))

# Prints all items in a for loop in reverse order as their negative values
def print_for_loop(start = 10, end = 1, step = -1):
    for item in range(start, end-1, step):
        print(-item)
        
# Returns the middle three character in a string
def middle_chars(a_string):
    length = len(a_string)
    start = int(length/2 - 1.5)
    end = start + 3
    result = ""
    for num in range(start, end):
        result += a_string[num]
    return result

# print(middle_chars("JhonDipPeta"))
# print(middle_chars("JaSonAy"))

import string

# Remove all non-alphanumeric characters in a string (spaces allowed). Uses callback remove_bad() to filter out symbols.
def remove_bad(char):
    bad = string.punctuation
    for symbol in bad:
        if char == symbol:
            return False
    return True
    
def remove_symbols(my_string):
    return "".join(list(filter(remove_bad, my_string)))

# print(remove_symbols("/*Jon is @developer & musician"))
# print(remove_symbols(":( T&)VPT&S(((OAT"))

# Checks whether a given value is in a given dictionary
def check_dict_values(dictionary, value):
    if value in list(dictionary.values()):
        return True
    return False

# my_dictionary = {'a': 100, 'b': 200, 'c': 300}
# my_value = 200

# print(check_dict_values(my_dictionary, my_value))

# Checks whether a number is a "Curzon" number. A Curzon number is one where 2 to the power of that number plus 1 is divisible by two times that number plus one.
def is_curzon(numbah):
    print(numbah)
    powah = 2**numbah + 1
    multiply = 2*numbah + 1
    if powah % multiply == 0:
        return True
    return False

# print(is_curzon(5))
# print(is_curzon(10))
# print(is_curzon(14))

# Returns how much time is saved when you drive a given distance at a given speed above that of the given speed limit
def time_saved(speed_limit, your_speed, distance, time_unit="hours"):
    time_speeding = distance / your_speed
    time_at_limit = distance / speed_limit
    return f"{time_at_limit - time_speeding} {time_unit}"

# print(time_saved(80, 90, 40))
# print(time_saved(80, 90, 4000))
# print(time_saved(80, 100, 40))
# print(time_saved(80, 100, 10))

# Takes a string and returns it in Morse code 
char_to_dots = {
  'A': '.-', 
  'B': '-...', 
  'C': '-.-.', 
  'D': '-..', 
  'E': '.', 
  'F': '..-.',
  'G': '--.', 
  'H': '....', 
  'I': '..', 
  'J': '.---', 
  'K': '-.-', 
  'L': '.-..',
  'M': '--', 
  'N': '-.', 
  'O': '---',
  'P': '.--.', 
  'Q': '--.-', 
  'R': '.-.',
  'S': '...', 
  'T': '-', 
  'U': '..-', 
  'V': '...-', 
  'W': '.--', 
  'X': '-..-',
  'Y': '-.--', 
  'Z': '--..', 
  ' ': ' ', 
  '0': '-----',
  '1': '.----', 
  '2': '..---', 
  '3': '...--', 
  '4': '....-', 
  '5': '.....',
  '6': '-....', 
  '7': '--...', 
  '8': '---..', 
  '9': '----.',
  '&': '.-...', 
  "'": '.----.', 
  '@': '.--.-.', 
  ')': '-.--.-', 
  '(': '-.--.',
  ':': '---...', 
  ',': '--..--', 
  '=': '-...-', 
  '!': '-.-.--', 
  '.': '.-.-.-',
  '-': '-....-', 
  '+': '.-.-.', 
  '"': '.-..-.', 
  '?': '..--..', 
  '/': '-..-.'
}

def encode_morse(message_string):
    morse = ""
    for char in message_string:
        morse += (char_to_dots[char.capitalize()] + " ")
    return morse

# print(encode_morse("HELP ME !"))
# print(encode_morse("EDABBIT CHALLENGE"))
# print(encode_morse("sos"))

import datetime

# Checks whether "Friday the 13th" occurs in a given month and year
def has_friday_13(month, year):
    thirteenth = datetime.date(year, month, 13)
    if thirteenth.weekday() == 4:
        return True
    return False

# print(has_friday_13(1, 1985))

# Encodes a string by reversing it, replacing all vowels with a certain number, then adding "aca" at the end.
def karaca(stringer):
    if stringer.lower() != stringer:
        return "All letters MUST be lowercase, silly."
    encrypting = stringer[::-1]
    karaca_dict = {"a": "0", "e": "1", "i": "2", "o": "2", "u": "3"}
    for key in karaca_dict:
        encrypting = encrypting.replace(key, karaca_dict[key])
    encrypting += "aca"
    return encrypting
        
# print(karaca("courage the cowardly dog"))

import math

# Returns the number of given integer powers (n) between one number and another (a and b), inclusive
def powerRanger(n,a,b):
    bottom = math.ceil( a**(1/n) )
    top = math.floor( b**(1/n) )
    in_range = list(range(bottom, top+1))
    return len(in_range)
    
# print(powerRanger(2, 49, 65)) # => 2, because 7**2 and 8**2 (2 numbers) are inclusively between 49 and 65.
# print(powerRanger(3, 1, 27))
# print(powerRanger(10, 1, 5))
# print(powerRanger(5, 31, 33))
# print(powerRanger(4, 250, 1300))

# Take any number of lists of integers, combines them, and checks if all integers between the minimum and maximum of the combined list is present (redundencies not allowed)
def consecutive_combo(*args):
    combo = []
    for next_list in args:
        combo += next_list
        
    range_to_meet = range(min(combo), max(combo)+1)
    for num in range_to_meet:
        if num not in combo:
            return False
        combo.pop(combo.index(num))
        
    if len(combo) == 0:
        return True
    return False
            
# print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
# print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
# print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
# print(consecutive_combo([44, 46], [45]))
