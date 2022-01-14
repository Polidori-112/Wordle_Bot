# Wordle_Bot
Python bot that can guess the daily Wordle word correct 92.4% of the time.

I tried a new algorythm works by guessing the five words: quick, brown, shady, cleft, gimps to see what letters in the alphabet are in the actual word.

It then takes those known letters and rearranges them so that they form an actual word and adds said word to a list of possible answers. Words are removed from the list if they do not meet the following criteria:

a: Their letters do not match the known letters and known locations

b: Their letters match the location of a known letter that has an unknown location

It will also attempt to unscramble and solve for copies of known letters or one of the unknown letters (x, z, j, v) if less than 5 letters are known

This method allows me to reduce the possible answers to 1 83% of the time and guess the correct answer a total of 92% of the time (by picking a random value from a list of possible values), which I believe is decent for an automated bot. It is, however, a lesser percentage than a few of the other bots out there. Feel free to build off my code if you want to make a better algorythm.

I am confident with this percentage because the list of words that I have (words.txt) contains all of the possible wordle answers and my tests function runs the wordle simulation with every single word in that file.

NOTE: I originally wanted to get this inputting my guesses to the actual website, but am having troubles with the webscraping part. May update later with that functionality.
