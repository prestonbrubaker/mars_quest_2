import pygame
import random
import time
import ast
import os
import glob
import copy
import math
import shutil

pygame.init()

planets = [[0, 0.4, 0, 0 - 0.1 * 0.1 * 0.02 / 5 + 0.3 * 0.1 * 0.003 / 5, 0, 0, 0.01, 50 / 3, [255, 195, 11]],
           [0.5 - 0.1 / 2 * 3 ** 0.5, 0.505, 0, 0 - 0.1 * 0.1 * 0.02 / 5 + 0.3 * 0.1 * 0.003 / 5, 0, 0, 0.01, 50 / 3, [255, 195, 11]],
           [0.5 + 0.1 / 2 * 3 ** 0.5 + 0.0001, 0.505, 0, 0 - 0.1 * 0.1 * 0.02 / 5 + 0.3 * 0.1 * 0.003 / 5, 0, 0, 0.01, 50 / 3, [255, 195, 11]],
           [0.5 + 0.1 / 2 * 3 ** 0.5, 0.205, 0, 0 - 0.1 * 0.1 * 0.02 / 5 + 0.3 * 0.1 * 0.003 / 5, 0, 0, 0.01, 50 / 3, [255, 195, 11]],
           [0.1 + 0.1 / 2 * 3 ** 0.5, 0.445, 0, 0 - 0.1 * 0.1 * 0.02 / 5 + 0.3 * 0.1 * 0.003 / 5, 0, 0, 0.01, 50 / 3, [255, 195, 11]],
           [0.5 + 0.1 / 2 * 3 ** 0.5, 0.435, 0, 0 - 0.1 * 0.1 * 0.02 / 5 + 0.3 * 0.1 * 0.003 / 5, 0, 0, 0.01, 50 / 3, [255, 195, 11]],
           [0.6 + 0.1 / 2 * 3 ** 0.5, 0.325, 0, 0 - 0.1 * 0.1 * 0.02 / 5 + 0.3 * 0.1 * 0.003 / 5, 0, 0, 0.01, 50 / 3, [255, 195, 11]],
           [0.5 + 0.1 / 2 * 3 ** 0.5, 0.415535, 0, 0 - 0.1 * 0.1 * 0.02 / 5 + 0.3 * 0.1 * 0.003 / 5, 0, 0, 0.01, 50 / 3, [255, 195, 11]],
           [0.5 + 0.1 / 2 * 3 ** 0.5, 0.713355, 0, 0 - 0.1 * 0.1 * 0.02 / 5 + 0.3 * 0.1 * 0.003 / 5, 0, 0, 0.01, 50 / 3, [255, 195, 11]],
           [0.7 + 0.1 / 2 * 3 ** 0.5, 0.415575, 0, 0 - 0.1 * 0.1 * 0.02 / 5 + 0.3 * 0.1 * 0.003 / 5, 0, 0, 0.01, 50 / 3, [255, 195, 11]],
           [0.3 + 0.1 / 2 * 3 ** 0.5, 0.9153523, 0, 0 - 0.1 * 0.1 * 0.02 / 5 + 0.3 * 0.1 * 0.003 / 5, 0, 0, 0.01, 50 / 3, [255, 195, 11]],
           [0.5 + 0.1 / 2 * 3 ** 0.5, 0.415674, 0, 0 - 0.1 * 0.1 * 0.02 / 5 + 0.3 * 0.1 * 0.003 / 5, 0, 0, 0.01, 50 / 3, [255, 195, 11]],
           [0.5 + 0.1 / 2 * 3 ** 0.5, 0.315232, 0, 0 - 0.1 * 0.1 * 0.02 / 5 + 0.3 * 0.1 * 0.003 / 5, 0, 0, 0.01, 50 / 3, [255, 195, 11]],
           [0.9 + 0.1 / 2 * 3 ** 0.5, 0.41565, 0, 0 - 0.1 * 0.1 * 0.02 / 5 + 0.3 * 0.1 * 0.003 / 5, 0, 0, 0.01, 50 / 3, [255, 195, 11]],
           [0.5 + 0.1 / 2 * 3 ** 0.5, 0.41523, 0, 0 - 0.1 * 0.1 * 0.02 / 5 + 0.3 * 0.1 * 0.003 / 5, 0, 0, 0.01, 50 / 3, [255, 195, 11]],
           [0.5 + 0.1 / 2 * 3 ** 0.5, 0.705, 0, 0 - 0.1 * 0.1 * 0.02 / 5 + 0.3 * 0.1 * 0.003 / 5, 0, 0, 0.01, 50 / 3, [255, 195, 11]]]

planets = []



# Toggle Options
is_master = True
can_reproduce = True
is_observation_mode = True
immobilize_player = False
show_minimap = True
can_die = True
load_players = True
# Environment Variables
player_make_c = 0.1
scale = 7
minimap_scale = 0.7
player_id = 0
sensitivity = 5
initial_agent_count = 1000
death_age = 1000 # Age when agent first has chance of random death
random_death_c = .1  # Chance of random death each iteration once at death age
metabolism_rate = 2
color_mutation_chance = 1
mutation_c = 0.35
min_reproduction_age = 400
wall_death_c = 1


players = []


gC = 1.8  # Gravitational constant
dt = 0.00001  # Change in time per iteration

p_mass = 0.001  # Player mass multiplier
p_mass_c = 10   # number of food units worth of mass to be added as a constant to player

drag = 0.01

fuel_cost = .000000  # multiplier for the cost for agent to thrust, to be scaled by dt


# Statistical Counters
births_by_sex = 0
births_by_not_sex = 0
reproduction_eff = 0.9
max_food = 500

wall_collisions = 0
sun_collisions = 0
old_age_deaths = 0
starvation_deaths = 0

total_food = 0
save_player_c = 600

corner_int = 600
corner = 0
corner_f = 0.05

itC = 0
el_time = 0

food_add_amount = 400
food_cycles = 20

grid_c = 30
food_grid = []
info_grid = []
exploded_grid = []


