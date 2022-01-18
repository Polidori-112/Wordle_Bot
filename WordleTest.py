#create dictionary of words
dict = {}				
file = open("words.txt", "r")
loc = 0
for word in file:
    for char in word:
        data = word[loc:loc + 5]
        loc = loc + 6
        dict.update({data.lower():''.join(sorted(data.lower()))})
    
del dict['']   


#simulate the wordle game
#guess is inputed guess into game
#answ is the 'unknown' solution
#letters is a string of currently known correct/present (green/yellow) letters in no particular order
#final and wrong_guess are arrays of letters in their known correct and present positions respectively
def wordle(guess, letters, answ, final, wrong_guess):
    for c in range (0,5):
        #append letter if correct
        if (answ[c] == guess[c]):
            letters = letters + guess[c]
            final[c] = guess[c]
        
        #append letter if incorrect
        if (answ[c] != guess[c] and (guess[c] == answ[0] or guess[c] == answ[1]
        or guess[c] == answ[2] or guess[c] == answ[3] or guess[c] == answ[4])):
            letters = letters + guess[c]
            wrong_guess[c].append(guess[c])
            
    return letters
#remove double letters from a guess
def clean(let):    
    result = "".join(dict.fromkeys(let))
    return result 
#unscrabble the letters    
def jumble(word, dict):
    list = []
    word = ''.join(sorted(word)) #set guess in alphabetical order of characters

    for key in dict:
        if (dict[key] == word): #check if guess matches dictionary value in alphabetical order
            list.append(key) #add actial dictionary value if so
            
    return list 
#clean array based on correct placements
#only removes one value per call
def remove(guesses, wrong_guess, final):
    for n in range(0, len(guesses)):
        for i in range (0, 5):
            for j in range(0, len(wrong_guess[i])):
                if ((guesses[n][i] != final[i] and final[i] != '') 
                or guesses[n][i] == wrong_guess[i][j]):
                    del guesses[n]
                    return 
#add new possible answers to list of possible answers            
def append_answers(guesses, wrong_guess, final, answers):
    #remove incorrect answers               
    for n in range(0, len(guesses)):
        remove(guesses, wrong_guess, final)
    #add said list to list of possible answers
    for i in range(0, len(guesses)):         
        answers.append(guesses[i])
#check to see what possible answers are available after a given guess
def check_answers(let, wrong_guess, final, answers):
    #call append answers if you know all 5 values
    if (len(let) == 5):
        append_answers(jumble(let, dict), wrong_guess, final, answers)
    #call append answers guessing for each unknown letter and a double of each known letter
    elif (len(let) == 4):
        for i in range(0, 4):
            append_answers(jumble(let + let[i], dict), wrong_guess, final, answers)
        append_answers(jumble(let + 'v', dict), wrong_guess, final, answers)
        append_answers(jumble(let + 'j', dict), wrong_guess, final, answers)
        append_answers(jumble(let + 'x', dict), wrong_guess, final, answers)
        append_answers(jumble(let + 'z', dict), wrong_guess, final, answers)
    #call this function to raise let up to four letters then move through append answers
    elif (len(let) == 3):
        for i in range(0, 3):
            check_answers(let + let[i], wrong_guess, final, answers)
        check_answers(let + 'v', wrong_guess, final, answers)
        check_answers(let + 'j', wrong_guess, final, answers)
        check_answers(let + 'x', wrong_guess, final, answers)
        check_answers(let + 'z', wrong_guess, final, answers)
        
#main solving operation
#guess 5 set words to remove almost all possible letters
#unscramble the known letters to get possible guess
def method(answ):
    let = ''
    #5 words that are guessed before program creates final guess
    words = ['quick', 'brown', 'shady', 'cleft', 'gimps']
    final = ['', '', '', '', '']
    wrong_guess = [[''], [''], [''], [''], ['']]#there can be multiple wrong guesses at a given value
    answers = []
    #test the words in the array
    for i in range(0, 5):
        test = words[i]
        let = wordle(test, let, answ, final, wrong_guess)
        let = clean(let)
    
    check_answers(let, wrong_guess, final, answers)
    #print feedback on the game
    print(answ)        
    print(answers)
    #used for testing to determine correct percentage
    if (len(answers) >= 1 and answers[0] == answ):
        return 1
    else:
        return 0
#test for percentage of wins vs losses in every possible answer    
def test():
    correct = 0
    total = 0
    
    for word in dict:
        if (method(word) == 1):
            correct = correct + 1
            total = total + 1
        else:
            total = total + 1
    #print results of test
    print('\nNumber Correct: ' + str(correct))
    print('Total: ' + str(total))
    print('Percentage: ' + str(correct / total))


test()
