import random


letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
letters.append(" ")



def replace(word, index, letter):
    tempword = []
    for l in word:
        tempword.append(l)
    tempword[index] = letter
    retrn = ''
    for thing in tempword:
        retrn = retrn + thing
    return retrn

while True:

    goal = raw_input("Enter Goal text(letters and spaces only): ").lower()
    text = ""
    for i in range(0, len(goal)):
        text = text + letters[random.randint(0, len(letters)-1)]
        print text
    done = False
    while not done:
        for i in range(0, len(text)):
            if text[i] != goal[i]:
                 text = replace(text, i, letters[random.randint(0, len(letters)-1)])
        print text
        done = True if (text == goal) else False
            
        
    