action_index_to_text = ["Rotate clockwise",
                        "Thrust backwards",
                        "Rotate counterclockwise",
                        "Thrust forwards",
                        "DECREASE sensitivity",
                        "decrease sensitivity",
                        "increase sensitivity",
                        "INCREASE sensitivity",
                        "DECREASE zoom",
                        "decrease zoom",
                        "increase zoom",
                        "INCREASE zoom",
                        "Increment player id",
                        "DECREASE time step",
                        "decrease time step",
                        "increase time step",
                        "INCREASE time step",
                        "Toggle minimap",
                        "Decrement player id",
                        "Toggle whether agents can die",
                        "Toggle whether agents can reproduce",
                        "Toggle observation mode",
                        "Commit die",
                        "Toggle immobilize mode",
                        "EXPLODE",
                        "Agent has chosen to rest"  # -1 used as index output by neural network to indicate no action
                        ]




time_ref = time.time()

window_width = 2000
width_f = 1.75

window = pygame.display.set_mode((int(window_width * width_f), window_width))


font_size = 18
text_color = (50, 255, 50)
font_path = os.path.join('mars_quest.ttf')
font = pygame.font.Font(font_path, font_size)
newline_spacing = 25


planets_file_path = 'planets.txt'
players_file_path = 'players.txt'




window.fill((50, 50, 50))



def create_players(number_to_make):
    for i in range(number_to_make):
        nodes = []
        for j in range(49):
            nodes.append(0)
        weights = []
        for j in range(646): # 10 reserved for other used, rest used for neural network
            weight = random.gauss(0, .3)
            if weight > 2:
                weight = 2
            if weight < -2:
                weight = 2
            weights.append(weight)

        players.append(
           [random.uniform(0, 1),
            random.uniform(0, 1),
            random.gauss(0, 1),
            random.gauss(0, 1),
            scale,
            sensitivity,
            0,
            0,
            -1,
            100,
            [[copy.deepcopy(nodes), copy.deepcopy(weights)], [copy.deepcopy(nodes), copy.deepcopy(weights)]],
            random.uniform(0, math.pi * 2),
            0,
            [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)],
            random.choice([True, False])
            ])


def initialize_food():
    food_out = []
    for y in range(grid_c):
        temp = []
        for x in range(grid_c):
            food = random.gauss(200, 1)
            if food < 0:
                food = 0
            temp.append(food)
        food_out.append(temp)
    return food_out


def update_info_grid():
    global info_grid
    info_grid = []
    for y in range(grid_c):
        temp = []
        for x in range(grid_c):
            temp.append([])
        info_grid.append(temp)

    for i in range(len(players)):
        x = players[i][0]
        y = players[i][1]
        if x < 0:
            x = 0
        if x >= 1:
            x = 1 - 1e-9
        if y < 0:
            y = 0
        if y >= 1:
            y = 1 - 1e-9
        x_index = int(x * grid_c)
        y_index = int(y * grid_c)
        info_grid[x_index][y_index].append(i)

def clear_exploded_grid():
    global exploded_list
    exploded_list = []
    for y in range(grid_c):
        temp = []
        for x in range(grid_c):
            temp.append(False)
        exploded_list.append(temp)


def add_food():
    global corner
    global itC
    global corner_int
    for i in range(food_cycles):
        if corner == 3:
            x = random.uniform(0.5 + corner_f, 1)
            y = random.uniform(0, 0.5 - corner_f)
        if corner == 2:
            x = random.uniform(0, 0.5 - corner_f)
            y = random.uniform(0, 0.5 - corner_f)
        if corner == 1:
            x = random.uniform(0, 0.5 - corner_f)
            y = random.uniform(0.5 + corner_f, 1)
        if corner == 0:
            x = random.uniform(0.5 + corner_f, 1)
            y = random.uniform(0.5 + corner_f, 1)
        x_ind = int(x * grid_c)
        y_ind = int(y * grid_c)
        dist = ((x - 0.5)**2 + (y - 0.5)**2)**0.5
        #if dist > 0.36 or dist < 0.3 or (y > 0.475 and y < 0.525) or (x > 0.475 and x < 0.525):
        food_grid[x_ind][y_ind] += random.uniform(0, food_add_amount)
        x = int(random.randint(0, grid_c - 1))
        y = random.randint(0, grid_c - 1)
        food_grid[x][y] *= .75

def find_total_food():
    global total_food
    total_food = 0
    for y in range(grid_c):
        for x in range(grid_c):
            total_food += food_grid[x][y]



