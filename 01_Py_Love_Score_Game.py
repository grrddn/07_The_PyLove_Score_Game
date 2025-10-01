print('''
            WELCOME TO THE LOVE SCORE GAME

This program calculates the love score between you and your crush based on the letters in the words TRUE and LOVE.


''')

your_name = input("What is your name? \n")
crush_name = input("What is your crush's name? \n")

def calculate_love_score(your_name, crush_name):
    your_name = your_name.upper()
    love_score_true = 0
    for i in "TRUE":
        for x in your_name:
            if i == x:
                love_score_true += 1
            else:
                continue
    crush_name = crush_name.upper()
    love_score_love = 0
    for i in "LOVE":
        for x in crush_name:
            if i == x:
                love_score_love += 1
            else:
                continue

    love_score = str(love_score_true) + str(love_score_love)
    print(f'\nYour love score is: {love_score}')


calculate_love_score(your_name, crush_name)