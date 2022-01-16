
import time
import selenium
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
            
#create dictionary of words
dict = {}				
file = open("words.txt", "r")
loc = 0
for word in file:
    for char in word:
        data = word[loc:loc + 5]
        loc = loc + 6 #i'm lazy and don't want to format my dictionary (word) document
        dict.update({data.lower():''.join(sorted(data.lower()))})
    
del dict['']   

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
def method():
    let = ''
    #5 words that are guessed before program creates final guess
    words = ['quick', 'brown', 'shady', 'cleft', 'gimps']
    final = ['', '', '', '', '']
    wrong_guess = [[''], [''], [''], [''], ['']]
    answers = []
    #test the words in the array
    for i in range(0, 5):
        test = words[i]
        let = enter_word(test, let, final, wrong_guess)
        let = clean(let)
    
    check_answers(let, wrong_guess, final, answers)
    print(wrong_guess)
    print(final)
    #print feedback on the game        
    print(answers)
    
    return answers[0]

#open wordle website and start playing game
browser = webdriver.Firefox()
browser.get('https://www.powerlanguage.co.uk/wordle/')

time.sleep(1)

Elem = browser.find_element_by_tag_name('html')

Elem.click()

time.sleep(1)

#enters guess into wordle and returns known letters/changes final and wrong_guess arrays
def enter_word(word, let, final, wrong_guess):
    Elem.send_keys(word)
    Elem.send_keys(Keys.ENTER)
    
    time.sleep(1)
    
    
    host = browser.find_element_by_tag_name("game-app")
    firstHost = browser.find_element_by_tag_name("game-app")
    game = browser.execute_script("return arguments[0].shadowRoot.getElementById('game')", host)
    
    
    keyboard = game.find_element_by_tag_name("game-keyboard")
    
    keys = browser.execute_script("return arguments[0].shadowRoot.getElementById('keyboard')", keyboard)
    
    time.sleep(2)
    #store data of all the letters (match, match in different location, no match)
    keydata = browser.execute_script("return arguments[0].innerHTML;",keys)
    #get array of matches and matches in different locations using janky regex logic
    correctRegex = re.compile('...............correct', re.VERBOSE)
    
    matches = ['', '', '', '', '']
    n = 0
    for groups in correctRegex.findall(keydata):
        if (groups[0] != final[0] and groups[0] != final[1] and groups[0] != final[2] and groups[0] != final[3] and groups[0] != final[4]):
            matches[n] = (groups[0])
        n = n + 1
        
    presentRegex = re.compile('...............present', re.VERBOSE)
    
    nearmatches = ['', '', '', '', '']
    n = 0
    for groups in presentRegex.findall(keydata):
        nearmatches[n] = (groups[0])
        n = n + 1
        
    #add known values to arrays used in method
    for i in range (0,5):
        for j in range(0, 5):
            if (word[i] == matches[j]):
                final[i] = word[i]
                let = ''.join((let, final[i]))
            if (word[i] == nearmatches[j]):
                wrong_guess[i].append(word[i])
                let = ''.join((let, word[i]))
    print(final)
    print(wrong_guess)
    return let

#give time for user to cancel and add suspense
time.sleep(1)
#input final guess
Elem.send_keys(method())
Elem.send_keys(Keys.ENTER)

#allow time to celebrate solving it
time.sleep(8)        

browser.close()
