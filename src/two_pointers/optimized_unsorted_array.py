from typing import Dict, List, Tuple


def find_target_some_pair(a: List[int], target_sum: int) -> List[Tuple[int, int]]:
    pairs: List = []
    hash_map: Dict = {}
    for value in a:
        if value in hash_map:
            hash_map[value] += 1
        else:
            hash_map[value] =1
    for value in a:
        calculated_value = target_sum - value
        if calculated_value in hash_map:
            hash_map[calculated_value] -=1
            if hash_map[calculated_value] == 0:
                del hash_map[value]
            pairs.append((value, calculated_value))
    return pairs


a: List[int] = [1, 2, 3, 4, 5, 6]

print(find_target_some_pair(a, target_sum=3))
