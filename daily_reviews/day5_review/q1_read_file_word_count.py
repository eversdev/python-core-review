import os
print("Current working directory:", os.getcwd())





def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        print(words)
        print("-----------")
        print("-----------")
        empty_dic = {}
        for word in words:
            #print(word)
            if word not in empty_dic:
                empty_dic[word] = 1
            else:
                empty_dic[word]+=1
            #print(empty_dic)
    
    return empty_dic



print(count_words(r'C:\Users\evers\Desktop\ProjectsPy\python-core-review\daily_reviews\day5_review\text.txt'))







#print(os.path.exists(r'C:\Users\evers\Desktop\ProjectsPy\python-core-review\daily_reviews\day5_review\text.txt'))





