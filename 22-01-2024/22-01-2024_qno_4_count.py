'''Given an integer N, write a program to count the number of digits in N.

Input Format

Example 1: Input0: N = 12345

Example 2: Input1: N = 8394

Constraints

n <= 10000

Output Format

Output0: 5 Explanation: N has 5 digits

Output1: 4 Explanation: N has 4 digits

Sample Input 0

12345
Sample Output 0

5
Sample Input 1

876349
Sample Output 1

6'''

#logic 1 using while loop
n=int(input())
def countDigit(n):
    count=0
    while(n!=0):
        digit = n%10   #taking last digit
        count+=1       #increment the count
        n=n//10        #removing the last digit
    return count
print(countDigit(n))

#logic 2 using length function
n=input()
def countDigit(n):
    n=str(n)
    count=len(n)       #using length function
    count=int(count)     
    return count
print(countDigit(n))   
