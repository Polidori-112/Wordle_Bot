There have been many posts and articles written about what people think the optimal first word is, but many of them either don't fully understand how Wordle is programmed, have blatant mistakes in their code/logic, or both. Below is a list of the top 70 words I found, and a further description of the numbers and how I got them follows.

List:

soare:

Words Left: 973 || Tile Score: 2.43

saree:

Words Left: 995 || Tile Score: 2.16

saine:

Words Left: 1017 || Tile Score: 2.3

saice:

Words Left: 1024 || Tile Score: 2.24

roate:

Words Left: 1024 || Tile Score: 2.33

raile:

Words Left: 1034 || Tile Score: 2.31

salet:

Words Left: 1034 || Tile Score: 2.27

coate:

Words Left: 1045 || Tile Score: 2.2

raine:

Words Left: 1046 || Tile Score: 2.28

arsey:

Words Left: 1052 || Tile Score: 2.16

ariel:

Words Left: 1057 || Tile Score: 2.26

slane:

Words Left: 1058 || Tile Score: 2.27

paire:

Words Left: 1059 || Tile Score: 2.2

sared:

Words Left: 1060 || Tile Score: 2.19

caret:

Words Left: 1061 || Tile Score: 2.23

orate:

Words Left: 1064 || Tile Score: 2.3

stoae:

Words Left: 1066 || Tile Score: 2.25

sorel:

Words Left: 1068 || Tile Score: 2.21

maire:

Words Left: 1071 || Tile Score: 2.16

slier:

Words Left: 1074 || Tile Score: 2.23

carle:

Words Left: 1074 || Tile Score: 2.22

sarge:

Words Left: 1074 || Tile Score: 2.18

strae:

Words Left: 1077 || Tile Score: 2.28

carte:

Words Left: 1078 || Tile Score: 2.22

leary:

Words Left: 1078 || Tile Score: 2.17

carse:

Words Left: 1081 || Tile Score: 2.22

liane:

Words Left: 1085 || Tile Score: 2.16

porae:

Words Left: 1085 || Tile Score: 2.16

sabre:

Words Left: 1085 || Tile Score: 2.16

seral:

Words Left: 1086 || Tile Score: 2.23

soler:

Words Left: 1087 || Tile Score: 2.21

salue:

Words Left: 1088 || Tile Score: 2.15

toile:

Words Left: 1090 || Tile Score: 2.15

brane:

Words Left: 1092 || Tile Score: 2.15

stane:

Words Left: 1092 || Tile Score: 2.23

prate:

Words Left: 1094 || Tile Score: 2.2

serai:

Words Left: 1097 || Tile Score: 2.16

sager:

Words Left: 1097 || Tile Score: 2.15

parle:

Words Left: 1097 || Tile Score: 2.16

sayer:

Words Left: 1097 || Tile Score: 2.19

earnt:

Words Left: 1098 || Tile Score: 2.16

reast:

Words Left: 1099 || Tile Score: 2.23

urate:

Words Left: 1099 || Tile Score: 2.2

artel:

Words Left: 1101 || Tile Score: 2.21

taler:

Words Left: 1102 || Tile Score: 2.25

alure:

Words Left: 1106 || Tile Score: 2.16

trone:

Words Left: 1106 || Tile Score: 2.18

earst:

Words Left: 1107 || Tile Score: 2.18

aline:

Words Left: 1107 || Tile Score: 2.17

prase:

Words Left: 1109 || Tile Score: 2.19

torse:

Words Left: 1111 || Tile Score: 2.18

scrae:

Words Left: 1111 || Tile Score: 2.17

slade:

Words Left: 1111 || Tile Score: 2.15

realo:

Words Left: 1112 || Tile Score: 2.16

tares:

Words Left: 1113 || Tile Score: 2.18

siler:

Words Left: 1113 || Tile Score: 2.17

stire:

Words Left: 1115 || Tile Score: 2.21

urase:

Words Left: 1115 || Tile Score: 2.19

ratel:

Words Left: 1117 || Tile Score: 2.21

spaer:

Words Left: 1119 || Tile Score: 2.17

trape:

Words Left: 1119 || Tile Score: 2.17

stear:

Words Left: 1120 || Tile Score: 2.2

taser:

Words Left: 1121 || Tile Score: 2.23

trine:

Words Left: 1121 || Tile Score: 2.18

oater:

Words Left: 1129 || Tile Score: 2.22

lares:

Words Left: 1129 || Tile Score: 2.15

caner:

Words Left: 1135 || Tile Score: 2.15

laser:

Words Left: 1137 || Tile Score: 2.19

tears:

Words Left: 1143 || Tile Score: 2.15

rates:

Words Left: 1146 || Tile Score: 2.14


Meaning of Words Left:

To prevent the word of the day from being some obscure word such as 'aahed', the creator of Wordle has created a list of 2314 possible solutions, as can be seen alongside the longer list of possible guesses in the JS source of Wordle. Note that the 70 words in this list were generated from the longer list of possible guesses.

The words left is an average of the amount of possible words in this list of possible solutions that are still possible after feedback from this first word is given when tested with every possible solution.

So, each of the words on this list knock slightly over half of the possible solutions out of consideration.


Meaning of Tile Score:

The game will give feedback after each guess, saying whether a letter you guessed is present in another location (yellow), correctly located (green), or not in the word at all (absent). The tile score is a weighted average of the amount of present/correctly guessed letters when tested with every possible solution where a green tile is worth two points and a yellow tile is worth 1 points.

So each of these words will on average grant slightly better than either two yellow tiles or one green tile when guessed.


Analysis:

What is interesting about this data is how much of an outlier soare is.

Almost every word has a tile score increment from the next greatest of less than a hundredth of a point and a tile score increment from the next greatest of less than 5 points, but soare is the greatest in both of these metrics by a surprisingly large margin. If anyone has any explanation or speculation for this, I would love to hear it.

That being said, I personally would not recommend guessing soare first every time because it consists entirely of very popular letters that will almost certainly be entered in future guesses. As you can see, there is not that much difference between words with high vowel counts and popular consonants such as: r, t, s. So maybe try mixing up your first word with words from this list to have a little fun or pick a word from the list with relatively less popular letters such as caner.