def run_brain(index_in):
    decision_list = []
    for k in range(2):
        # Input layer
        players[index_in][10][k][0][0] = players[index_in][0]  # x-pos
        players[index_in][10][k][0][1] = players[index_in][1]  # y-pos

        players[index_in][10][k][0][2] = sigmoid(players[index_in][2])  # vx
        players[index_in][10][k][0][3] = sigmoid(players[index_in][3])  # vy

        players[index_in][10][k][0][4] = sigmoid(players[index_in][5])  # sensitivity

        players[index_in][10][k][0][5] = sigmoid(players[index_in][6])  # fx
        players[index_in][10][k][0][6] = sigmoid(players[index_in][7])  # fy

        players[index_in][10][k][0][7] = sigmoid(players[index_in][9] / 100)  # food

        players[index_in][10][k][0][8] = sigmoid(math.cos(players[index_in][11]))  # x-component of angle
        players[index_in][10][k][0][9] = sigmoid(math.sin(players[index_in][11]))  # y-component of angle

        players[index_in][10][k][0][10] = 1  # bias

        players[index_in][10][k][0][11] = players[index_in][10][k][0][34]  # memory

        players[index_in][10][k][0][12] = players[index_in][10][k][0][35]  # memory 2

        players[index_in][10][k][0][13] = random.uniform(0, 1)  # random

        players[index_in][10][k][0][14] = sigmoid(random.gauss(0, 0.5))  # random

        players[index_in][10][k][0][15] = random.randint(0, 1)  # random

        if players[index_in][10][k][0][16] == 0:
            players[index_in][10][k][0][16] = 1
        else:
            players[index_in][10][k][0][16] = 0


        x = players[index_in][0]
        y = players[index_in][1]
        if x < 0:
            x = 0
        if x >= 1:
            x = 1 - 1e-9
        if y < 0:
            y = 0
        if y >= 1:
            y = 1 - 1e-9


        x_index = int(x * grid_c)
        y_index = int(y * grid_c)
        if len(info_grid[x_index][y_index]) > 1:
            dists = []
            dx_and_dy = []
            index_list = []
            for i in range(len(info_grid[x_index][y_index])):
                if info_grid[x_index][y_index][i] == index_in:
                    continue
                dx = players[info_grid[x_index][y_index][i]][0] - x
                dy = players[info_grid[x_index][y_index][i]][1] - y
                dist = (dx ** 2 + dy ** 2) ** 0.5
                dists.append(dist)
                dx_and_dy.append([dx, dy])
                index_list.append(info_grid[x_index][y_index][i])
            index_cl = dists.index(min(dists))
            players[index_in][10][k][0][17] = sigmoid(dx_and_dy[index_cl][0] * grid_c)
            players[index_in][10][k][0][18] = sigmoid(dx_and_dy[index_cl][1] * grid_c)
            players[index_in][10][k][0][19] = sigmoid(len(dists))
            players[index_in][10][k][0][21] = players[index_list[index_cl]][10][k][0][36]
            players[index_in][10][k][0][22] = players[index_list[index_cl]][10][k][0][37]


        else:
            players[index_in][10][k][0][17] = 0
            players[index_in][10][k][0][18] = 0
            players[index_in][10][k][0][19] = 0
            players[index_in][10][k][0][21] = 0
            players[index_in][10][k][0][22] = 0


        players[index_in][10][k][0][20] = sigmoid(food_grid[x_index][y_index] / 100)



        weight_index = 0

        # input to hidden: Setting nodes 23-27 using input nodes 0-22

        for a in range(5):
            sum = 0
            for b in range(23):
                sum += players[index_in][10][k][0][b] * players[index_in][10][k][1][weight_index]
                weight_index += 1
            players[index_in][10][k][0][a + 23] = relu(sum)

        players[index_in][10][k][0][28] = 1  # bias


        # hidden 1 to hidden 2: setting nodes 29-33 using nodes 23-28

        for a in range(5):
            sum = 0
            for b in range(6):
                sum += players[index_in][10][k][0][b + 23] * players[index_in][10][k][1][weight_index]
                weight_index += 1
            players[index_in][10][k][0][a + 29] = relu(sum)



        # hidden + input to output: setting nodes 34 to 47 using nodes nodes 0-33

        for a in range(14):
            sum = 0
            for b in range(34):
                sum += players[index_in][10][k][0][b] * players[index_in][10][k][1][weight_index]
                weight_index += 1
            players[index_in][10][k][0][a + 34] = sigmoid(sum)

        # 34 & 35 Are alloted to nodes 11 & 12 (memory)

        # 36 & 37 reserved as output to communicate out to other agents

        # 38 is willingness to reproduce asexually

        # 39 is willingness to reproduce sexually

        # 40 to 45 reserved for actions

        # 46 reserved for thrust factor

        # 47 reserved for fuel transfer ratio

        decision_temp_list = []
        for i in range(6):
            decision_temp_list.append(players[index_in][10][k][0][i + 40])
        decision_list.append(decision_temp_list)
    if players[index_in][14]:
        weight_from_last = -2
    else:
        weight_from_last = -1
    decision_list_cond = []
    for i in range(len(decision_list[0])):
        decision_list_cond.append( decision_list[0][i] * sigmoid(players[index_in][10][0][1][weight_from_last]) + decision_list[1][i] * sigmoid(players[index_in][10][1][1][weight_from_last]) )


    decision = decision_list_cond.index(max(decision_list_cond))

    if decision == 4:  # Rest
        decision = -1
    if decision == 5:  # Explode
        decision = 24
    return decision



def relu(x_in):
    if x_in > 0:
        return x_in
    else:
        return 0



def sigmoid(x_in):
    if x_in > 100:
        return 1
    elif x_in < -100:
        return 0
    else:
        return 1 / (1 + math.exp(-1 * x_in))





def iterate_players():
    global player_id
    global old_age_deaths
    global starvation_deaths
    for i in range(len(players)):
        # Eat Food
        x_player = int(players[i][0] * grid_c)
        if x_player > grid_c - 1:
            x_player = grid_c - 1
        if x_player < 0:
            x_player = 0

        y_player = int(players[i][1] * grid_c)
        if y_player > grid_c - 1:
            y_player = grid_c - 1
        if y_player < 0:
            y_player = 0

        food_transfer = food_grid[x_player][y_player] * 0.01
        food_grid[x_player][y_player] -= food_transfer
        players[i][9] += food_transfer
        if players[i][9] > max_food:
            players[i][9] = max_food
        # Metabolism
        players[i][9] -= metabolism_rate
        if players[i][9] < 0:
            players[i][9] = 0
        x = players[i][0]
        y = players[i][1]
        dist = ((x - 0.5) ** 2 + (y - 0.5) ** 2) ** 0.5
        # Attempt Reproduction
        if (
            players[i][9] > 200 and
            players[i][10][0][0][38] > .5 and
            dist > 0.1
            and can_reproduce
            and (i != player_id
            or i == player_id
            and is_observation_mode)
            and players[i][12] >= min_reproduction_age):
            if players[i][10][0][0][38] > 0.75:
                duplicate_player(i)
            else:
                sexually_duplicate_player(i)

    for i in range(len(players) - 1, -1, -1):
        players[i][12] += 1
        if players[i][9] <= 0:
            death_note.append(i)
            starvation_deaths += 1
        elif random.uniform(0, 1) < random_death_c and players[i][12] > death_age:
            death_note.append(i)
            old_age_deaths += 1

        player_died = False
        if (i in death_note and len(players) > 10 and (i != player_id or i == player_id and can_die)):
            if i < player_id:
                player_id -= 1
            if i == player_id:
                player_died = True

            x_index = int(players[i][0] * grid_c)
            y_index = int(players[i][1] * grid_c)
            if x_index > grid_c - 1:
                x_index = grid_c - 1
            if y_index > grid_c - 1:
                y_index = grid_c - 1
            if x_index < 0:
                x_index = 0
            if y_index < 0:
                y_index = 0
            food_grid[x_index][y_index] += players[i][9]
            players.pop(i)
        if player_died:
            player_id = len(players) - 2



