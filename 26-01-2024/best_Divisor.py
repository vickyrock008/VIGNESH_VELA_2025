"""Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that  is better than  and that  is better than .

Given an integer, , can you find the divisor of  that Kristin will consider to be the best?

Input Format

A single integer denoting .

Constraints

Output Format

Print an integer denoting the best divisor of .

Sample Input 0

12
Sample Output 0

6"""

"logic 1:"

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def find_best_divisor(n):
    best_divisor = 1
    max_sum = 0

    for i in range(1, n + 1):
        if n % i == 0:
            current_sum = sum_of_digits(i)
            
            if current_sum > max_sum or (current_sum == max_sum and i < best_divisor):
                max_sum = current_sum
                best_divisor = i
    
    return best_divisor

def main():
    
    n = int(input())

    
    result = find_best_divisor(n)
    print(result)

if __name__ == "__main__":
    main()

"logic 2:"

def find_best_divisor(n):
    def digit_sum(num):
        return sum(int(digit) for digit in str(num))

    best_divisor = 1
    max_sum = 0

    for i in range(1, n + 1):
        if n % i == 0:
            current_sum = digit_sum(i)
            
            if current_sum > max_sum or (current_sum == max_sum and i < best_divisor):
                max_sum = current_sum
                best_divisor = i
    
    return best_divisor

def main():
    
    n = int(input())

    result = find_best_divisor(n)
    print(result)

if __name__ == "__main__":
    main()
