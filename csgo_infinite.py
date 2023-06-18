import random
import time

class player:
    def __init__(self, team, role, position):
        #role has a dictionary of values
        
        self.team = team # -1 for terror, 0 for counter
        self.role_name = role['name']
        self.health = role['health']
        self.max_health = role['health']
        self.damage = role['damage']
        self.position = position # list, x and y
    
    def move(self, movement): #list of [x, y]
        self.position = movement  
    
    def shoot_damage(self):
        return self.damage
    
    def damage_taken(self, damage):
        self.health = int(self.health) - int(damage)
        
    def revive(self):
        self.health = role['health']
        
    def __str__(self):
        if int(self.health) > 0:
            final = "\N{Large Green Circle}" +  str(self.role_name) + " " + "(" + str(self.health) + "/" + str(self.max_health) + ")"
        else:
            final = "\N{Large Red Circle}" +  str(self.role_name) + " " + "(" + str(self.health) + "/" + str(self.max_health) + ")"
            
        return final
    
    
    
    
    
def map_grid(filename): 
    #reads the map file
    
    with open(filename, "r", encoding="utf-8") as file:
        file = file.readlines()
    
    return file
    

def get_spawn_t(file): 
    #finds T spawn
    
    final = []
    
    for row in range(len(file)):
        for col in range(len(file[row])):
            if file[row][col] == "T":
                final.append([row, col]) # returns row and col index in list
                
    return final

def get_spawn_ct(file):
    #same as t spawn 
    final = []
    
    for row in range(len(file)):
        for col in range(len(file[row])):
            if file[row][col] == "C":
                final.append([row, col])
    
    return final

def display_map(grid):
    #gets grid then prints it with emojis
        
    for i in range(len(grid)):
        print(" ")                           # print new line every row
        for letter in range(len(grid[i])):
            
            #flooring and walls    
            if grid[i][letter] == "*":
                print("\N{Large Brown Circle}", end='')
            elif grid[i][letter] == "-":
                print("\N{Large Yellow Square}", end= "")
            elif grid[i][letter] == "B":
                print("\N{Large Red Square}", end = "")
            elif grid[i][letter] == "A":
                print("\N{Large Blue Square}", end = "")
            elif grid[i][letter] == "%":
                print("\N{door}", end = "")
            elif grid[i][letter] == "&":
                print("\N{window}", end = "")            
                
            #players and deaths        
            elif grid[i][letter] == "C":
                print("\N{face with cowboy hat}", end = "")
            elif grid[i][letter] == "T":
                print("\N{Shocked face with exploding head}" ,end = "")
            elif grid[i][letter] == "D":
                print("\N{skull}", end = "")
            else:
                print("", end= "")
                
                
                
def move(grid, i):
    #create a random movement from 0-3.
    # i is a player class object in a list.
    movement_t = random.randint(0,8) 
    
    if movement_t == 0:
        movement_t = "north"
    if movement_t == 1:
        movement_t = "east"
    if movement_t == 2:
        movement_t = "south"
    if movement_t == 3:
        movement_t = "west"
    if movement_t == 4:
        movement_t = "west"
    if movement_t == 5:
        movement_t = "east"
    if movement_t == 6:
        movement_t = "north"
    if movement_t == 7:
        movement_t = "north"
    
    
    old_pos = i.position
    
    if int(i.team) == -1:
        if check_move(i.position, movement_t, grid):
        
            if movement_t == "north":
                new_pos = [(i.position[0]-1), i.position[1]] #move in desired direction
                i.move(new_pos)
            
            if movement_t == "east":
                new_pos = [i.position[0], (i.position[1]+1)]
                i.move(new_pos)
            
            if movement_t == "west":
                new_pos = [i.position[0], (i.position[1]-1)]
                i.move(new_pos)
                
            if movement_t == "south":
                new_pos = [(i.position[0]+1), i.position[1]]
                i.move(new_pos)
    
    movement_ct = random.randint(0,8) 
    
    if movement_ct == 0:
        movement_ct = "north"
    if movement_ct == 1:
        movement_ct = "east"
    if movement_ct == 2:
        movement_ct = "south"
    if movement_ct == 3:
        movement_ct = "west"
    if movement_ct == 4:
        movement_ct = "west"
    if movement_ct == 5:
        movement_ct = "east"
    if movement_ct == 6:
        movement_ct = "south"
    if movement_ct == 7:
        movement_ct = "south"
        
    if int(i.team) == 0:
        if check_move(i.position, movement_ct, grid):
        
            if movement_ct == "north":
                new_pos = [(i.position[0]-1), i.position[1]] #move in desired direction
                i.move(new_pos)
            
            if movement_ct == "east":
                new_pos = [i.position[0], (i.position[1]+1)]
                i.move(new_pos)
            
            if movement_ct == "west":
                new_pos = [i.position[0], (i.position[1]-1)]
                i.move(new_pos)
                
            if movement_ct == "south":
                new_pos = [(i.position[0]+1), i.position[1]]
                i.move(new_pos)
                
    grid = update_map(grid, i, old_pos)
    return grid
        
