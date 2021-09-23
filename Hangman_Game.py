#importing required modules, random is for randomly selecting one of the words available to use for game
#whereas time is for providing necessary time span between various functions and print statements
import random,time

#using try and except to handle KeyboardInterrupt Exception, so that user can quit the game using ctrl-c whenever he wants.

try:
    #Initial statements to invite the user in the game.
    welstr = 'Welcome to Hangman game.'
    print('\n'+welstr.center(80,'-'))
    name = input('\nEnter your name : ' )
    time.sleep(1)
    print('\nHello '+name+'!. Best of luck!')
    time.sleep(1)
    print('Let\'s play Hangman! Remember, you are allowed to make only 5 incorrect guesses, else you\'ll lose.')
    time.sleep(1)
    print('The game is about to start in 3 seconds...')
    time.sleep(0.5)
    for i in range(3):
        print(str(i+1),'.',end='',sep='')
        time.sleep(1)
    print('\nHere we go!..')
    time.sleep(1)
    print('\nOne more thing, press ctrl-c to quit.OK?')
    time.sleep(1)
    
#main statement is use for intializing various global variables used in the project.
    def main():
        global count
        global display
        global word
        global already_guessed
        global length
        global playl_game
        global realword
        global d1
        words_to_guess = ["january","border","image","film","promise","kids","lungs","doll"]    #list of words used to let user guess in the game
        word = random.choice(words_to_guess)                                                    #(word)selecting random word to give to the user
        realword = word
        length = len(word)
        count = 0                                                                               #(count)to keep the track of no. of wrong guesses so that it doesn't exceed the limit.
        already_guessed = []
        play_game = ''
        d1=['_']*length                                                                         #(d1)to update the blanks that has to be displayed to the user for respective words
        display = ' '.join(d1)                                                                  #(display)to display the blanks on the screen
      
#this function is used to re-execute the game when the fist round ends if the user wants or else to exit the game.      
    def play_loop():
        global play_game
        play_game = input('\nDo you want to play again? (y//n): ')
        while play_game.lower() not in ['y','n']:
            play_game = input('\nEnter your choice correctly. Do you want to play again? (y//n): ')
        if play_game.lower() == 'y':
            main()
            hangman()
        elif play_game.lower() == 'n':
            print('\nThanks for playing.:)')
            exit()
#to display the blanks and words to the user.Major part of the game is displayed here.
    def hangman():
        global count
        global display
        global word
        global already_guessed
        global play_game
        global d1
        limit = 5   #max no. of wrong guesses that an user is allowed to make
        time.sleep(1)
        print('\n\nThis is your Hangman word: '+display)
        time.sleep(0.5)
        guess = input('Enter your guess: ')
        
        guess = guess.strip()
        if len(guess.strip())== 0 or len(guess.strip())>=2 or guess<='9':
            print('Invalid Input,Try a letter\n')
            hangman()
            
        elif guess in word:
            already_guessed.extend([guess])
            index = word.find(guess)
            word = word[:index]+ '_' + word[(index+1):]
            d1[index]=guess
            display = ' '.join(d1)
            print(display+'\n')       
            
            
            
        elif guess in already_guessed:
            print('Try another letter.\n')
            
        else:
            count+=1

            if count==1:
                time.sleep(1)
                print("   _____ \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                time.sleep(0.5)
                print('Wrong guess. '+str(limit-count)+' guesses remaining.')

            elif count == 2:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                time.sleep(0.5)
                print('Wrong guess. '+str(limit-count)+' guesses remaining.')

            elif count == 3:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                time.sleep(0.5)
                print('Wrong guess. '+str(limit-count)+' guesses remaining.')
                time.sleep(0.5)
                
                hint = input('Do you want any hint? (y/n): ')
                while hint.lower() not in ['y','n']:
                   hint = input('Enter your choice correctly. Do you want any hint (y/n): ')
                if hint.lower() == 'y':
                    hword = list(realword)
                    for i in already_guessed:
                        hword.remove(i)
                    hintword = random.choice(hword)
                    hstr = 'HINT: '+hintword
                    print('\n'+hstr.center(50))
                elif hint.lower() == 'n':
                    pass
                    

            elif count==4:
                time.sleep(1)
                print("   _____ \n"
                          "  |     | \n"
                          "  |     |\n"
                          "  |     | \n"
                          "  |     o \n"
                          "  |      \n"
                          "  |      \n"
                          "__|__\n")
                time.sleep(0.5)
                print('Wrong guess. '+str(limit-count)+' last guess remaining.Think More!')
                time.sleep(0.5)
                
                hint = input('Do you want any hint? (y/n): ')
                while hint.lower() not in ['y','n']:
                   hint = input('Enter your choice correctly. Do you want any hint (y/n): ')
                if hint.lower() == 'y':
                    hword = list(realword)
                    for i in already_guessed:
                        hword.remove(i)
                    hintword = random.choice(hword)
                    hstr = 'HINT: '+hintword
                    print('\n'+hstr.center(50))
                elif hint.lower() == 'n':
                    pass

            elif count == 5:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     o \n"
                      "  |    /|\ \n"
                      "  |    / \ \n"
                      "__|__\n")
                time.sleep(0.5)
                print('Wrong guess.You are hanged.')
                result = 'The word was:'+ realword
                print(result.center(80,'*'))
                play_loop()

        if word =='_'*length:
            print('\nCongrats! You have guessed the word correctly.')
            play_loop()

        elif count!=limit:
            hangman()

    main()
    hangman()

except KeyboardInterrupt:
    print('\n\nYou chose to quit!. Anyways, Thanks for playing. :)')
    exit()
    










































        

        

            
            
