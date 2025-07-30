from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_info = sorted(zip(position, speed), reverse=True)
        fleet_num = len(position)
        front_pos = car_info[0][0]
        front_speed = car_info[0][1]
        for pos, sp in car_info[1:]:
            goal_time = (target-front_pos)/front_speed
            if goal_time*sp+pos >= target:
                fleet_num -= 1
            else:
                front_pos = pos
                front_speed = sp
        return fleet_num


target = 10
position = [4, 1, 0, 7]
speed = [2, 2, 1, 1]
print(Solution().carFleet(target, position, speed))
