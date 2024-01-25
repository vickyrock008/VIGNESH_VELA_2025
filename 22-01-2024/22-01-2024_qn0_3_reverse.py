'''Given a number N reverse the number and print it.

Example 1: Input: N = 123 Output: 321 Explanation: The reverse of 123 is 321

Example 2: Input: N = 234 Output: 432 Explanation: The reverse of 234 is 432

Input Format

123

Constraints

N <= 1000

Output Format

321

Sample Input 0

123
Sample Output 0

321
Sample Input 1

2341
Sample Output 1

1432'''

#logic 1 using slicing 

n=int(input())
def reverseNum(n):
    n=str(n)
    n=n[::-1]         #reverse indexing
    n=int(n)
    return n
print(reverseNum(n))

#logic 2 using while loop
n = int(input())
def reverseNum(n):
    rev=0
    while (n!=0):
        digit=n%10         #taking last digit
        rev=rev*10+digit   #append
        n=n//10            #removing the last digit
    return rev
print(reverseNum(n))



