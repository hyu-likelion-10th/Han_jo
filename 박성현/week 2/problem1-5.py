def solution(participant, completion):
    answer = ''
    
    participant.sort()
    completion.sort()

    for i in range(len(participant)):
        if(participant[i] != completion[i]): 
            return participant[i]
