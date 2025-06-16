'''def count_words(filename):
    pass
'''
#import os
#print("Current working directory:", os.getcwd())






'''with open('daily_reviews/day5_review/text.txt', 'r') as file:
    content = file.read()
    print(content)

'''




'''
with open('daily_reviews/day5_review/text.txt', 'r') as file:
    content = file.read()
    print(content)
    words = content.split()
    print(words)
    empty_dic = {}
    
    for word in words:
        empty_dic[words] = word.count()

'''








with open('daily_reviews/day5_review/text.txt', 'r') as file:
    content = file.read()
    words = content.split()
    print(words)
    print("-----------")
    print("-----------")
    empty_dic = {}
    count = 0
    for word in words:
        #print(word)
        if word not in empty_dic:
            empty_dic[word] = 1
        else:
            empty_dic[word]+=1
    print(empty_dic)



#maybe count them indidvually first
#then once you do make a note of that like a counter and the word associated with ti

#then put them in a dicitionary?

    
 





#1 i get a string
#2 i can use split() to turn it into elements of strings
#3 i then loop through the entire string text


#loop through the entire loop and during it you will check to see 

#if element does not exist, add to empty dicitionary as key and set its count to 1
#elif element does exist set the empty_dic value to currentval+=1

#return empty_dic aka file name???