def sexually_duplicate_player(index_in):
    global player_id
    global births_by_sex
    x = players[index_in][0]
    y = players[index_in][1]
    if x < 0:
        x = 0
    if x >= 1:
        x = 1 - 1e-9
    if y < 0:
        y = 0
    if y >= 1:
        y = 1 - 1e-9


    x_index = int(x * grid_c)
    y_index = int(y * grid_c)

    if len(info_grid[x_index][y_index]) > 1:
        dists = []
        dx_and_dy = []
        index_list = []
        for i in range(len(info_grid[x_index][y_index])):
            if info_grid[x_index][y_index][i] == index_in:
                continue
            dx = players[info_grid[x_index][y_index][i]][0]
            dy = players[info_grid[x_index][y_index][i]][1]
            dist = (dx ** 2 + dy ** 2) ** 0.5
            dists.append(dist)
            dx_and_dy.append([dx, dy])
            index_list.append(info_grid[x_index][y_index][i])
        index_cl = dists.index(min(dists))
        mate_index = index_list[index_cl]
        if players[mate_index][10][0][0][39] > 0.5 and players[mate_index][9] > 200:
            births_by_sex += 1

            food_transfered_father = players[index_in][9] * players[index_in][10][0][0][47] * 0.2
            players[index_in][9] -= food_transfered_father
            food_transfered_mother = players[mate_index][9] * players[index_in][10][0][0][47] * 0.8
            players[mate_index][9] -= food_transfered_mother

            players[index_in][9] -= food_transfered_father
            players[mate_index][9] -= food_transfered_mother
            player_list = copy.deepcopy(players[mate_index])
            player_list[0] += random.uniform(-0.001, 0.001)
            player_list[1] += random.uniform(-0.001, 0.001)
            player_list[2] += random.uniform(-0.001, 0.001)
            player_list[3] += random.uniform(-0.001, 0.001)
            player_list[8] = -1
            player_list[9] = (food_transfered_father + food_transfered_mother) * reproduction_eff
            player_list[12] = 0
            player_list[14] = random.choice([False, True])


            if random.uniform(0, 1) < 0.5:
                player_list[10][0][1] = copy.deepcopy(players[index_in][10][0][1])
            else:
                player_list[10][1][1] = copy.deepcopy(players[index_in][10][1][1])

            if random.uniform(0, 1) < sigmoid(players[index_in][10][0][1][-3] - 1):  # Chance of mutation
                random_magnitude = random.randint(-14, 4)
                brain_index = random.randint(0, 1)
                mutated = False
                while random.uniform(0, 1) < sigmoid(players[index_in][10][0][1][-4]) or not mutated:
                    mutated = True
                    random_index = random.randint(0, len(player_list[10][brain_index][1]) - 1)
                    player_list[10][brain_index][1][random_index] += random.uniform(-1, 1) * 2 ** random_magnitude
                    if player_list[10][brain_index][1][random_index] > 10:
                        player_list[10][brain_index][1][random_index] = 10
                    if player_list[10][brain_index][1][random_index] < -10:
                        player_list[10][brain_index][1][random_index] = -10

            if random.uniform(0, 1) < color_mutation_chance:  # Chance of color mutation
                random_color_index = random.randint(0, 2)
                player_list[13][random_color_index] += random.randint(-10, 10)
                if player_list[13][random_color_index] < 0:
                    player_list[13][random_color_index] = 0
                elif player_list[13][random_color_index] > 255:
                    player_list[13][random_color_index] = 255

            players.append(player_list)



        else:
            return None


    else:
        return None





def duplicate_player(index_in):
    global births_by_not_sex
    births_by_not_sex += 1
    food_transfered = players[index_in][9] * players[index_in][10][0][0][47]
    players[index_in][9] -= food_transfered

    player_list = copy.deepcopy(players[index_in])
    player_list[0] += random.uniform(-0.001, 0.001)
    player_list[1] += random.uniform(-0.001, 0.001)
    player_list[2] += random.uniform(-0.001, 0.001)
    player_list[3] += random.uniform(-0.001, 0.001)
    player_list[8] = -1
    player_list[9] = food_transfered * reproduction_eff
    player_list[12] = 0
    player_list[14] = random.choice([False, True])


    if random.uniform(0, 1) < sigmoid(players[index_in][10][0][1][-3] - 1):  # Chance of mutation
        random_magnitude = random.randint(-14, 4)
        brain_index = random.randint(0, 1)
        mutated = False
        while random.uniform(0, 1) < sigmoid(players[index_in][10][0][1][-4]) or not mutated:
            mutated = True
            random_index = random.randint(0, len(player_list[10][brain_index][1]) - 1)
            player_list[10][brain_index][1][random_index] += random.uniform(-1, 1) * 2 ** random_magnitude
            if player_list[10][brain_index][1][random_index] > 10:
                player_list[10][brain_index][1][random_index] = 10
            if player_list[10][brain_index][1][random_index] < -10:
                player_list[10][brain_index][1][random_index] = -10

    if random.uniform(0, 1) < color_mutation_chance:  # Chance of color mutation
            random_color_index = random.randint(0, 2)
            player_list[13][random_color_index] += random.randint(-10, 10)
            if player_list[13][random_color_index] < 0:
                player_list[13][random_color_index] = 0
            elif player_list[13][random_color_index] > 255:
                player_list[13][random_color_index] = 255

    players.append(player_list)



def find_and_delete_most_recent_command():
    global is_master
    # Find all files in the current directory that match the pattern 'command_*.txt'
    command_files = glob.glob("command_*.txt")

    if not command_files:
        return None

    # Extract the epoch times from the filenames
    epochs = [int(f.split('_')[1].split('.')[0]) for f in command_files]

    # Find the file with the maximum epoch (most recent)
    most_recent_epoch = max(epochs)
    most_recent_file = f"command_{most_recent_epoch}.txt"
    try:
        # Read the contents of the most recent file
        with open(most_recent_file, 'r') as file:
            contents = file.read()

        if contents == "":
            return None
        # Convert the contents to an integer
        command_value = int(contents)
        if not is_master:
            os.rename(most_recent_file, "executed_" + most_recent_file)
        else:
            os.remove(most_recent_file)

    except:
        return None
    return command_value