def update_map(grid, player, old):
    #removes players old position in grid.
    #updates with new position from move method.
    o_row = old[0]
    o_col = old[1]
    n_row = player.position[0]
    n_col = player.position[1]
    
    fake = []
    for row in grid:
        row_blank = []
        for col in row:
            col_blank = []
            col_blank.append(col)
            row_blank.append(col_blank)
            
        fake.append(row_blank)
            
    template_map = map_grid("dust.txt")
    if template_map[o_row][o_col] in ["T", "C", "-"]:
        fake[o_row][o_col][0] = "-"
    else:
        fake[o_row][o_col][0] = template_map[o_row][o_col]
    
    
    if player.team == -1:
        fake[n_row][n_col][0] = "T"
    elif player.health == 0:
        fake[n_row][n_col][0] = "D"
    else:
        fake[n_row][n_col][0] = "C"
    
    
    
    final = []
    for row in fake:
        maps = ""
        for col in row:
            maps = maps + col[0] 
        final.append(maps)  
        
    return final

def check_move(current_pos, direction, grid):
    row = current_pos[0]
    col = current_pos[1]
    cant_go = ("*", "T", "C")
    
    if direction == "north":
        if grid[row-1][col] in cant_go:
            return False
        else:
            return True
        
    elif direction == "east":
        if grid[row][col+1] in cant_go:
            return False
        else:
            return True
    
    elif direction == "west":
        if grid[row-1][col-1] in cant_go:
            return False
        else:
            return True
        
    elif direction == "south":
        if grid[row+1][col] in cant_go:
            return False
        else:
            return True
        
def death(grid, player):
    #return a grid with a death skull
    death_row = player.position[0]
    death_col = player.position[1]

    fake = []
    for row in grid:
        row_blank = []
        for col in row:
            col_blank = []
            col_blank.append(col)
            row_blank.append(col_blank)

        fake.append(row_blank)
        
    fake[death_row][death_col][0] = "D"

    final = []
    for row in fake:
        maps = ""
        for col in row:
            maps = maps + col[0] 
        final.append(maps)  

    return final

def going(players):
  
    for i in players:
        t_death = 0
        ct_death = 0
        if i.team == -1:
            if i.health <= 0:
                t_death += 1
                
        if i.team == 0:
            if i.health <= 0:
                ct_death += 1
                
    if ct_death == 5 or t_death == 5:
        return False
    else:
        return True
    
def see_col(t_pos, ct_pos, grid):
    t_col = t_pos[1]
    t_row = t_pos[0]
    ct_row = ct_pos[0]
    ct_col = ct_pos[1]
    x = 0
    
    if ct_row > t_row:
        for row in grid[ct_row:t_row]:
            for letter in row:
                if letter[0:1] == "-":
                    x += 1
                    
        if x == len(grid[ct_col:t_col]):
            return True 
        
    else:
        for row in grid[t_col:ct_col+1]:
            for letter in row:
                if letter[0:1] == "-":
                    x += 1
        
        if x == len(grid[t_col:ct_col+1]):
            return True
                
def see_row(t_pos, ct_pos, grid):
    t_row = t_pos[0]
    t_col = t_pos[1]
    ct_col = ct_pos[1]
    
    if t_col > ct_col:
        if grid[t_row][t_col+1:ct_col].count("-") == len(grid[t_row][t_col+1:ct_col]):
            return True
        elif grid[t_row][t_col:ct_col+1].count("&") >= 1: #shoot through glass
            return True
    elif ct_col > t_col:
        if grid[t_row][ct_col:t_col+1].count("-") == len(grid[t_row][ct_col:t_col+1]):
            return True
        elif grid[t_row][ct_col:t_col+1].count("&") >= 1: #shoot through glass
            return True        
    else:
        return False
    

def display_stats(strings):
    ct = strings[5:len(strings)]
    t = strings[0:5]
    print("")
    print(" "*25 + "\N{Large Blue Circle}" +"COUNTER-TERROR" + " "*25 + "\N{Large Yellow Circle}"+"TERROR")
    for i in range(len(ct)):
        print("")
        print(" " *25 + ct[i] + " "*25 + t[i])

