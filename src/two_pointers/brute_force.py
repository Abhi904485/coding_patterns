from typing import List, Tuple


def find_target_some_pair(a: List[int], target_sum: int) -> List[Tuple[int, int]]:
    pairs: List = []
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == target_sum:
                pairs.append((a[i], a[j]))
    return pairs


a: List[int] = [1, 2, 3, 4, 5, 6]

find_target_some_pair(a, target_sum=7)
