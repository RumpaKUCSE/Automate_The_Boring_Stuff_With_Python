lst = ['a', 'b', 'c', 'd']
print(''.join(lst))
print('_'.join(lst))
print('@'.join(lst))

text = 'Today is Sunday.'
print(text.split())
print(text.split('a'))

txt = 'Hello'
print(txt.ljust(10))
print(txt.rjust(10))
print(txt.center(10))
print(txt.ljust(10, '*'))
print(txt.rjust(10, '*'))
print(txt.center(10, '*'))

spam = ' Hello World '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())


# this section is very interesting.
import pyperclip

# pyperclip.copy('Hello world!')
print(pyperclip.paste())