def save_timelapse_frame():
    # Create the directory if it doesn't exist
    if not os.path.exists('timelapse_pics'):
        os.makedirs('timelapse_pics')

    # Construct the filename based on the itC variable
    filename = f'timelapse_pics/frame_{itC:08d}.png'

    # Save the current window surface to the file
    pygame.image.save(window, filename)



def clear_timelapse_pics_folder():
    folder = 'timelapse_pics'

    # Check if the folder exists
    if os.path.exists(folder):
        # Iterate over all the files and subfolders in the directory
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                # Check if it's a file or directory
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # remove the file or link
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # remove the directory
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
    else:
        print(f'The folder "{folder}" does not exist.')

    with open('statistics.txt', 'w') as file:
        file.write("")



def load_player_data():
    players_out = "f"
    with open('players.txt', "r") as file:
        contents = file.read()
        if len(contents) > 5:
            try:
                players_out = ast.literal_eval(contents)
            except:
                players_out = "f"
    return players_out


def load_planet_data():
    planets_out = "f"
    with open('planets.txt', "r") as file:
        contents = file.read()
        if len(contents) > 5:
            try:
                planets_out = ast.literal_eval(contents)
            except:
                planets_out = "f"
    return planets_out



def write_to_text_file():
    players_r = []
    for i in range(min(save_player_c, len(players))):
        players_r.append(players[i])


    with open('planets.txt', 'w') as file:
        file.write(str(planets))
    with open('players.txt', 'w') as file:
        file.write(str(players_r))

def write_stats():
    with open('statistics.txt', 'a') as file:
        stats = str(itC) + " " + str(len(players)) + " " + str(wall_collisions) + " " + str(sun_collisions) + " " + str(births_by_sex) + " " + str(births_by_not_sex) + " " + str(old_age_deaths) + " " + str(starvation_deaths) + " " + str(total_food)
        file.write(stats + "\n")



def run_physics():
    global sun_collisions
    global wall_collisions
    global starvation_deaths
    global old_age_deaths
    global immobilize_player
    for i in range(len(planets)):  # Physics for planets
        planets[i][4] = 0
        planets[i][5] = 0
        for j in range(len(planets)):
            if i == j:
                continue
            dx = planets[j][0] - planets[i][0]
            dy = planets[j][1] - planets[i][1]

            dist = (dx ** 2 + dy  ** 2) ** 0.5
            if dist < 0.000001:
                continue
            if dist < planets[j][6] + planets[i][6]:
                dist = -0 * (planets[j][6] + planets[i][6])
                #planets[i][2] -= 1000 * (planets[j][2] * planets[j][7] - planets[i][2] * planets[i][7]) / (abs(planets[j][2]) + abs(planets[i][2])) / (planets[i][7] + planets[j][7]) / planets[i][7] * dt
                #planets[i][3] -= 1000 * (planets[j][3] * planets[j][7] - planets[i][3] * planets[i][7]) / (abs(planets[j][3]) + abs(planets[i][3])) / (planets[i][7] + planets[j][7]) / planets[i][7] * dt
            else:
                fx = gC * planets[j][7] * planets[i][7] * dx / dist ** 3
                fy = gC * planets[j][7] * planets[i][7] * dy / dist ** 3

                planets[i][4] += fx
                planets[i][5] += fy

    for i in range(len(planets)):
        planets[i][2] += planets[i][4] / planets[i][7] * dt
        planets[i][3] += planets[i][5] / planets[i][7] * dt

        planets[i][0] += planets[i][2] * dt
        planets[i][1] += planets[i][3] * dt

        # Collision logic for planets
        if planets[i][0] > 1:
            planets[i][0] = 1
            planets[i][2] *= -1
        if planets[i][0] < 0:
            planets[i][0] = 0
            planets[i][2] *= -1
        if planets[i][1] > 1:
            planets[i][1] = 1
            planets[i][3] *= -1
        if planets[i][1] < 0:
            planets[i][1] = 0
            planets[i][3] *= -1


    for i in range(len(players)):  # Physics for players
        players[i][6] = 0
        players[i][7] = 0

        players[i][2] *= 1 - drag # * dt
        players[i][3] *= 1 - drag # * dt
        if i != player_id or not immobilize_player:
            players[i][0] += players[i][2] * dt
            players[i][1] += players[i][3] * dt
        hit_wall = False
        # Collision logic for players
        if players[i][0] > 1:
            players[i][0] = 1
            players[i][2] *= -1
            hit_wall = True
        if players[i][0] < 0:
            players[i][0] = 0
            players[i][2] *= -1
            hit_wall = True
        if players[i][1] > 1:
            players[i][1] = 1
            players[i][3] *= -1
            hit_wall = True
        if players[i][1] < 0:
            players[i][1] = 0
            players[i][3] *= -1
            hit_wall = True

        if hit_wall:
            wall_collisions += 1

        if hit_wall and random.uniform(0, 1) < wall_death_c:
            death_note.append(i)

        for j in range(len(planets)):
            dx = planets[j][0] - players[i][0]
            dy = planets[j][1] - players[i][1]
            dist = (dx ** 2 + dy ** 2) ** 0.5
            if dist == 0:
                continue
            if dist < planets[j][6] and (abs(players[i][2]) + abs(planets[j][2])) != 0 and (abs(players[i][3]) + abs(planets[j][3])) != 0:
                dist = -1 * planets[j][6]
                death_note.append(i)
                sun_collisions += 1
                players[i][2] *= 0.6
                players[i][3] *= 0.6
            players[i][6] += gC * planets[j][7] * dx / dist ** 3
            players[i][7] += gC * planets[j][7] * dy / dist ** 3

        players[i][2] += players[i][6] * dt / (p_mass * (players[i][9] + p_mass_c))
        players[i][3] += players[i][7] * dt / (p_mass * (players[i][9] + p_mass_c))





