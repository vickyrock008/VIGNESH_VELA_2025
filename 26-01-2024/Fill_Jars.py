"""Animesh has  empty candy jars, numbered from  to , with infinite capacity. He performs  operations. Each operation is described by  integers, , , and . Here,  and  are indices of the jars, and  is the number of candies to be added inside each jar whose index lies between  and  (both inclusive). Can you tell the average number of candies after  operations?

Example



The array has  elements that all start at . In the first operation, add  to the first  elements. Now the array is . In the second operation, add  to the last  elements (3 - 5). Now the array is  and the average is 10. Sincd 10 is already an integer value, it does not need to be rounded.

Function Description

Complete the solve function in the editor below.

solve has the following parameters:

int n: the number of candy jars
int operations[m][3]: a 2-dimensional array of operations
Returns

int: the floor of the average number of canidies in all jars
Input Format

The first line contains two integers,  and , separated by a single space.
 lines follow. Each of them contains three integers, , , and , separated by spaces.

Constraints





Sample Input

STDIN       Function
-----       --------
5 3         n = 5, operations[] size = 3
1 2 100     operations = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
2 5 100
3 4 100
Sample Output

160"""

"logic 1:"

def solve(n, operations):
    total_candies = 0

    for operation in operations:
        a, b, k = operation
        total_candies += (b - a + 1) * k

    average_candies = total_candies // n
    return average_candies

def main():
    
    n, m = map(int, input().split())
    operations = [list(map(int, input().split())) for _ in range(m)]

    result = solve(n, operations)
    print(result)

if __name__ == "__main__":
    main()

"logic 2:"

def solve(n, operations):
    total_candies = 0

    for a, b, k in operations:
        total_candies += (b - a + 1) * k

    average_candies = total_candies // n
    return average_candies

def main():
    
    n, m = map(int, input().split())
    
    candy_jars = [0] * n

    for _ in range(m):
        a, b, k = map(int, input().split())
        for i in range(a - 1, b):
            candy_jars[i] += k

    average_candies = sum(candy_jars) // n
    print(average_candies)

if __name__ == "__main__":
    main()
