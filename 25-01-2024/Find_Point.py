"""Consider two points,  and . We consider the inversion or point reflection, , of point  across point  to be a  rotation of point  around .

Given  sets of points  and , find  for each pair of points and print two space-separated integers denoting the respective values of  and  on a new line.

Function Description

Complete the findPoint function in the editor below.

findPoint has the following parameters:

int px, py, qx, qy: x and y coordinates for points  and 
Returns

int[2]: x and y coordinates of the reflected point 
Input Format

The first line contains an integer, , denoting the number of sets of points.
Each of the  subsequent lines contains four space-separated integers that describe the respective values of , , , and  defining points  and .

Constraints

Sample Input

2
0 0 1 1
1 1 2 2
Sample Output

2 2
3 3"""

"logic 1:"

def findPoint(px, py, qx, qy):
    dx = qx - px
    dy = qy - py
    
    rx = qx + dx
    ry = qy + dy
    
    return [rx, ry]

def main():
    n = int(input())
    for _ in range(n):
        px, py, qx, qy = map(int, input().split())
        result = findPoint(px, py, qx, qy)
        print(result[0], result[1])

if __name__ == "__main__":
    main()

"logic 2:"

def find_reflected_point(px, py, qx, qy):
    dx = qx - px
    dy = qy - py
    rx, ry = qx + dx, qy + dy
    
    return rx, ry

def main():
    n = int(input())
    reflected_points = [find_reflected_point(*map(int, input().split())) for _ in range(n)]
    for rx, ry in reflected_points:
        print(rx, ry)

if __name__ == "__main__":
    main()