def draw_minimap():
    minimap_x = (width_f - minimap_scale - 0.03) * window_width
    minimap_y = 0.02 * window_width
    minimap_size = minimap_scale * window_width
    pygame.draw.rect(window, (50, 200, 50), ((minimap_x - 3), (minimap_y - 3), (minimap_size + 6), (minimap_size + 6)))
    pygame.draw.rect(window, (0, 0, 0), (minimap_x, minimap_y, minimap_size, minimap_size))

    food_grid_f = []
    for y in range(grid_c):
        for x in range(grid_c):
            food_grid_f.append(food_grid[x][y])

    max_f = max(food_grid_f)
    for y in range(grid_c):
        for x in range(grid_c):
            x_draw = minimap_x + x / grid_c * minimap_size
            y_draw = minimap_y + y / grid_c * minimap_size
            intensity = int(food_grid[x][y] / max_f * 150)
            if intensity > 255:
                intensity = 255
            if intensity < 0:
                intensity = 0
            exploded = False
            if exploded_list[x][y]:
                exploded = True
            if not exploded:
                pygame.draw.rect(window, (intensity, intensity, 0), (x_draw, y_draw, minimap_size / grid_c, minimap_size / grid_c))
            else:
                pygame.draw.rect(window, (255, 0, 0), (x_draw, y_draw, minimap_size / grid_c, minimap_size / grid_c))

    for i in range(len(planets)):
        x_in = planets[i][0]
        y_in = planets[i][1]
        r_in = planets[i][6]
        color = planets[i][8]
        x = x_in * minimap_scale * window_width + minimap_x
        y = y_in * minimap_scale * window_width + minimap_y
        r = r_in * minimap_scale * window_width
        if r < 1:
            r = 1
        pygame.draw.circle(window, color, ((int(x)), (int(y))), r)

    for i in range(len(players)):
        x_in = players[i][0]
        y_in = players[i][1]
        x = x_in * minimap_scale * window_width + minimap_x
        y = y_in * minimap_scale * window_width + minimap_y
        if x_in == players[player_id][0]:
            pygame.draw.circle(window, (255, 255, 255), (x, y), 6)
            pygame.draw.circle(window, players[player_id][13], (x, y), 3)
        else:
            pygame.draw.circle(window, players[i][13], (x, y), 3)
    pygame.draw.circle(window, (255, 0, 0), (minimap_x + 0.5 * minimap_size, minimap_y + 0.5 * minimap_size), 0.1 * minimap_size, 2)



