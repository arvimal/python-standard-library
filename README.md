<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Python Standard Library](#python-standard-library)
  - [1. `re`](#1-re)
    - [1.1. `re` Character classes](#11-re-character-classes)
    - [1.2. Using the `re` module](#12-using-the-re-module)
    - [1.3. Grouping pattern matching with parantheses](#13-grouping-pattern-matching-with-parantheses)
    - [1.4. Matching multiple patterns with pipe (|)](#14-matching-multiple-patterns-with-pipe-)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Python Standard Library

## 1. `re`

Regular expressions, also called regex, are descriptions for patterns of text.

The text can consist of words, numbers, spaces etc..

In Python, the `re` module provides the capability to create a regular expression object, and search/match values with it.

### 1.1. `re` Character classes

Character | Action
--------- | -------
| \d | Any numeric(number) from 0 to 9|
| \D | Any character that is not a numeric(number from 0 to 9)|
| \w | Any letter, number, or underscore character. ie. word characters|
| \W | Any character that is not a letter, number, or underscore character|
| \s | Any space, tab, newline character.|
| \S | Any character that is not a space, tab, or newline.|

### 1.2. Using the `re` module

Using the `re` module involves creating a regex pattern. The steps can be summarised as following:

* Import the `re` module.
* Create the regular expression (regex) pattern
* Compile the regex pattern to a regex object using `re.compile()`.
* Search the regex object using `<regex_object>.search(<word>)` for a match.
* Call the <regex_object> `group()` method to return the actual string.

NOTE: The fourth step is not mandatory, though it helps to understand if the searched string was properly matched.

---

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

### 1.3. Grouping pattern matching with parantheses

```python
In [6]: num_pattern = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"

In [7]: num_pattern
Out[7]: '(\\d\\d\\d)-(\\d\\d\\d)-(\\d\\d\\d\\d)'

In [9]: phone_num_group_re = re.compile(num_pattern)
Out[9]: re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)', re.UNICODE)

In [11]: phone_num_group_re.search("986-015-2544")
Out[11]: <_sre.SRE_Match object; span=(0, 12), match='986-015-2544'>

In [12]: phone_num_group_re.search("986-015-2544").group()
Out[12]: '986-015-2544'

In [15]: phone_num_group_re.search("9860152544")
<None> - <No match>
```

### 1.4. Matching multiple patterns with pipe (|)

It is possible to match the occurrence of any one of multiple strings/numbers using regex.

Checking if any from a specific list of words occur in a string (curse words for example) can be achieved through a pipe regex.

```python
In [26]: str_regex = re.compile("Great|Awesome|Excellent")

In [27]: str_regex.search("This is both Great and Excellent")
Out[27]: <_sre.SRE_Match object; span=(13, 18), match='Great'>

In [34]: str_regex.search("This is both Great and Excellent").group()
Out[34]: 'Great'

In [35]: str_regex.findall("This is both Great and Excellent")
Out[35]: ['Great', 'Excellent']
```

The search ends at the first occurrence. The above example shows that even though the sentence had both `Great` and `Excellent` in it and both were part of the regex, the search stopped and lists only `Great`.

In case you want to find all the occurrences of the regex components in the input string, use the `findall()` method on the regex object.


**IMPORTANT:** Do not put spaces in between the pipes while passing to `re.compile()`. This will fail the search. Check the example below:

```python
In [38]: str_regex = re.compile("Great | Awesome | Excellent", re.IGNORECASE)

In [39]: str_regex.search("This is great")
None - No match
In [40]: str_regex.search("This is awesome")
None - No match

In [41]: str_regex_proper = re.compile("Great|Awesome|Excellent", re.IGNORECASE)

In [42]: str_regex_proper.search("This is awesome")
Out[42]: <_sre.SRE_Match object; span=(8, 15), match='awesome'>

In [43]: str_regex_proper.search("This is great")
Out[43]: <_sre.SRE_Match object; span=(8, 13), match='great'>
```

