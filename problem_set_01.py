print('PROBLEM SET 01 \n')
python_author = 'Guido van Rossum'
python_foundation_officer = python_author + ', President'

print(''.join(['python_foundation_officer = ', python_foundation_officer, '\n']))

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
#print(len(zen_of_python))
num_chars = 822
print(''.join(['num_chars = ', str(num_chars), '\n']))

#print(len(zen_of_python.split(' ')))
num_char_chunks = 119

print(''.join(['num_char_chunks = ', str(num_char_chunks), '\n']))

avg_num_chunks_per_line = num_char_chunks/19
print(''.join(['avg_num_chunks_per_line = ', str(avg_num_chunks_per_line), '\n']))

zen_of_python_uniqname = zen_of_python.replace('Dutch', 'ahhampto@umich.edu')
print(''.join(['zen_of_python_uniqname = ', zen_of_python_uniqname, '\n']))