def draw_text():


    if players[player_id][8] != None:
        action_string = action_index_to_text[players[player_id][8]]
    else:
        action_string = "No action taken"
    total_deaths = max(wall_collisions + sun_collisions + old_age_deaths + starvation_deaths, 1)

    statistics = ["Iteration: " + str(itC),
                  "Obervation Mode?: " + str(is_observation_mode),
                  "Can Reproduce?: " + str(can_reproduce),
                  "Can Die?: " + str(can_die),
                  "Immobilize Player?: " + str(immobilize_player),
                  "Minimum Reproduction Age: " + str(min_reproduction_age),
                  "Time Step: " + str(round(dt, 7)),
                  "Elapsed Time: " + str(round(el_time, 7)),
                  "Zoom Factor: " + str(round(scale, 5)),
                  "Sensitivity: " + str(round(sensitivity, 10)),
                  "Average Framerate: " + str(round(itC / (time.time() - time_ref), 5)),
                  " ",
                  "Player: " +  str(player_id),
                  "Player X: " + str(round(players[player_id][0], 5)),
                  "Player Y: " + str(round(players[player_id][1], 5)),
                  "Player Angle (Radians): " + str(round(players[player_id][11], 6)),
                  "Player X-Velocity: " + str(round(players[player_id][2], 5)),
                  "Player Y-Velocity: " + str(round(players[player_id][3], 5)),
                  "Player Speed: " + str(round((players[player_id][2] ** 2 + players[player_id][3] ** 2) ** 0.5, 5)),
                  "Player X-Force: " + str(round(players[player_id][6], 5)),
                  "Player Y-Force: " + str(round(players[player_id][7], 5)),
                  "Player Age: " + str(round(players[player_id][12], 7)),
                  "Is Male?: " + str(players[player_id][14]),
                  "Player Total Force: " + str(round((players[player_id][6] ** 2 + players[player_id][7] ** 2) ** 0.5, 5)),
                  "Player Food: " + str(round(players[player_id][9], 5)),
                  " ",
                  "Players Count: " + str(len(players)),
                  "Agents Produced Sexually (all time): " + str(births_by_sex),
                  "Agents Produced Asexually (all time): " + str(births_by_not_sex),
                  "Wall_collisions frac: " + str(round(wall_collisions / total_deaths, 5)),
                  "Sun collisions frac: " + str(round(sun_collisions / total_deaths, 5)),
                  "Old age deaths frac: " + str(round(old_age_deaths / total_deaths, 5)),
                  "Starvation deaths frac: " + str(round(starvation_deaths / total_deaths, 5)),
                  "Total Food (e5): " + str(round(total_food / 100000, 5)),
                  " ",
                  "Player Last Action: " + str(action_string)
                 ]

    outputs = ["               BRAIN 1",
               "Memory 1: " + str(round(players[player_id][10][0][0][35], 5)),
               "Memory 2: " + str(round(players[player_id][10][0][0][36], 5)),
               "Communication to others 1: " + str(round(players[player_id][10][0][0][37], 5)),
               "Communication to others 2: " + str(round(players[player_id][10][0][0][38], 5)),
               "Willingness to reproduce male/asexually: " + str(round(players[player_id][10][0][0][39], 5)),
               "Willingness to reproduce sexually: " + str(round(players[player_id][10][0][0][40], 5)),
               "Rotate Left: " + str(round(players[player_id][10][0][0][41], 5)),
               "Thrust Forward: " + str(round(players[player_id][10][0][0][42], 5)),
               "Rotate Right: " + str(round(players[player_id][10][0][0][43], 5)),
               "Thrust Backwards: " + str(round(players[player_id][10][0][0][44], 5)),
               "Explode: " + str(round(players[player_id][10][0][0][45], 5)),
               "Rest: " + str(round(players[player_id][10][0][0][46], 5)),
               "Male coefficient: " + str(round(sigmoid(players[player_id][10][0][1][-2]), 5)),
               "Female coefficient: " + str(round(sigmoid(players[player_id][10][0][1][-1]), 5)),
               "Thrust coefficient: " + str(round(sigmoid(players[player_id][10][0][0][47]), 5)),
               "Fuel Transfer Ratio: " + str(round(sigmoid(players[player_id][10][0][0][48]), 5)),
               "Mutation Rate: " + str(round(sigmoid(players[player_id][10][0][1][-3] - 1), 5)),
               "Mutation Dampening Rate: " + str(round(sigmoid(players[player_id][10][0][1][-4]), 5))


              ]




    outputs_2 = ["               BRAIN 2",
               "Memory 1: " + str(round(players[player_id][10][1][0][35], 5)),
               "Memory 2: " + str(round(players[player_id][10][1][0][36], 5)),
               "Communication to others 1: " + str(round(players[player_id][10][1][0][37], 5)),
               "Communication to others 2: " + str(round(players[player_id][10][1][0][38], 5)),
               "Rotate Left: " + str(round(players[player_id][10][1][0][41], 5)),
               "Thrust Forward: " + str(round(players[player_id][10][1][0][42], 5)),
               "Rotate Right: " + str(round(players[player_id][10][1][0][43], 5)),
               "Thrust Backwards: " + str(round(players[player_id][10][1][0][44], 5)),
               "Explode: " + str(round(players[player_id][10][1][0][45], 5)),
               "Rest: " + str(round(players[player_id][10][1][0][47], 5)),
               "Male coefficient: " + str(round(sigmoid(players[player_id][10][1][1][-2]), 5)),
               "Female coefficient: " + str(round(sigmoid(players[player_id][10][1][1][-1]), 5))

              ]



    for i in range(len(statistics)):
        text_surface = font.render(statistics[i], True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10, newline_spacing * i)
        window.blit(text_surface, text_rect)

    for i in range(len(outputs)):
        text_surface = font.render(outputs[i], True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10, newline_spacing * i + 25 * len(statistics) + 25)
        window.blit(text_surface, text_rect)

    for i in range(len(outputs_2)):
        text_surface = font.render(outputs_2[i], True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (10, newline_spacing * i + 25 * len(statistics) + 25 * len(outputs) + 50)
        window.blit(text_surface, text_rect)


def draw_vectors():
    x = window_width / 2
    y = window_width / 2
    # Draw line for velocity vector
    vx = players[player_id][2]
    vy = players[player_id][3]
    v_dist = (vx ** 2 + vy ** 2) ** 0.5
    if v_dist != 0:
        x_v = x + vx / v_dist * 20
        y_v = y + vy / v_dist * 20
        pygame.draw.line(window, (0, 255, 0), (x, y), (x_v, y_v), 2)

    # Draw line for force vector
    fx = players[player_id][6]
    fy = players[player_id][7]
    f_dist = (fx ** 2 + fy ** 2) ** 0.5
    if f_dist != 0:
        x_f = x + fx / f_dist * 20
        y_f = y + fy / f_dist * 20
        pygame.draw.line(window, (255, 0, 0), (x, y), (x_f, y_f), 2)




def draw_scene():
    global scale
    if len(players) == 0:
        return 0
    x_player = players[player_id][0]
    y_player = players[player_id][1]

    for i in range(len(planets)):
        x_in = planets[i][0]
        y_in = planets[i][1]
        r_in = planets[i][6]
        color = planets[i][8]
        x = (scale * (x_in - x_player) + 0.5) * window_width
        y = (scale * (y_in - y_player) + 0.5) * window_width
        r = r_in * window_width * scale
        if x + r < 0 or x - r > window_width or y + r < 0 or y - r > window_width:
            continue
        pygame.draw.circle(window, color, (int(x), int(y)), r)

def draw_players():
    global scale
    z_p = sigmoid(math.log(scale) - 3.5) * 2 + 0.12  # Make players smaller when zooming out
    if len(players) == 0:
        return
    x_player = players[player_id][0]
    y_player = players[player_id][1]
    for i in range(len(players)):
        angle = players[i][11]
        dx = math.cos(angle) * 20 * z_p
        dy = math.sin(angle) * 20 * z_p
        x_in = players[i][0]
        y_in = players[i][1]
        x = (scale * (x_in - x_player) + 0.5) * window_width
        y = (scale * (y_in - y_player) + 0.5) * window_width
        player_color = players[i][13]

        front_x = x + dx
        front_y = y + dy
        back_x = x - dx
        back_y = y - dy

        # Rocket fins
        fin_length = 15 * z_p
        fin_width = 20 * z_p

        left_fin_x1 = back_x + math.cos(angle + (math.pi / 2)) * fin_width
        left_fin_y1 = back_y + math.sin(angle + (math.pi / 2)) * fin_width
        left_fin_x2 = back_x + math.cos(angle) * fin_length
        left_fin_y2 = back_y + math.sin(angle) * fin_length

        pygame.draw.polygon(window, player_color, [(back_x, back_y), (left_fin_x1, left_fin_y1), (left_fin_x2, left_fin_y2)])

        right_fin_x1 = back_x + math.cos(angle - (math.pi / 2)) * fin_width
        right_fin_y1 = back_y + math.sin(angle - (math.pi / 2)) * fin_width
        right_fin_x2 = back_x + math.cos(angle) * fin_length
        right_fin_y2 = back_y + math.sin(angle) * fin_length

        pygame.draw.polygon(window, player_color, [(back_x, back_y), (right_fin_x1, right_fin_y1), (right_fin_x2, right_fin_y2)])

        # Rocket body
        pygame.draw.line(
            window,
            (int(0.8 * player_color[0]), int(0.8 * player_color[1]), int(0.8 * player_color[2])),
            (back_x, back_y),
            (front_x, front_y),
            int(15 * z_p)
        )

        # Rocket nose
        base_length = 15 * z_p
        height = 15 * z_p

        left_base_x = front_x + math.cos(angle + math.pi / 2) * base_length
        left_base_y = front_y + math.sin(angle + math.pi / 2) * base_length

        right_base_x = front_x + math.cos(angle - math.pi / 2) * base_length
        right_base_y = front_y + math.sin(angle - math.pi / 2) * base_length

        tip_x = front_x + math.cos(angle) * height
        tip_y = front_y + math.sin(angle) * height

        pygame.draw.polygon(window, player_color, [(tip_x, tip_y), (left_base_x, left_base_y), (right_base_x, right_base_y)])

        # Contingency flame triangle
        flame_length = 25 * z_p

        flame_x1 = back_x + math.cos(angle - (math.pi / 2)) * flame_length
        flame_y1 = back_y + math.sin(angle - (math.pi / 2)) * flame_length
        flame_x2 = back_x + math.cos(angle + (math.pi / 2)) * flame_length
        flame_y2 = back_y + math.sin(angle + (math.pi / 2)) * flame_length
        flame_x3 = back_x - math.cos(angle) * flame_length
        flame_y3 = back_y - math.sin(angle) * flame_length

        if players[i][8] == 1:
            pygame.draw.polygon(window, (255, 140, 0), [(flame_x1, flame_y1), (flame_x2, flame_y2), (flame_x3, flame_y3)])
        elif players[i][8] == 3:
            pygame.draw.polygon(window, (0, 140, 255), [(flame_x1, flame_y1), (flame_x2, flame_y2), (flame_x3, flame_y3)])



clear_timelapse_pics_folder()
food_grid = initialize_food()
clear_exploded_grid()

if not load_players:
    create_players(initial_agent_count)
else:
    players = copy.deepcopy(load_player_data())

update_info_grid()


running = True
while running:

    find_total_food()


    if itC % 1 == 0:
        write_stats()
        window.fill((0, 0, 0))
        draw_scene()
        draw_vectors()
        draw_players()
        if show_minimap:
            update_info_grid()
            draw_minimap()
        draw_text()
        pygame.display.flip()

    if itC % 1 == 0:
        save_timelapse_frame()


    death_note = []
    run_physics()
    update_info_grid()

    clear_exploded_grid()
    kill_player = False
    num_c = 50  # Can leave space
    for i in range(len(players)):
        if  i == player_id:
            players[player_id][8] = find_and_delete_most_recent_command()
            command = players[player_id][8]
            sensitivity_p = sensitivity
        if is_observation_mode and command == None or i != player_id:
            players[i][8] = run_brain(i)
            if players[i][8] == -1:
                continue
            sensitivity_p = players[i][10][0][0][46] * sensitivity
            command = players[i][8] + i * num_c
        if command != None:
            player_id_c = int((command - command % num_c) / num_c)
            if player_id_c < 0 or player_id_c > len(players) - 1:
                continue
            if command % num_c == 0:
                players[player_id_c][11] += math.pi / 4
                players[player_id_c][11] = players[player_id_c][11] % (2 * math.pi)
            if command % num_c == 1:  # Up arrow
                players[player_id_c][2] += sensitivity_p * math.cos(players[player_id_c][11]) / (p_mass * (players[player_id_c][9] + p_mass_c))
                players[player_id_c][3] += sensitivity_p * math.sin(players[player_id_c][11]) / (p_mass * (players[player_id_c][9] + p_mass_c))
                players[player_id_c][9] -= sensitivity_p * fuel_cost
            if command % num_c == 2:
                players[player_id_c][11] -= math.pi / 4
                players[player_id_c][11] = players[player_id_c][11] % (2 * math.pi)
            if command % num_c == 3:
                players[player_id_c][2] -= sensitivity_p * math.cos(players[player_id_c][11]) / (p_mass * (players[player_id_c][9] + p_mass_c)) / 2 # Penalty for using backthrust
                players[player_id_c][3] -= sensitivity_p * math.sin(players[player_id_c][11]) / (p_mass * (players[player_id_c][9] + p_mass_c)) / 2 # Penalty for using backthrust
                players[player_id_c][9] -= sensitivity_p * fuel_cost

            if command % num_c == 24:
                x_index = int(players[player_id_c][0] * grid_c)
                y_index = int(players[player_id_c][1] * grid_c)
                if x_index > grid_c - 1:
                    x_index = grid_c - 1
                if y_index > grid_c - 1:
                    y_index = grid_c - 1
                if x_index < 0:
                    x_index = 0
                if y_index < 0:
                    y_index = 0
                exploded_list[x_index][y_index] = True
                for j in info_grid[x_index][y_index]:
                    if j != player_id_c:
                        death_note.append(j)

            # Boundary on actions human vs. non-human can perform

            if command % num_c == 4:
                players[player_id_c][5] *= 0.5
            if command % num_c == 5:
                players[player_id_c][5] *= 1 / 1.1
            if command % num_c == 6:
                players[player_id_c][5] *= 1.1
            if command % num_c == 7:
                players[player_id_c][5] *= 2

            if players[player_id_c][5] > 2:  # Cap on sensitivity
                players[player_id_c][5] = 2


            if command % num_c == 8:
                scale *= 0.5
            if command % num_c == 9:
                scale *= 1 / 1.1
            if command % num_c == 10:
                scale *= 1.1
            if command % num_c == 11:
                scale *= 2
            if command % num_c == 12 and player_id == player_id_c:
                player_id += 1
                if player_id >= len(players):
                    player_id = 0
            if command % num_c == 13:
                dt *= 0.5
            if command % num_c == 14:
                dt *= 0.9
            if command % num_c == 15:
                dt *= 1.1
            if command % num_c == 16:
                dt *= 1.5
            if command % num_c == 17:
                show_minimap = not show_minimap
            if command % num_c == 18:
                player_id -= 1
                if player_id < 0:
                    player_id = len(players) - 1
            if command % num_c == 19:
                can_die = not can_die
            if command % num_c == 20:
                can_reproduce = not can_reproduce
            if command % num_c == 21:
                is_observation_mode = not is_observation_mode
            if command % num_c == 22:
                kill_player = True
            if command % num_c == 23:
                immobilize_player = not immobilize_player
    if kill_player:
        death_note.append(0)





    if itC % 500 == 0:
        if is_master:
            write_to_text_file()
        else:
            players_in = load_player_data()
            planets_in = load_planet_data()
            if players_in != "f":
                players = copy.deepcopy(players_in)
            if planets_in != "f":
                planets = copy.deepcopy(planets_in)

    itC += 1
    el_time += dt


    update_info_grid()
    iterate_players()
    add_food()
    if itC % corner_int == 0:
        corner += 1
    if corner >= 4:
        corner = 0


    if random.uniform(0, 1) < player_make_c:
        create_players(1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()




