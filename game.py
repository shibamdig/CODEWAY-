import random,ques


print("Welcome to the Quiz Game".center(140))

play = input("Do you want to Play the Game? (y/n/Y/N): ".center(140))

if play == 'n' or play == 'N':
    quit()

"""
    Getting User's Profile Information
    Just Prompting the user to give his/her name
"""
userName = input("Enter Your Name : ".center(140))

#to display the rules of the game
print()
print("============================================================================================".center(140))
print("RULES OF THE GAME: ".center(140))
print("1) Questions will be MCQ type".center(140))
print("2) The quiz is of 10 marks".center(140))
print("3) For each correct answers you will be marked +2".center(140))
print("4) There is no negative markings".center(140))
print("5) After completion all the correct answers of the questions will be provided".center(140))
print("6) Once you start the game you can't quit before finishing it.".center(140))

#Displaying the rules of the Quiz Game
while True:
    quizQuestions = [] # This List will contain all the set of Questions Seleted from the Questions Set
    qindex = [] #this list will contain all the indexes of the set of ques selected from the Questions Set
    providedAnswers = [] #This List will contain all the user provided answers
    userScore = 0
    i = 1
    #Generating 5 Quiz Questions from a set of 10 Questions
    while i <= 5:
        q = random.choice(ques.questionlists)
        if q not in quizQuestions:
            quizQuestions.append(q)
            i = i+1
            qindex.append(ques.questionlists.index(q)+1)
    print()
    print("============================================================================================".center(140))
    print(" Let's Start !!".center(140))
    print("From these set of MCQ Questions only 1 Option is correct".center(140))
    print("============================================================================================".center(140))
    print()

    #Displaying the Quiz Questions and Prompting the answers of the questions from the user
    i = 0
    for q in quizQuestions:
        print("============================================================================================".center(140))
        print(q.center(140)) #displaying of the question
        answers = ques.answerset[qindex[i]] #fetching the answer set of the question
        #displaying the answer set of the question
        print(f"1: {answers[0]}".center(140))
        print(f"2: {answers[1]}".center(140))
        print(f"3: {answers[2]}".center(140))
        print(f"4: {answers[3]}".center(140))
        print()
        while True:
            try:
                ans = int(input("Enter the Correct Option for the Above Question (1/2/3/4) : ".center(140)))
                if ans>=1 and ans<=4:
                    break
                else:
                    print("============================================================================================".center(140))
                    continue
            except ValueError:
                print("enter a valid value".center(140))
                continue
        print("============================================================================================".center(140))
        providedAnswers.append(answers[ans-1])
        i = i+1

    #Calculating the Score of the Quiz 
    i = 0
    print("============================================================================================".center(140))
    for q in qindex:
        correctAnswer = ques.correctAnswers[q]
        if correctAnswer == providedAnswers[i]:
            userScore += 2
        
        print("Correct Answer : ",correctAnswer,"      User Provided Answer : ",providedAnswers[i])
        i += 1
    print("============================================================================================".center(140))
    print("The Score of {} is : {}".format(userName,userScore).center(140))
    print("============================================================================================".center(140))
    ch = input("Do you want to play the game again? (y/n): ")
    if ch == 'n' or ch == 'no':
        print("============================================================================================".center(140))
        print("Thanks for Playing !!! ".center(140))
        print("============================================================================================".center(140))
        quit()
