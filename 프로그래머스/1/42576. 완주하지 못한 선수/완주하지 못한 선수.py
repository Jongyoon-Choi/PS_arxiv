def solution(participant, completion): 
    from collections import Counter
    answer = Counter(participant)
    for person in completion:
        if answer[person] == 1:
            del answer[person]
        else:
            answer[person] -= 1
    
    return list(answer.keys())[0]