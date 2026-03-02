def solution(nums):
    from collections import Counter
    num_count = Counter(nums)
    answer = min(len(nums)/2, len(num_count.keys()))
    return answer