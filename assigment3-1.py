import random

words_bank =["blue", "red", "apple", "pan", "banana"]
user_mistake=0
good_chars=[]
bad_chars=[]
x = random.randint(0, len(words_bank)-1)
word = words_bank[x]
while user_mistake<6:
    for i in range(len(word)):
       if word[i] in good_chars:
         print (word[i],end=" ")
       else:
         print("-", end=" ")

    user_cahr = input("please enter your guess:")
    if user_cahr!=1:
       if user_cahr in word:
         good_chars.append(user_cahr)
         print("true")

       else:
            bad_chars.append(user_cahr)
            user_mistake += 1
            print("wrong")
       if len(good_chars)   ==len(word):
        print("you are win")
        break


    else:
        print("enter just one caracter")
if user_mistake==6:
    print("game over")


