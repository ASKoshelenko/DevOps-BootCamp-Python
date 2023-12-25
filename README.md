>Please use branch ```python-structures``` for this task that already exist in your forked repository after you has been started task
### TASK 1
**loop.py:** Calculate n!. n! = 1 * 2 * 3 * … * (n-1) * n,  0! = 1. n >= 0.
 
**Example 1:**

*Input:*

    3

*Output:*

    6
 
**Example 2:**

*Input:*

    5

*Output:*

    120
 
### TASK 2
**digits.py:** Find sum of n-integer digits. n >= 0.
 
**Example 1:**

*Input:*

    321

*Output:*

    6
 
### TASK 3
**strings.py:** Check whether the input string is a palindrome.

**Example 1:**

*Input:*

    abcba

*Output:*

    yes

**Example 2:**

*Input:*

    test

*Output:*

    no
 
### TASK 4
**lists.py:** Consider a list (list = []). You can perform the following commands:

    insert i e: Insert integer e at position i.
    print: Print the list.
    remove e: Delete the first occurrence of integer e.
    append e: Insert integer e at the end of the list.
    sort: Sort the list.
    pop: Pop the last element from the list.
    reverse: Reverse the list.
 
Initialize your list and read in the value followed by lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

The first line contains an integer, denoting the number of commands.

Each line of the subsequent lines contains one of the commands described above.

**Example:**

*Input:*

    12
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 6
    append 9
    append 1 
    sort
    print
    pop
    reverse
    print

*Output:*

    [6, 5, 10]
    [1, 5, 9, 10]
    [9, 5, 1]

**!!!Don't convert list to string for output!!!!:**

    l = [1, 2, 3]
    print(l) # correct
    print(str(l) # wrong
 
### TASK 5
**dicts.py:** Drop empty items from a dictionary.

**Example:**

*Input:* (note, double quotes have to used in input)

    {"c1": "Red", "c2": "Green", "c3": null}

*Output:*

    {'c1': 'Red', 'c2': 'Green'}

### TASK 6
**sets.py:** Find common items in 2 lists without duplicates. Sort the result list before output.

**Example:**

*Input:*

    1 1 2 3 5 8 13 21 34 55 89
    1 2 3 4 5 6 7 8 9 10 11 12 13

*Output:*

    [1, 2, 3, 5, 8, 13]

### TASK 7
**split_join.py** (add by yourself): Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

In the string, each word is separated by single space and there will not be any extra space in the string.

**Example:**

*Input:*

    Let's take LeetCode contest

*Output:*

    s'teL ekat edoCteeL tsetnoc
