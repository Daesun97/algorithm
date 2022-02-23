
def solution(s):
    number=["0","1","2","3","4","5","6","7","8","9"]
    english = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    dic={}
    for i in range(len(number)):
        dic[english[i]]=number[i]

    for key, val in dic.items():
        s= s.replace(key,val)
    return int(s)