import random

if __name__=="__main__":
    user_input = input()
    
    #specify an answer
    f=open("woed.txt","r")
    dictionary=f.read().splitlines()
    f.close()
    answer = random.sample(dictionary,1)[0]
    print(answer)

    if not user_input in dictionary:
        print("please input an vaild word")
        exit()
        
    #compare answer and input     
    for i in range(len(user_input)):
        if user_input[i] == answer[i]:
            print("A")
        elif user_input[i] in answer:
            print("B")
        else:
            print("X")        