def main():    
    grid = map_grid("dust.txt")
    
    roles_ct = [{"name" : "LEAD", "health" : 100, "damage" : 35},  # all counters
                {"name" : "HOLD", "health" : 100, "damage" : 40},# all counters
                {"name" : "AWP!", "health" : 100, "damage" : 150 }, #counter is entry
                {"name" : "SUPP", "health" : 100, "damage" : 40}, #counter by awp
                {"name" : "BACK", "health" : 100, "damage" : 50}] #counter by entry\igl
    
    roles_t = [{"name" : "IGL", "health" : 100, "damage" : 35},  # all counters
                {"name" : "ENTRY", "health" : 100, "damage" : 40},# all counters
                {"name" : "AWP!", "health" : 100, "damage" : 150 }, #counter is entry
                {"name" : "SUPP", "health" : 100, "damage" : 40}, #counter by awp
                {"name" : "LURK", "health" : 100, "damage" : 50}] #counter by entry\igl
    
    t_spawn = get_spawn_t(grid)
    ct_spawn = get_spawn_ct(grid)
    
   
    player1 = player(-1, roles_t[0], t_spawn[0])
    player2 = player(-1, roles_t[1], t_spawn[1])
    player3 = player(-1, roles_t[2], t_spawn[2])
    player4 = player(-1, roles_t[3], t_spawn[3])
    player5 = player(-1, roles_t[4], t_spawn[4])
    t_players = [player1, player2, player3, player4, player5]
    
    ct_player1 = player(0, roles_ct[0], ct_spawn[0])
    ct_player2 = player(0, roles_ct[1], ct_spawn[1])
    ct_player3 = player(0, roles_ct[2], ct_spawn[2])
    ct_player4 = player(0, roles_ct[3], ct_spawn[3])
    ct_player5 = player(0, roles_ct[4], ct_spawn[4])
    ct_players = [ct_player1, ct_player2, ct_player3, ct_player4, ct_player5]
    
    players = t_players + ct_players

    
    for i in range(len(players)):
        grid = move(grid, players[i])
   
    action = 0
    bomb_plant = False
    round_condition = True
    
    while round_condition == True:
        for i in players:
            if i.health > 0:
                grid = move(grid, i)
            else:
                grid = death(grid, i)
        
        for t in t_players:
                for ct in ct_players:
                    if ct.health > 0 and t.health > 0:
                        
                        damager = t.shoot_damage()
                        damager_ct = ct.shoot_damage()
                        if t.position[0] in [2,3,4] and t.position[1] in [4,5,6] or t.position[1] in [44, 45, 46]:
                            bomb_plant = True
                            break
                        
                        if t.position[0] == ct.position[0] and see_row(t.position, ct.position, grid):
                            print("")
                            var = random.randint(0,1)
                            
                            if var == 0:
                                ct.damage_taken(damager)
                                print(f"{str(ct.team)}: {ct} has taken {damager} damage! ({ct.health} / {ct.max_health})")
                                print(f"{str(t.team)}: {t} has dealt the damage!")
                            
                            else:
                                t.damage_taken(damager_ct)
                                print(f"{str(t.team)}: {t} has taken {damager} damage!")
                                print(f"{str(ct.team)}: {ct} has dealt the damage!")                       
                            action = 1
                                
                    
                        elif t.position[1] == ct.position[1] and see_col(t.position, ct.position, grid):
                            print("")
                            var = random.randint(0,1)
                    
                            if var == 0:                    
                                ct.damage_taken(damager)
                                print(f"{str(ct.team)}: {ct} has taken {damager} damage!)")
                                print(f"{str(t.team)}: {t} has dealt the damage!")
                    
                            else:
                                t.damage_taken(damager_ct)
                                print(f"{str(t.team)}: {t} has taken {damager} damage!")
                                print(f"{str(ct.team)}: {ct} has dealt the damage!")                        
                            action = 1
                            
        
        
        if action == 1:
            print()
            print(">>------>  >>------>  >>------>" * len(grid[1]))
            print("\n" * 12)
            time.sleep(0.85)
        else:
            print("\n" * 16)
            time.sleep((.4))
            
        action = 0    
        display_map(grid)
        
        t_death = 0
        ct_death = 0

        for i in players:
            if int(i.health) <= 0:
                if int(i.team) == 0:
                    ct_death += 1
                else:
                    t_death += 1

        if ct_death == 5 or t_death == 5:
            round_condition = False
        elif bomb_plant == True:
            round_condition = False
    
        
        
        overall_stats = []
        
        for i in t_players:
            overall_stats.append(str(i))
            
        for i in ct_players:
            overall_stats.append(str(i))
            
        display_map(grid)
        print("")
        display_stats(overall_stats)
        
    if ct_death == 5:
        print("Congratulations, Terror has won!")
    else:
        print("Well Done, Enemy forces eleminated.")
            
main()