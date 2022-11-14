#at first Im going to define a function and then I use replace method in python 

def replace_word():

    str="hello guys I am Sepehr and Im going to teach beginner friendly Python projects"
    word_to_replace=input("please select the word that you want to replace: ")
    word_replacement=input("please substitute the replacement word: ")
    print(str.replace(word_to_replace,word_replacement))


replace_word()

