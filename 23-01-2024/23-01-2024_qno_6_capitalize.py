'''You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan'''

#logic 1 using title function
def solve(s):
    if (s.isalpha()):
        return s
    else:
        return s.title()

#logic 2 using capitalize method

def solve(s):
    li=[]
    cap=[]
    new=[]
    spt=s.split(" ")
    for i in spt:
        li.append(i[0])
    for j in li:
        cap.append(j.upper())
    for k in spt:
        f = k.capitalize()
        new.append(f)
    return " ".join(new)
