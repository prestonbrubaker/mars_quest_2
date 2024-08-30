import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the display (we don't actually need a display for this task)
screen = pygame.display.set_mode((400, 300))


player_id = 0
num_players = 3


player_id_old = player_id

# Set the initial state of the program
running = True

# Start the main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            player_id_old = player_id
            if event.key == pygame.K_RIGHT:
                output = 0
            elif event.key == pygame.K_UP:
                output = 3
            elif event.key == pygame.K_LEFT:
                output = 2
            elif event.key == pygame.K_DOWN:
                output = 1
            elif event.key == pygame.K_z:
                output = 4
            elif event.key == pygame.K_x:
                output = 5
            elif event.key == pygame.K_c:
                output = 6
            elif event.key == pygame.K_v:
                output = 7
            elif event.key == pygame.K_a:
                output = 8
            elif event.key == pygame.K_s:
                output = 9
            elif event.key == pygame.K_d:
                output = 10
            elif event.key == pygame.K_f:
                output = 11
            elif event.key == pygame.K_p:
                output = 12
                player_id += 1
                if player_id > num_players - 1:
                    player_id = 0
            elif event.key == pygame.K_q:
                output = 13
            elif event.key == pygame.K_w:
                output = 14
            elif event.key == pygame.K_e:
                output = 15
            elif event.key == pygame.K_r:
                output = 16
            elif event.key == pygame.K_i:
                output = 17
            elif event.key == pygame.K_o:
                output = 18
            elif event.key == pygame.K_l:
                output = 19
            elif event.key == pygame.K_k:
                output = 20
            elif event.key == pygame.K_j:
                output = 21
            elif event.key == pygame.K_h:
                output = 22
            elif event.key == pygame.K_m:
                output = 23



            else:
                continue  # Ignore other keys

            output += player_id_old * 50

            player_id_old = player_id

            # Get the current epoch time
            epoch_time = int(time.time() * 1000)

            # Generate the filename using the epoch time
            filename = f"command_{epoch_time}.txt"

            # Write the output to the file
            with open(filename, "w") as file:
                file.write(str(output))

            print(f"Key pressed: {output} - Written to {filename}")

# Quit Pygame
pygame.quit()
