from typing import List, Tuple


def find_target_some_pair(a: List[int], target_sum: int) -> List[Tuple[int, int]]:
    pairs: List = []
    left, right = 0, len(a) - 1
    while left <= right:
        sum = a[left] + a[right]
        if sum < target_sum:
            left += 1
        elif sum > target_sum:
            right -= 1
        else:
            pairs.append((a[left], a[right]))
            right -= 1
    return pairs


a: List[int] = [0, 0, 0]

print(find_target_some_pair(a, target_sum=0))
