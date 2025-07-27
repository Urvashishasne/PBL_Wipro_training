def frequency_count(sentence,name):
    count=0
    for words in sentence.split():
        if words==name:
            count+=1
    return count
s="Hi Alex Welcome Alex, Good Alex"
print(frequency_count(s,'Alex'))