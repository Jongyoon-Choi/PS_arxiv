import sys
input=sys.stdin.readline

min_change=1000

sentence = input()
num_a=0
for c in sentence:
    if c=='a':
        num_a+=1
sentence=sentence[:-1]+sentence[:-1]
for i in range(len(sentence)//2):
    num_b=0
    for c in sentence[i:i+num_a]:
        if c=='b':
            num_b+=1
    min_change=min(min_change, num_b)
print(min_change)