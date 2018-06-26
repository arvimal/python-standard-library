# Python Standard Library

These are notes taken while studying the Python standard library.

## Table of Contents

1. [`re`](https://github.com/arvimal/python-standard-library#1-re)
  1.1. [`re` Character classes](https://github.com/arvimal/python-standard-library#11-re-character-classes)
  1.2. [How to use the `re` module?](https://github.com/arvimal/python-standard-library#12-how-to-use-the-re-module)

## 1. `re`

Regular expressions, called regexes for short, are descriptions for a pattern of text.

### 1.1. `re` Character classes

Character | Action
--------- | -------
| \d | Any numeric(number) from 0 to 9|
| \D | Any character that is not a numeric(number from 0 to 9)|
| \w | Any letter, number, or underscore character. ie. word characters|
| \W | Any character that is not a letter, number, or underscore character|
| \s | Any space, tab, newline character.|
| \S | Any character that is not a space, tab, or newline.|

### 1.2. How to use the `re` module?

The `re` module is used to create a regular expression object, and operations such as `search` are done on said object.

ie.. Passing a string value representing your regular expression to `re.compile()` returns the regular expression pattern object, or regex object. The search is then run on this regex object.

To create a regex object for a 10 - digit phone number, use:

```python
In[10]: phone_number_regex = re.compile("\d\d\d\d\d\d\d\d\d\d")
```

`\d` stands for any number from 0 to 9. Hence, the `phone_number_regex` regex object will cater to any 10 - digit number.

```python
In[11]: phone_number_regex.search("0123456789")
Out[11]: < _sre.SRE_Match object; span = (0, 10), match = '0123456789' >

In[12]: phone_number_regex.search("abcdefghik")
None
```

The first search returns a matching object, whereas the second search did not.

Assigning the output to a variable tends to make things easier.

```python
In[15]: my_search = phone_number_regex.search("0123456789")

In[17]: my_search.group()
Out[17]: '0123456789'
```

In short, the steps to create and use a Regular expression object is:

1. Import the `re` module.
2. Create a Regex object by passing the desired pattern to `re.compile()`.
3. Pass the string to search for, to the regex's `search()` method, which returns a match object.
4. Call the match object's `group()` method to return the actual string.

Even though the fourth step is not required, it helps to understand that the searched string is properly matched.



