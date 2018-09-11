import random
import sys
import time

randomToppings = ['anchovies', 'grape tomaotes', 'bell pepper', 'potatoes', 'onions', 'oninon rings', 'ghost breath', 'devil']

# ffunction to show the list of toppings
# theList is a function itself to call apon the randomToppings list
# this is done so the len functions is used correctly
def showToppings(theList):
    print()
    if len(theList) == 0:
        print('Your pizza has no toppings.')
        print()
    else:
        print('The toppings on your pizza are:')
        print()
        for thisItem in theList:  #iterate through the list, print each item
            print('----->:  '  + thisItem + '  :<---------')




def menu():
#this allows the menu def function to be a universal menu

    def load():
        # this define function is for a loading bar 
        toolbar_width = 60

        # setup toolbar
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
        xrange = range
        for i in xrange(toolbar_width):
            time.sleep(0.1) # do real work here
                        # update the bar
            sys.stdout.write("-")
            sys.stdout.flush()

        sys.stdout.write("\n")
        time.sleep(2)
        print("alright i have returned ")
        print()
        print('yes you are that speacial for me to run out to the store for')
    
#-----------------------------------------------------------------------------------------------------------------------------------------
# main code



    toppingsList = [ ]
    while True:
        
        print()
        print()
        print('---- Operations ----')
        print('a/add         Add a topping')
        print('c/change      Change a topping')
        print('o/order       Order the pizza')
        print('p/pick random Pick a random topping for me') 
        print('q/quit        Quit')  


        print('r/remove      Remove a topping')
        print('s/startover   Start over')
        print()
        print(randomToppings)
        print()
        
        menuChoice = input('What would you like to do?: ').strip()
        print()

        if (menuChoice == 'a') or (menuChoice == 'add'):  #add a topping
            newTopping = input(' Type in a topping to add: ').strip()
            toppingsList.append(newTopping)  #append adds to the end of a list
            if menuChoice not in randomToppings:
                
                
                print(' one second let me run to the store and put your order in the oven to stay warm')
                print()
                load()
                
                
            
            
                
                



        elif (menuChoice == 'c') or (menuChoice == 'change'):  #change a topping
            oldTopping = input('What topping would you like to change: ')
            if oldTopping in toppingsList:  # is it in the list
                index = toppingsList.index(oldTopping)  #find out where it is in the list
                newTopping = input('What is the new topping: ')
                toppingsList[index] = newTopping   # set a new value at that index
            else:
                print(oldTopping, 'was not found.')

        elif (menuChoice == 'o') or (menuChoice == 'order'):  #order the pizza
            showToppings(toppingsList)
            load()
            print()
            print('Thanks for your order!')
            print 
            another = input('Would you like to order again (y/n) ? ')
            if another == 'y':  
                toppingsList = [ ]
            else:
                break

        elif (menuChoice == 'p') or (menuChoice == 'pick random'):  #pick random
            randomTopping = random.choice(randomToppings)
            print('For you, I randomly chose to add: ', randomTopping)
            print('and added it to your toppings.')
            toppingsList.append(randomTopping)

        elif (menuChoice == 'q') or (menuChoice == 'quit'): #quit
            break
        
        elif (menuChoice == 'r') or (menuChoice == 'remove'):  #remove a topping
            delTopping = input('What topping would you like to remove: ')
            if delTopping in toppingsList:  #check to see if the topping is in our list
                index = toppingsList.index(delTopping)  # find out where it is
                toppingsList.pop(index)    # remove it
                                        #  same as: del toppingsList[index]
                                        #  same as:  toppingsList.remove(delTopping)
                # The code above only removes the first occurrence of the topping.  
            else:
                print(delTopping, 'was not found')
                
        elif (menuChoice == 's') or (menuChoice == 'startover'):  #reset to no toppings
            print("OK, let's start over.")
            toppingsList = [ ]  #reset to the empty list

        else:
            print("Uh ... sorry, I'm not sure what you said, please try again.")
            print()
            print('or would you like to add this strange topping to your order')

        showToppings(toppingsList)  # show the list of toppings on the pizza
    
    print()
    print('Goodbye')
menu()
