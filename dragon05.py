#Source File Name dragon05.py
#Author: Troy Strachan
#Date: May 16 2013
#Last Modified by: Troy Strachan
#Purpose: Create a game where there is multiple levels of decisions to make. Only one choice is a positive outcome.


import random
import time

def displayIntro():
    print ('You wake up, the bright sun is blinding you. You use your hand as shade to help figure out where you are.')
    print ('You try to get up. You are in a massive amount of pain but you cannot remember why.')
    time.sleep(2)
    print ('You finally muster the strength to get up. You start wandering towards what sounds like a river.')
    time.sleep(1)
    print ('As you get closer to the river you hear what sounds like a group of horses gallopping in your direction.')
    print ('The horses are carrying a bunch of warrior looking men. You over hear them describing what you are wearing')
    time.sleep(2)
    print ('You cannot understand why they are looking for you. Afterall, you cannot remember what hapened before you woke up')
    print ('Actually you cannot even remember your name!')
    time.sleep(1)
    print ('You get some water from the river and decide to move to find cover. You see a cave and begin walking into it')
    print ('Shortly after walking into the cave you see it split into two options...')
def chooseCave():
    cave = ''
    while cave != 'left' and cave != "l" and cave != 'right' and cave!="r":
        print ('Which cave will you go into? Left or right')
        cave = raw_input().lower()
    return cave

def checkCave(chosenCave):

    if chosenCave == "left" or chosenCave == "l": # first decision level
        print ('You are staring down a long tunnel, at the end of it there is another fork. Do you want to go left or right?')
        nextCave = raw_input().lower()
        if nextCave == "left":#second decision level
            print('You start hearing noises coming from deep within the cave. You begin to follow it. It is beginning to sound like a monkey. Do you want to follow it? Yes/No?')
            nextCave = raw_input().lower()
            if nextCave =="yes" or nextCave == "y": # 3rd decision 1
                print('You encounter a viral monkey who bit you... you have 45 seconds before you are terminally infected... Good Luck')
            elif nextCave == "no" or nextCave == "n": #3rd decision 2
                print('You see a light, but it is coming at you really fast. Oh wait that is ... Fire')
        elif nextCave == "right" or nextCave == "r": #second decision level
            print('You find your way out of the cave')
            time.sleep(1)
            print('Or so you thought. There is a warm breeze coming from the left tunnel... do you chance it? Left or Right?')
            nextCave = raw_input().lower()
            if nextCave == "left" or nextCave =="l": #3rd decision  3
                print ('Following the breeze may have been a bad idea... here comes a lava flow. Nice knowing you bud')
            elif nextCave == "right" or nextCave == "r": #3rd decision 4
                print ("You suddenly hear a voice - 'I am sorry to bother you sir but do you have a light?'.") 
                print ('You turn and see a dragon who smirks then slashes you into three even pieces with his sharp claws')     
            
    elif chosenCave == "right" or chosenCave == "r": # first decision level
        print ('A dragon appears and points down to another tunnel telling you to be careful and to choose your path wisely. Go left or right?')
        nextCave = raw_input().lower()
        if nextCave == "left" or nextCave == "l": #second decision level
            print('You encounter a cute monkey, his foot is stuck under a fallen rock. You help him and for helping him...')
            time.sleep(3)
            print('he bites your hand and rips off three of your fingers! Then picks up the rock and crushes your head with it')
            time.sleep(2)
            print('You wake up weary and blurry eyed.')
            time.sleep(1)
            print('You can barely make out the evil monkey who is hovering a few feet from you holding out his hand as though he means to help.')
            print('Do you grab it, Yes/No?')
            nextCave = raw_input().lower()
            if nextCave == 'y' or nextCave=='yes': #3rd decision 5
                print("You hear in your head - You're gunna have a bad time - The monkey gets an evil look on his face and starts dragging you deeper into the cave.")
                time.sleep(2)
                print('Until you feel the air getting warm. The monkey has delivered you to a momma dragon, and her offspring are looking mighty hungry - awe shit')
                time.sleep(2)
                print('Just as you feel a burst of air on the back of your neck you hear a deep, loud voice say')
                time.sleep(2)
                print("Are you ok? The monkey is sorry he bit your fingers off. He was hungry and I was unable to find his favourite bananas. Here let me help you.")
                time.sleep(4)
                print('The dragon then helps you out of the cave and flies you to the nearest hospital where you can get help')
                print('As the dragon is about to leave you he asks you if there is anything she can do for you.')
                memoryRestore = random.randint(1,2)# There is a 50/50 shot that your memory is restored
                if memoryRestore == 1:
                    print('The dragon says your memory has been restored')
                    time.sleep(5)
                    print('Your memory is restored and you DO NOT feel good about yourself. You are a horrible murderer and now you wish you had died in the cave system.')
                else:
                    print('The dragon says, I am unable to restore your memory. Maybe that is for the best. ')
                    time.sleep(1)
                    print('You thank the dragon for the ride and wander into the hospital')

            elif nextCave == "no" or nextCave == "n": #3rd decision 6
                print('The monkey looks at you feeling scorned and disrespected. He picks up the rock again and goes at you, well, like a spider monkey')
        else: #first decision level
            print('You step on a loose stone, you hear a thud then it sounds like something is rolling. You turn around and you see a ball like the one of Indiana Jones...')
            time.sleep(2)
            print('You notice a split in the tunnel coming up, go left or right?')#second decision level
            nextCave = raw_input().lower()
            if nextCave == "left" or nextCave == "l":
                print("The ball just misses you as you dive into the tunnel on the left, only to find out you found a nest full of king cobra snakes and you woke them up. They aren't very happy")
            elif nextCave == "right" or nextCave == "r":
                print("You aren't out running the giant stone ball... dive to side or keep running? Dive or Run")
                nextCave = raw_input().lower()
                if nextCave == "dive": #3rd decision level 7
                    print ('I always thought you were a bit chunky, interesting form of diet though.')
                elif nextCave == "run": #3rd decision 8
                    print('You keep running, you see a spot where the tunnel narrows and dive into it. ')
                    print('The ball follows you and SMASHES against the smaller tunnel area and gets lodged. There is now no getting out.')    
    
def main():

    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)

        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()
