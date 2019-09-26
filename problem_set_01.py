# START PROBLEM SET 01
print('PROBLEM SET 01 \n')

1st_bdfl = 'Guido van Rossum'
benevolent_dictator_for_life! = 'Guido van Rossum'
python author = 'Guido van Rossum'
python_author = 'Guido van Rossum'
lambda = 'Guido van Rossum'

# PROBLEM 01B (25 points)
# Use the appropriate operator to append (i.e., concatenate) Guido's current position
# at the Python Software Foundation (see https://www.python.org/psf/members/#officers)
# to the value assigned to the variable you chose you in Problem 01A. Assign
# the concatenated value to the variable python_foundation_officer.

# Adopt the following format for the new string:
# "<name>, President"
python_author = 'Guido van Rossum'
python_foundation_officer = python_author + ', President'

# Note use of the .join() function to join a list of items to an
# empty string in order to form a new string
print(''.join(['python_foundation_officer = ', python_foundation_officer, '\n']))

# The Zen of Python, by Tim Peters (1999)
# Mail list (1999): https://mail.python.org/pipermail/python-list/1999-June/001951.html
# PEP 20 (2004): https://www.python.org/dev/peps/pep-0020/
zen_of_python = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

print(''.join(['zen_of_python = ', zen_of_python, '\n']))

# PROBLEM 01C (25 points)
# Count the number of characters in the string assigned to the
# variable zen_of_python and assign the value to the variable num_chars.
   #print(len(zen_of_python))
num_chars = 822
print(''.join(['num_chars = ', str(num_chars), '\n']))

# PROBLEM 01D (25 points)
# Count the number of "words" separated by whitespace (word is used
# figuratively since not all the character chunks you will encounter are
# actually words) in the string assigned to the variable zen_of_python
# and assign the value to the variable num_char_chunks.
    #print(len(zen_of_python.split()))
num_char_chunks = 137
print(''.join(['num_char_chunks = ', str(num_char_chunks), '\n']))

# PROBLEM 01E (25 points)
# Use floor division to divide num_char_chunks by 19 (i.e., the number of lines
# in the Zen of Python). Return an integer rather than a floating point value.
# Assign the value to the variable avg_num_chunks_per_line.
avg_num_chunks_per_line = num_char_chunks//19
print(''.join(['avg_num_chunks_per_line = ', str(avg_num_chunks_per_line), '\n']))

# PROBLEM 01F (25 points)
# Substitute your U-M email address for all occurrences of the word "Dutch" using
# the appropriate built-in function in the zen_of_python string. Assign the modified
# Zen of Python string to a new variable named "zen_of_python_uniqname".
zen_of_python_uniqname = zen_of_python.replace('Dutch', 'ahhampto@umich.edu')
print(''.join(['zen_of_python_uniqname = ', zen_of_python_uniqname, '\n']))
