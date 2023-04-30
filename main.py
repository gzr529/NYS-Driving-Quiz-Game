import random
import pygame
import os 

#Initalize
pygame.init()
xLength, yLength = 800, 700
screen = pygame.display.set_mode((xLength, yLength))
pygame.display.set_caption("NYS Drivers Quiz")

#Assets
button = pygame.image.load("media/img/button.png")

#button = pygame.transform.scale(buttonRaw, (250, 90))
cordRX = -100
cordRY = -100

#Logic
answerHistory = []

# list1 = [1,1,1,1]
# list2 = ["How fast do you drive",
#          "What color is stop sign",
#          "Break pedal on left",
#          "Kill",
#          "Your",
#          "Self",
#          "Smile"]
# list4 = ["Qa","Qb","Qc","Qd","Qe","Qf","Qg"]
# list3 = []
    
# def Randomizer(): 
#     x = random.randint(0,len(list2)-1)
#     if x in list3:
#         list1.sort()
#         #print("This # Has Been Used!", list2[x])  
#     else:
#         list3.append(x)
#         list3.sort()
        
# while True:
#     Randomizer()
#     if len(list2) == len(list3):
#         print("No More Questions!")
#         break   


#Colors/Font
numFont = pygame.font.Font('media/font/Montserrat-Medium.ttf', 15)
titleFont = pygame.font.Font('media/font/Montserrat-Bold.ttf', 18)
greyClr = (40,40,40)
redClr = (222, 80, 80)
whiteClr = (255,255,255)

def controls():
    global cordRX
    global cordRY

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        print("1")
        cordRX = 40
        cordRY = 380
        controls.answerGiven = 1
        pygame.display.update()
    elif keys[pygame.K_2]:
        print("2")
        cordRX = 40
        cordRY = 470
        controls.answerGiven = 2
    elif keys[pygame.K_3]:
        print("3")
        cordRX = 40
        cordRY = 560
        controls.answerGiven = 3
    elif keys[pygame.K_4]:
        print("4")
        cordRX = 40
        cordRY = 650
        controls.answerGiven = 4
    elif keys[pygame.K_c]:
        print("Confirmed")
        cordRX = -100
        cordRY = -100
        if controls.answerGiven == 3:
            print("YAYAYA!")
            answerHistory.append("Y")
        else:
            answerHistory.append("N")



#Start Screen / Will Become In Valid Once Confirmed in While Loop
screen.fill(greyClr)
pygame.display.update()

#Text Handler
def text():
    numText = numFont.render(('1'), True, whiteClr)
    screen.blit(numText, (40, 371))
    numText = numFont.render('2', True, whiteClr)
    screen.blit(numText, (40, 461))
    numText = numFont.render('3', True, whiteClr)
    screen.blit(numText, (40, 551))
    numText = numFont.render('4', True, whiteClr)
    screen.blit(numText, (40, 641))
    titleText = titleFont.render('Use NUM Keys to Select then Press "C" to Confrim Answer', True, whiteClr)
    screen.blit(titleText, (130, 314))
    titleText = titleFont.render(str(answerHistory), True, whiteClr)
    screen.blit(titleText, (130, 250))
    
#Draws Window Colordef drawScreen():
def draw():
    screen.fill(greyClr)
    screen.blit(button, (0,600))
    screen.blit(button, (0,510))
    screen.blit(button, (0,420))
    screen.blit(button, (0,330))
    pygame.draw.circle(screen, whiteClr, (cordRX, cordRY), 10)
    text()
    pygame.display.update()

            
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(15)  # Ensures 60FPS and 60 Updates a Second (Quiz Game Doesnt Need High FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        controls()
        draw()

    pygame.quit()
    
    
#Makes sure that this file is ran directly
if __name__ == "__main__":
    main()