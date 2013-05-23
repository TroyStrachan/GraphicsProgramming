
import time

def displayIntro():
    print ('You are on a planet full of dragons. In front of you,')
    print ('you see two caves. In one cave, the dragon is friendly')
    print ('and will share his treasure with you. The other dragon')
    print ('is greedy and hungry, and will eat you on sight.')
    print

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print ('Which cave will you go into? (1 or 2)')
        cave = raw_input()
    return cave

def checkCave(chosenCave):
    print ('You approach the cave...')
    time.sleep(.5)
    print ('It is dark and spooky...')
    time.sleep(.5)
    print
    time.sleep(.5)

    

    if chosenCave == "1": # first decision level
        print ('You are staring down a long tunnel, at the end of it there is another fork. Do you want to go left or right?')
        nextCave = raw_input()
        if nextCave == "left":#second decision level
            print('You start hearing noises coming from deep within the cave. You begin to follow it. It is beginning to sound like a monkey. Do you want to follow it? Yes/No?')
            nextCave = raw_input()
            if nextCave =="Yes" or nextCave == "y": # 3rd decision 1
                print('You encounter a viral monkey who bit you... you have 45 seconds before you are terminally infected... Good Luck')
            else: #3rd decision 2
                print('You see a light, but it is coming at you really fast. Oh wait that is ... Fire')
        else: #second decision level
            print('You find your way out of the cave')
            time.sleep(1)
            print('Or so you thought. There is a warm breeze coming from the left tunnel... do you chance it? Left or Right?')
            nextCave = raw_input()
            if nextCave == "left" or nextCave =="l": #3rd decision  3
                print ('Following the breeze may have been a bad idea... here comes a lava flow. Nice knowing you bud')
            else: #3rd decision 4
                print ("You suddenly hear a voice - I am sorry to bother you sir but do you have a light. You turn and see a dragon who smirks then slashes you into 3 even pieces with his sharp claws")     
            
    elif chosenCave == "2": # first decision level
        print ('A dragon appears and points down to another tunnel telling you to be careful and to choose your path wisely. Go left or right?')
        nextCave = raw_input()
        if nextCave == "left": #second decision level
            print('You encounter a cute monkey, his foot is stuck under a fallen rock. You help him and for helping him...')
            time.sleep(3)
            print('he bites your hand and rips off 3 of your fingers! Then picks up the rock and crushes your head with it')
            time.sleep(2)
            print('You wake up weary and blurry eyed.')
            time.sleep(1)
            print('You can barely make out the evil monkey who is hovering a few feet from you holding out his hand as though he means to help.')
            print('Do you grab it, Yes/No?')
            nextCave = raw_input()
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
            else: #3rd decision 6
                print('The monkey looks at you feeling scorned and disrespected. He picks up the rock again and goes at you, well, like a spider monkey')
        else: #first decision level
            print('You step on a loose stone, you hear a thud then it sounds like something is rolling. You turn around and you see a ball like the one of Indiana Jones...')
            time.sleep(2)
            print('You notice a split in the tunnel coming up, go left or right?')#second decision level
            nextCave = raw_input()
            if nextCave == "left":
                print("The ball just misses you as you dive into the tunnel on the left, only to find out you found a nest full of king cobra snakes and you woke them up. They aren't very happy")
            else:
                print("You aren't out running the giant stone ball... dive to side or keep running? Dive or Run")
                nextCave = raw_input()
                if nextCave == "Dive": #3rd decision level 7
                    print ('I always thought you were a bit chunky, interesting form of diet though.')
                else: #3rd decision 8
                    print('You keep running, you see a spot where the tunnel narrows and dive into it. ')
                    print('The ball follows you and SMASHES against the smaller tunnel area and gets lodged. There is now no getting out.')
                
    elif chosenCave != "1" or chosenCave != "2": 
        print ('Before you have a chance to decide a mean dragon comes out of one of the caves and eats you. That is what you get for hesitating.')

def main():

    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)

        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()
