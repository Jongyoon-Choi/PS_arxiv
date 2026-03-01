def solution(s):
    num_list = list(map(int, s.split()))
    num_max = str(max(num_list))
    num_min = str(min(num_list))
    return num_min + " " + num_max