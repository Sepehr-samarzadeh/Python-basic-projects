#at first Im going to create a dictionary and then I use key-value pairs to write answers and questions
#but this time I have decided to give a seperate dictionary to questions which are keys inn this programmes and answers are going to act as values
#score system is too easy to explain 
# enjoy 



quiz={
    "question1":{
        "question":"What is the name of the Metallica band lead singer?"+"\n",
        "answer":"James Hetfield"
    },
    "question2":{
        "question":"What is the name of the Metallica band lead electric guitarist?"+"\n",
        "answer":"Kirk Hammet"
    },
    "question3":{
        "question":"What is the capital of Iran?"+"\n",
        "answer":"Tehran"
    },
    "question4":{
        "question":"Who plays the role 'Batman' in nolan series?"+"\n",
        "answer":"Chiristian Bale"
    },
    "question5":{
        "question":"Who is the lead singer of 'Guns n Roses'?"+"\n",
        "answer":"Axel Rose"
    },
}

score = 0

for key,value in quiz.items():
    print(value["question"])
    answer = input("Answer?")
    print("")
    if answer.lower() == value["answer"].lower():
        print("Correct!")
        score = score + 1
        print("your score is "  + str(score))
    else:
        print("Wrong!")
        print("the answer is: "  + str(value["answer"]))
        print("your score is: "  + str(score))

print("Now its time for valuation!"+"\n")
print("your overal score is: "  + str(score) + " and in percentage you answered," + str(score/5 *100)+"%"+"of all the questions")

if score >3 :
    print("concradulations, you have passed your exam")
else:
    print("Sorry, you have faild!")