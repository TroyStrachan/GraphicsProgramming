
import time

def displayIntro():
    print ('You are on a planet full of dragons. In front of you,')
    print ('you see two caves. In one cave, the dragon is friendly')
    print ('and will share his treasure with you. The other dragon')
    print ('is greedy and hungry, and will eat you on sight.')
    print

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3':
        print ('Which cave will you go into? (1, 2 or 3)')
        cave = raw_input()
    return cave

def checkCave(chosenCave):
    print ('You approach the cave...')
    time.sleep(.5)
    print ('It is dark and spooky...')
    time.sleep(.5)
    print
    time.sleep(.5)

    

    if chosenCave == "1":
        print ('You are staring down a long tunnel, at the end of it there is another fork. Do you want to go left or right?')
        nextCave = raw_input()
        if nextCave == "left":
            print('You encounter a viral monkey who bit you... you have 45 seconds before you are terminally infected... Good Luck')
        else:
            print('You lived')
    elif chosenCave == "2":
        print ('A dragon appears and points down to another tunnel telling you to be careful and to choose your path wisely. Go left of right?')
        nextCave = raw_input()
        if nextCave == "left":
            print('You encounter a cute monkey, his foot is stuck under a fallen rock. You help him and for helping him...')
            time.sleep(3)
            print('he bites your hand and rips off 3 of your fingers! Then picks up the rock and crushes your head with it')
        else:
            
            print('You lived')
    else: 
        print ('You have become part of the dragon bbq!')

def main():

    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)

        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()
