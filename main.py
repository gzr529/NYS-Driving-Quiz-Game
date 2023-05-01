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
cordRX = -100
cordRY = -100

#Logic Storage
answerHistory = []

def scoreCalculator(answerHistory):
    score = 0
    for answer in answerHistory:
        if answer == 'Y':
            score += 1
        elif answer == 'N':
            score += 0
    globalScore = score*10
    return globalScore

questions = ("When did WW2 Start (Western Front)?",
             "Where is Albania Located?",
             "What is the (Objectively) Most Popular Anime?",
             "How long is an Olympic swimming pool (in meters)?",
             "What is the name of the biggest technology company in South Korea?",
             "What is the most consumed manufactured drink in the world?",
             "What is the term for the psychological phenomenon in which people tend to remember the first and last items on a list better than those in the middle?",
             "When did the USSR Collapse?",
             "Which of these counties is located in the Caucasus Mountains?",
             "How many died in the Challenger Explosion?",
             "What is the Hottest Planet in the Solar System?",
             "What's the smallest country in the world?",)
answers = (("1939", "1941", "1947", "1944"),
           ("Balkans", "Baltics", "South East Asia", "Siberia"),
           ("One Piece", "Naruto", "Attack on Titan", "Fullmetal Alchemist: Brotherhood"),
           ("30", "25", "50", "100"),
           ("LG", "Samsung", "Hyundai", "SK Hynix"),
           ("Coca-Cola", "Tea", "Coffee", "Pepsi"),
           ("Serial Position Effect", "List Effect",
            "Memory Bias", "Primacy-Recency Effect"),
           ("1985", "1991", "1989", "1990"),
           ("Azerbaijan", "Bulgaria", "Nepal", "Vietnam"),
           ("5", "7", "10", "12"),
           ("Mercury", "Venus", "Earth", "Mars"),
           ("Vatican City", "Monaco", "Nauru", "San Marino"),)
correctAnswers = [1, 1, 4, 3, 2, 2, 1, 2, 1, 2, 2, 1]
void = []
i = 0

#Randomizer
def Randomizer():
    while True:
        Randomizer.x = random.randint(0, len(questions) - 1)
        if Randomizer.x not in void:
            void.append(Randomizer.x)
            break
    void.sort()

Randomizer()

#Colors/Font
numFont = pygame.font.Font('media/font/Montserrat-Medium.ttf', 15)
titleFont = pygame.font.Font('media/font/Montserrat-Bold.ttf', 18)
questionsFont = pygame.font.Font('media/font/PathwayI.ttf', 30)
questionsPreFont = pygame.font.Font('media/font/PathwayN.ttf', 18)
greyClr = (40,40,40)
redClr = (222, 80, 80)
whiteClr = (255,255,255)
blackClr = (0,0,0)

def controls():
    global cordRX
    global cordRY
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        cordRX = 40
        cordRY = 380
        controls.answerGiven = 1
        pygame.display.update()
    elif keys[pygame.K_2]:
        cordRX = 40
        cordRY = 470
        controls.answerGiven = 2
    elif keys[pygame.K_3]:
        cordRX = 40
        cordRY = 560
        controls.answerGiven = 3
    elif keys[pygame.K_4]:
        cordRX = 40
        cordRY = 650
        controls.answerGiven = 4
    elif keys[pygame.K_c]:
        print("Confirmed")
        cordRX = -100
        cordRY = -100
        # print("--------",len(void))
        # print("--------",len(questions))
        
        # Checks the remaining questions (and if the game can continue)
        if len(void) == 11 and len(answerHistory):
            print("No more questions left. Game over.")
        elif controls.answerGiven != "":
            if controls.answerGiven == correctAnswers[Randomizer.x]:
                answerHistory.append("Y")
                Randomizer()
            elif controls.answerGiven == "":    
                print("NULL")
            else:
                answerHistory.append("N")
                Randomizer()
            controls.answerGiven = ""

#Start Screen / Will Become In Valid Once Confirmed in While Loop
screen.fill(greyClr)
pygame.display.update()

#Wraps Text to make more Readable
def wrap_text(text, font, max_width):
    words = text.split(" ")
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        test_width, _ = font.size(test_line)

        if test_width < max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    lines.append(current_line.strip())
    return lines


#Text Handler
def text():
    y_positions = [371, 461, 551, 641]

    # Multiple Choice Numbers
    for i in range(1, 5):
        numText = numFont.render(str(i), True, whiteClr)
        screen.blit(numText, (40, y_positions[i - 1]))

    # Multiple Choice Answers
    for i in range(1, 5):
        ansText = numFont.render(answers[Randomizer.x][i - 1], True, whiteClr)
        screen.blit(ansText, (70, y_positions[i - 1]))

    # Text for Info
    titleText = titleFont.render(
        'Use NUM Keys to Select then Press "C" to Confirm Answer', True, whiteClr)
    screen.blit(titleText, (130, 314))

    # Wrapped Question Text
    question_lines = wrap_text(
        questions[Randomizer.x], questionsFont, xLength - 150)
    for i, line in enumerate(question_lines):
        titleText = questionsFont.render(line, True, whiteClr)
        screen.blit(titleText, (130, 100 + i * 40))

    titleText = questionsPreFont.render(
        "Question " + str(len(void)), True, whiteClr)
    screen.blit(titleText, (130, 80))
    titleText = questionsPreFont.render(str(answerHistory), True, whiteClr)
    screen.blit(titleText, (130, 290))
    titleText = titleFont.render("Answer History Below:", True, whiteClr)
    screen.blit(titleText, (130, 270))

    
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

controls.answerGiven = ""    

#Game Over Text/Screen
def gameOver():
    screen.fill((0, 0, 0))  # Clear the screen by filling it with a black color

    gameOverFont = pygame.font.Font('media/font/Montserrat-Bold.ttf', 50)
    gameOverText = gameOverFont.render("Game Over | Score : "+str(scoreCalculator(answerHistory))+"%", True, whiteClr)
    gameoverRect = gameOverText.get_rect(center=(xLength // 2, yLength // 2))


    screen.blit(gameOverText, gameoverRect)
    pygame.display.update()

      
def main():
    clock = pygame.time.Clock()
    run = True
    gameOverCheck = False 

    while run:
        clock.tick(8)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        controls()

        if gameOverCheck:
            gameOver()
        else:
            draw()

        #Will End Game on Question 11 (When Question 10 Has Been Answered)
        if len(void) == 11:
            gameOverCheck = True

    
#Makes sure that this file is ran directly
if __name__ == "__main__":
    main()