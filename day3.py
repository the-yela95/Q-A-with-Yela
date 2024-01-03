
#Final_Project
print ("Welcome to the Q&A with Yela Game!")
print('''           _                       
           | |                      
__   _____ | | ___ __ _ _ __   ___  
\ \ / / _ \| |/ __/ _` | '_ \ / _ \ 
 \ V / (_) | | (_| (_| | | | | (_) |
  \_/ \___/|_|\___\__,_|_| |_|\___/ 
                                    ''')
                                    

name= input("What\'s your name?\n")
print (f"Welcome {name} to Q&A with Yela.\nLet's see how far you can go.")

question= input("What\'s my birth month?\nJanuary, July, December?\n")
question1 = question.lower()

if question1 == "september":    
    question2 = input("What trait of mine do I value the most?\nMoney or Friendship\n")
    question2_1 = question2.lower()
    if question2_1 == "friendship":
        question3 = input("Use a, b, c\nIf I was arrested for doing something wrong. What would that be.\na. Clubbing and Partying\nb. Bad food combo\nc. Listening to Christian Music\n")
        question3_1 = question3.lower()
        if question3_1 == "a":
            print("oops. I don\'t attend parties. I'm always on my bed.")
        elif question3_1 == "b":
            print("Welldone, you are indeed a fan of Yela.")
        elif question3_1 == "c":
            recommendation = input("I'll be glad. Please recommend more gospel songs for me\n")
            print (f"Thank you for recommending {recommendation}, I will check it out.")
            print ("\nThanks for testing my code")
    else:
        print("You failed. Try Again")    
else: 
    print("You failed. Try Again")