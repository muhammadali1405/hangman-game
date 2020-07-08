import pygame


#setup
pygame.init()
WIDTH, HEIGHT =800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

#Images

images = []
for i in range(7):
	image = pygame.image.load("img/hangman"+str(i)+".png")
	images.append(image)


#game variables
hangman_status = 0

#color
WHITE = (255,255,255)


#loop


FPS = 60
clock = pygame.time.Clock()
run = True

while run:
	clock.tick(FPS)									#telling the fps

	win.fill(WHITE)             
	win.blit(images[hangman_status],(150,100))  	#displays current hangman
	pygame.display.update()                     	#it is essential to update after every addon..we must refresh manually   

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False								#if quit button selected loop closes
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()			#gets the pointer location when clicked
			print(pos)



pygame.quit()