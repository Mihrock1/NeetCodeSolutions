'''
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at
the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed.
A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination,
then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.
'''

from collections import deque
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0], reverse=True)
        print("position, speed: ", cars)

        time = list(map(lambda x: (target - x[0]) / x[1], cars))
        print("time taken: ", time)

        stack = deque()
        for i in range(len(cars)):
            if bool(stack) and time[stack[-1]] >= time[i]:
                continue
            else:
                stack.append(i)

        return len(stack)

def main():
    solution = Solution()
    target = 100
    position = [0,2,4]
    speed = [4,2,1]
    result = solution.carFleet(target, position, speed)
    print(result)

    target = 10
    position = [1,4]
    speed = [3,2]
    result = solution.carFleet(target, position, speed)
    print(result)

    target = 10
    position = [4,1,0,7]
    speed = [2,2,1,1]
    result = solution.carFleet(target, position, speed)
    print(result)

if __name__ == "__main__":
    main()