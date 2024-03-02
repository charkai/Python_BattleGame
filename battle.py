import sys

class player: 

  def __init__(self, player):
    self.name = player

    # player 1 and player 2 have lists initialised for their surrounding base and home base
    if player == "Player 1": 
        self.base = [1,1]
        self.surrounding_base = [[0, 1], [1, 0], [2, 1], [1, 2]] 

        self.unoccupied_positions = [[0, 1], [1, 0], [2, 1], [1, 2]] # all positions next to the home base are initially unoccupied (and free for recruitment)

    if player == "Player 2": 
        self.base = [width-2, height-2]
        self.surrounding_base = [[width-3, height-2], [width-2, height-3], [width-1, height-2], [width-2, height-1]]

        self.unoccupied_positions = [[width-3, height-2], [width-2, height-3], [width-1, height-2], [width-2, height-1]] #all positions next to the home base are initially unoccupied (and free for recruitment)
    
    # each player begins with 2 of each resource 
    self.wood = 2
    self.food = 2
    self.gold = 2

    # a list is initialised for each player's respective armies
    self.spearman = []  
    self.archer = [] 
    self.knight = [] 
    self.scout = []
    self.scout_intermediary_positions = [] 


  def check_sufficient_resources_spearman(self): 
    # this function checks if the player has sufficient resources to recruit a spearman (1 wood and 1 food)

    if self.wood < 1 or self.food < 1: 
      sufficient = False
    else: 
      sufficient = True 
    return sufficient   


  def check_sufficient_resources_archer(self):
    # this function checks if the player has sufficient resources to recruit an archer (1 wood and 1 gold)

    if self.wood < 1 or self.gold < 1: 
      sufficient = False
    else: 
      sufficient = True 
    return sufficient   


  def check_sufficient_resources_knight(self):
    # this function checks if the player has sufficient resources to recruit a knight (1 food and 1 gold)

    if self.food < 1 or self.gold < 1: 
      sufficient = False
    else: 
      sufficient = True 
    return sufficient 


  def check_sufficient_resources_scout(self):
    # this function checks if the player has sufficient resources to recruit a scout (1 wood, 1 food and 1 gold)

    if self.wood < 1 or self.food < 1 or self.gold < 1: 
      sufficient = False
    else: 
      sufficient = True 
    return sufficient  


  def move_spearmen(self, initial_position, new_position):
    # this function moves the player's spearman from an initial position to a new position

    # iterating over the list allows the index of the initial position to be obtained so that the new position can be inserted in its place
    i = 0 
    while i < len(self.spearman): 
      if initial_position == self.spearman[i]:
        break
      i += 1 
    self.spearman.remove(initial_position)
    self.spearman.insert(i, new_position)


  def move_archer(self, initial_position, new_position): 
    # this function moves the player's archer from an initial position to a new position

    # iterating over the list allows the index of the initial position to be obtained so that the new position can be inserted in its place
    i = 0 
    while i < len(self.archer): 
      if initial_position == self.archer[i]:
        break
      i += 1 
    self.archer.remove(initial_position)
    self.archer.insert(i, new_position)
  

  def move_knight(self, initial_position, new_position): 
    # this function moves the player's knight from an initial position to a new position

    # iterating over the list allows the index of the initial position to be obtained so that the new position can be inserted in its place
    i = 0
    while i < len(self.knight): 
      if initial_position == self.knight[i]:
        break
      i += 1
    self.knight.remove(initial_position)
    self.knight.insert(i, new_position)


  def move_scout(self, initial_position, new_position): 
    # this function moves the player's scout from an initial position to a new position

    # iterating over the list allows the index of the initial position to be obtained so that the new position can be inserted in its place
    i = 0 
    while i < len(self.scout): 
      if initial_position == self.scout[i]:
        break
      i += 1 

    # As scouts can move up to two steps (in the same direction), this block of code records the 'intermediary step' for the scout if they took two steps
    if new_position[0] == initial_position[0]: 
      if new_position[1] == initial_position[1]+2: # if the scout moved two steps up
        self.scout_intermediary_positions.append([new_position[0], initial_position[1]+1])

      elif new_position[1] == initial_position[1]-2: #if the scout moved two steps down 
        self.scout_intermediary_positions.append([new_position[0], initial_position[1]-1])

    elif new_position[1] == initial_position[1]: 
      if new_position[0] == initial_position[0] +2: #if the scout moved two steps right 
        self.scout_intermediary_positions.append([initial_position[0]+1, new_position[1]])

      if new_position[0] == initial_position[0] -2: #if the scout moved two steps left 
        self.scout_intermediary_positions.append([initial_position[0]-1, new_position[1]])

    self.scout.remove(initial_position)
    self.scout.insert(i, new_position)


  def collect_resources(self, new_position):
    # this function allows a player to collect the resources if their armies move to that space, and remove that resource from the map
    if new_position in woods: 
      current_player.wood += 2 
      woods.remove(new_position)
      print("Good. We collected 2 Wood.")

    if new_position in foods: 
      current_player.food += 2
      foods.remove(new_position)
      print("Good. We collected 2 Food.")

    if new_position in golds: 
      current_player.gold += 2
      golds.remove(new_position)        
      print("Good. We collected 2 Gold.")

class Frame: 
  # a class is initialised for the Frame/map 

  def __init__(self, width, height):
    self.size = "{}x{}".format(width, height) 
 

  # the following function prints the map/Frame
  def print_game_board(self): 
    print("Please check the battlefield, commander.")


    # the first line is built as a string, with the length of the string depending on the width given in the configuration file
    first_line = ''
    for x in range(width): 
      if x == 0: 
        first_line += '  X0{}'.format(x) #the beginning of the string
      elif x > 0: 
        first_line += ' 0{}'.format(x) #the 'body' of the string 
      if x == (width-1): 
        first_line += 'X' #the end of the string 
    print(first_line)
      

    dash_number = (3*width)-1 # the number of dashes in the second and last line is proportional to the width by this formula 
    second_and_last_line =' Y+{}+'.format('-'*dash_number) 
    print(second_and_last_line)


    # each line of the map is built as a string, with the length of the string depending on the width given in the config file
    # the number of lines depends on the height given in the config file 
    for y in range(height): 
      line = ''
      for x in range(width): 
        if x == 0: 
          line += '0{}|'.format(y) #the beginning of the string 
        line += "{}|".format(get_symbol(x, y)) #the 'body' of the string
      print(line)

    print(second_and_last_line) # the last line is identical to the second line

def get_symbol(x, y):
  # this function checks for the symbols to occupy each of the map spaces

  symbol = "  " #the default symbol is an blank space 

  # check bases and water
  if [x, y] in waters: 
    symbol = "~~"
  if [x, y] == player1.base: 
    symbol = "H1"
  if [x, y] == player2.base: 
    symbol = "H2"

  # check resources
  if [x, y] in woods: 
    symbol = "WW" 
  if [x, y] in foods: 
    symbol = "FF"
  if [x, y] in golds: 
    symbol = "GG"
  
  #check player 1 armies 
  if [x, y] in player1.spearman: 
    symbol = "S1"
  if [x, y] in player1.archer: 
    symbol = "A1"
  if [x, y] in player1.knight: 
    symbol = "K1"
  if [x, y] in player1.scout: 
    symbol = "T1"

  # check player 2 armies 
  if [x, y] in player2.spearman: 
    symbol = "S2"
  if [x, y] in player2.archer: 
    symbol = "A2"
  if [x, y] in player2.knight: 
    symbol = 'K2'
  if [x, y] in player2.scout: 
    symbol = 'T2'
   
  return symbol

def display_prices(): 
  # whenever a user calls the 'PRIS' command, the same message is printed
  print("Recruit Prices:")
  print("  Spearman (S) - 1W, 1F") 
  print("  Archer (A) - 1W, 1G") 
  print("  Knight (K) - 1F, 1G")
  print("  Scout (T) - 1W, 1F, 1G")

def check_for_quit_dis_or_prices(answer): 
    # whenever a user is prompted for an input, this function checks whether the user wishes to enact the commands of 'QUIT', 'PRIS', or 'DIS'

    if answer == 'QUIT': 
        game_finished = True
        quit()
    if answer == 'PRIS': 
        display_prices()
        return True
    if answer == 'DIS': 
        gamemap.print_game_board()
        return True
    return False

# Please implement this function according to Section "Read Configuration File"
def load_config_file(filepath):
  # It should return width, height, waters, woods, foods, golds based on the file
  # Complete the test driver of this function in file_loading_test.py
  width, height = 0, 0
  waters, woods, foods, golds = [], [], [], [] # list of positions
  file_var = open(filepath, "r") 


  # ---- CHECKING FOR FILE FORMAT ERROR ---- #


  #the following code adds each line of the configuration file as separate elements in a list
  lines = [] 
  for line in file_var:
    lines.append(line.strip())

  # this code checks for blank lines in the file, which would make it invalid 
  if '' in lines: 
    raise SyntaxError("Invalid Configuration File: format error!")
      
  # this code checks if number of lines is greater than 5, or if the required labels are not correct, which would make it invalid
  if len(lines) != 5 or lines[0].split()[0] != "Frame:" or lines[1].split()[0] != "Water:" or lines[2].split()[0] != "Wood:" or lines[3].split()[0] != "Food:" or lines[4].split()[0] != "Gold:": 
    raise SyntaxError("Invalid Configuration File: format error!")


  #---- CHECKING CONTENT OF FRAME---- #


  try: 
    frame_line = lines[0].split() # the line containing the frame information 

    if len(frame_line) != 2: #if too many arguments are put into the frame information, the file is invalid.
      raise IndexError

    frame = frame_line[1] 
    dimensions = frame.split("x")
    if len(dimensions) != 2: #if more than two dimensions for the frame were given, the file is invalid
      raise IndexError 
    width = int(dimensions[0]) 
    height = int(dimensions[1])
    
  except (IndexError, ValueError):  # an error will be raised if there is no x separating width and height, if there is no input, if there were too many arguments or dimensions, or if inputs were non-integers
    raise SyntaxError('Invalid Configuration File: frame should be in format widthxheight!')
  
  if width < 5 or width > 7 or (height < 5 or width > 7): #width and height should be between 5 and 7, otherwise the file is invalid
    raise ArithmeticError('Invalid Configuration File: width and height should range from 5 to 7!')
  

  #---- CHECKING CONTENT OF WATER, WOOD, FOOD AND GOLD ----#


  coords = [] #A list is initialised all the coordinates, with a list of coordinates each separate resource
  all_coordinates_duplicates_check = [] #this list stores all the coordinates regardless of resource, in order to check for duplicates later in the program
  
  line_names = ['Frame', 'Water', 'Wood', 'Food', 'Gold']
  for each_line in range(1,5): #For Water, Wood, Food and Gold

    line_label = line_names[each_line]
    stringed_integer_coordinates = lines[each_line].split()[1:] #remove the label, place all of the integers into a list 
 
    try: 
      integer_coordinates = [int(each_elem) for each_elem in stringed_integer_coordinates] 

    except ValueError: #if any of the inputs in the line are not integers, the file is invalid
      raise ValueError("Invalid Configuration File: {} contains non integer characters!".format(line_label))

    if len(integer_coordinates) % 2 !=0: #if there is an odd number of elements in the line, the file is invalid
      raise SyntaxError("Invalid Configuration File: {} has an odd number of elements!".format(line_label))
    


    # check none of the x coordinates exceed the width by iterating over the list for even indexes (x-coordinates)
    i = 0 
    while i < len(integer_coordinates): 
      if integer_coordinates[i] > width: 
        raise ArithmeticError("Invalid Configuration File: {} contains a position that is out of map.".format(line_label))
      i += 2 


    # check none of the y coordinates exceed the height by iterating over the list for odd indexes (y-coordinates)
    i = 1
    while i < len(integer_coordinates): 
      if integer_coordinates[i] > height: 
        raise ArithmeticError("Invalid Configuration File: {} contains a position that is out of map.".format(line_label)) 
      i += 2
    

    resource_coords = [] #initialising a new list for each resource, which contains all of the positions of that resource
    ls_forbidden_positions = [[1, 1], [width-2, height-2], [0, 1], [1, 0], [2, 1], [1, 2], [width-3, height-2], [width-2, height-3], [width-1, height-2], [width-2, height-1]]
    for each_elem in range(0, len(integer_coordinates), 2):
      
      # initialising a list of each coordinate pair, to then be added to the list of that resource's coordinates
      pair = [integer_coordinates[each_elem], integer_coordinates[each_elem + 1]] 
      resource_coords.append(pair)

      all_coordinates_duplicates_check.append(pair) #each pair is added to the list checking for duplicates
      for forbidden_positions in ls_forbidden_positions: 
        if pair == forbidden_positions: #if any of the pairs correspond to occupied positions, an error is raised as the file is invalid
          raise ValueError("Invalid Configuration File: The positions of home bases or the positions next to the home bases are occupied!")

    coords.append(resource_coords) #coords is now a multi-dimensional list, containing the lists of all of the resources
    

  for coordinates in all_coordinates_duplicates_check: 
      if all_coordinates_duplicates_check.count(coordinates) > 1: # if there are multiple instances of the same coordinate pair, an error is raised as the file is invalid
        raise SyntaxError("Invalid Configuration File: Duplicate position {}!".format(tuple(coordinates)))


  file_var.close()
  
  waters = coords[0] 
  woods = coords[1]
  foods = coords[2]
  golds = coords[3]
  return width, height, waters, woods, foods, golds 

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python3 little_battle.py <filepath>")
    sys.exit()

  
  width, height, waters, woods, foods, golds = load_config_file(sys.argv[1])
  player_1_home = [1, 1]
  player_2_home = [width-2, height-2]
  player1 = player("Player 1") # Player 1 is initialised as an object of the 'Player' class 
  player2 = player("Player 2") # Player 2 is initialised as an object of the 'Player' class 


  # The following block of code prints all of the game details 
  print("Configuration file {} was loaded.".format(sys.argv[1]))
  print("Game Started: Little Battle! (enter QUIT to quit the game)")
  print()
  gamemap = Frame(width, height) # gamemap is initialised as an object of the 'Frame' class
  gamemap.print_game_board()
  print("(enter DIS to display the map)")
  print()
  display_prices()
  print("(enter PRIS to display the price list)")


  game_finished = False
  year = 617 

  # the game starts with player 1's turn  
  current_player = player1
  alternate_player = player2

  while game_finished == False:

    # the following code prints the introductory message 
    print()
    print("-Year {}-".format(year))
    print()
    print("+++{}'s Stage: Recruit Armies+++".format(current_player.name))
    print()
    print("[Your Asset: Wood - {} Food - {} Gold - {}]".format(current_player.wood, current_player.food, current_player.gold))


    # ------------------------------------------ #

    # --------- RECRUIT ARMIES STAGE ----------- #

    # ------------------------------------------ #

    recruit_armies_finished = False
    while recruit_armies_finished == False: 

 
      # if insufficient resources to recruit any further units, skip the stage. 
      if current_player.check_sufficient_resources_spearman() == False and current_player.check_sufficient_resources_archer()== False and current_player.check_sufficient_resources_knight()== False and current_player.check_sufficient_resources_scout()== False: 
        print("No resources to recruit any armies.") 
        recruit_armies_finished = True
        break

      # if there are no available spaces to place units, skip the stage 
      elif len(current_player.unoccupied_positions) == 0:
        print("No place to recruit new armies.") 
        recruit_armies_finished = True
        break


      print()
      print("Which type of army to recruit, (enter) ‘S’, ‘A’, ‘K’, or ‘T’? Enter ‘NO’ to end this stage.")
      army = input()

      # checking for edge cases- the input is first checked to see if the user gave any commands, rather than recruiting an army 
      if army == 'QUIT': 
        game_finished = True
        recruit_armies_finished = True
        exit()
      if army == 'NO': 
        recruit_armies_finished = True
      elif army == 'PRIS': 
        display_prices()
      elif army == 'DIS': 
        gamemap.print_game_board()

      # ------ RECRUITING A SPEARMAN ------- # 

      elif army == 'S': 
        # edge case- if the player does not have the sufficient resources to recruit a spearman, they must try again 
        if current_player.check_sufficient_resources_spearman() == False:
          print("Insufficient resources. Try again.")
          continue   

        else:

          while True: 
            print() 
            print("You want to recruit a Spearman. Enter two integers as format ‘x y’ to place your army.")
            answer = input() 
            if check_for_quit_dis_or_prices(answer) == True: #checking for edge cases- users inputting commands 
                continue

            # The following try/except block checks for invalid input 
            try: 
              x, y = answer.split(' ')
              position = [int(x), int(y)]
              if position not in current_player.unoccupied_positions: # edge case- if the desired position is occupied or not next to the home base (including negative integers), an error is raised 
                raise SyntaxError 

            except SyntaxError: 
              print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
              continue

            except ValueError: #negative case- if the input was not 2 integers, an error is raised 
              print("Sorry, invalid input. Try again.")
              continue
            
    
            # If the recruitment position was valid, the player has made a successful recruitment 
            print() 
            print("You has recruited a Spearman.")              
            current_player.spearman.append(position)
            current_player.unoccupied_positions.remove(position) #the position they recruited to is now occupied by an army 
            print()
            
            # the cost is applied
            current_player.wood -= 1 
            current_player.food -= 1 

            print("[Your Asset: Wood - {} Food - {} Gold - {}]".format(current_player.wood, current_player.food, current_player.gold))
            break

      # ------ RECRUITING A ARCHER ------- # 

      elif army == 'A': 
        # edge case- if the player does not have sufficient resources to recruit an archer, they must try again
        if current_player.check_sufficient_resources_archer() == False:
          print("Insufficient resources. Try again.")
          continue 


        else:

           while True: 
            print() 
            print("You want to recruit a Archer. Enter two integers as format ‘x y’ to place your army.")
            answer = input() 
            if check_for_quit_dis_or_prices(answer) == True: #checking for edge cases- users inputting commands                  
              continue

            # the following try/except block checks for invalid input  
            try: 
              x, y = answer.split(' ')
              position = [int(x), int(y)]
              if position not in current_player.unoccupied_positions:  # edge case- if the desired position is occupied or not next to the home base (including negative integers), an error is raised
                raise SyntaxError

            except SyntaxError:
              print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")                
              continue

            except ValueError: #if the input was not 2 integers, an error is raised 
              print("Sorry, invalid input. Try again.")
              continue
              
              
            # If the recruitment position was valid, the player has made a successful recruitment 
            print() 
            print("You has recruited a Archer.")
            current_player.archer.append(position)
            current_player.unoccupied_positions.remove(position) #the position they recruited to is now occupied by an army
            print()
            
            # cost is applied 
            current_player.wood -= 1 
            current_player.gold -= 1 

            print("[Your Asset: Wood - {} Food - {} Gold - {}]".format(current_player.wood, current_player.food, current_player.gold))
            break

      # ------ RECRUITING A KNIGHT ------- #    

      elif army == 'K': 
        # edge case - if the player does not have the sufficient resources to recruit a knight, they must try again 
        if current_player.check_sufficient_resources_knight() == False:
          print("Insufficient resources. Try again.")
          continue   

        else:

           while True: 
            print() 
            print("You want to recruit a Knight. Enter two integers as format ‘x y’ to place your army.")
            answer = input() 
            if check_for_quit_dis_or_prices(answer) == True:  #checking for edge cases- users inputting commands
                continue 

            # the following try/except blocks for invalid input        
            try: 
              x, y = answer.split(' ')
              position = [int(x), int(y)]
              if position not in current_player.unoccupied_positions: # edge case- if the desired position is occupied or not next to the home base (including negative integers), an error is raised
                raise SyntaxError 

            except SyntaxError:
              print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")                
              continue

            except ValueError: # negative case- if the input was not 2 intergers, an error is raised
              print("Sorry, invalid input. Try again.")
              continue
            
            # if the recruitment position was valid, the player has made a successful recruitment 
            print() 
            print("You has recruited a Knight.")
            current_player.knight.append(position)
            current_player.unoccupied_positions.remove(position) # the position they recruited to is now occupied by an army
            print()

            #the cost is applied
            current_player.food -= 1 
            current_player.gold -= 1

            print("[Your Asset: Wood - {} Food - {} Gold - {}]".format(current_player.wood, current_player.food, current_player.gold))
            break
            
      # ------ RECRUITING A SCOUT ------- # 

      elif army == 'T': 
        # edge case - if the player does not have the sufficient resources to recruit a scout, they must try again
        if current_player.check_sufficient_resources_scout() == False:
          print("Insufficient resources. Try again.")
          continue 

        else:

          while True: 
            print() 
            print("You want to recruit a Scout. Enter two integers as format ‘x y’ to place your army.")
            answer = input()               
            if check_for_quit_dis_or_prices(answer) == True: #checking for edge cases- users inputting commands
                continue
            
            # the following try/except block checks for invalid input 
            try: 
              x, y = answer.split(' ')
              position = [int(x), int(y)]
              if position not in current_player.unoccupied_positions: # edge case- if the desired position is occupied or not next to the home base(including negative integers), an error is raised
                  raise SyntaxError 

            except SyntaxError:
              print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")                
              continue
            except ValueError: # negative case- if the input was not 2 integers, an error is raised 
              print("Sorry, invalid input. Try again.")
              continue


            # if the recruitment position was valid, the player has made a successful recruitment 
            print() 
            print("You has recruited a Scout.")
            current_player.scout.append(position)
            current_player.unoccupied_positions.remove(position) #the position they recruited to is now occupied by an army 
            print()
            
            #the cost is applied 
            current_player.wood -= 1 
            current_player.food -= 1 
            current_player.gold -= 1

            print("[Your Asset: Wood - {} Food - {} Gold - {}]".format(current_player.wood, current_player.food, current_player.gold))
            break
     
      # if the user input was not one of the aforementioned options, it is invalid 
      else: 
        print('Sorry, invalid input. Try again.')
        continue


    # ------------------------------------------ #

    # ----------- MOVE ARMIES STAGE ------------ #

    # ------------------------------------------ #


    print()
    print("==={}'s Stage: Move Armies===".format(current_player.name))

    # Copying the list ensures that the player cannot move the same army member twice in one turn. 
    moveable_spearmen = current_player.spearman.copy()
    moveable_archers = current_player.archer.copy() 
    moveable_knights= current_player.knight.copy()
    moveable_scouts = current_player.scout.copy()
    
    while True:
      print()

      # if no armies to move, skip this step
      if len(moveable_spearmen) == 0 and len(moveable_archers) == 0 and len(moveable_knights) == 0 and len(moveable_scouts) ==0: 
        print("No Army to Move: next turn.")
        armies_moving_finished = True
        break
      

      print("Armies to Move:")

      # the player's armies are printed depending on what they have recruited (and what they have already moved this turn)
      if len(moveable_spearmen) != 0: 
        print("  Spearman: {}".format(str(list(tuple(spearman_position) for spearman_position in moveable_spearmen))[1:-1]))
      if len(moveable_archers) != 0: 
        print("  Archer: {}".format(str(list(tuple(archer_position) for archer_position in moveable_archers))[1:-1]))
      if len(moveable_knights) != 0: 
        print("  Knight: {}".format(str(list(tuple(knight_position) for knight_position in moveable_knights))[1:-1]))
      if len(moveable_scouts) != 0: 
        print("  Scout: {}".format(str(list(tuple(scout_position) for scout_position in moveable_scouts))[1:-1]))
      

      print()
      print("Enter four integers as a format ‘x0 y0 x1 y1’ to represent move unit from (x0, y0) to (x1, y1) or ‘NO’ to end this turn.") 
      move = input()

      # checking for edge cases- users inputting commands
      if check_for_quit_dis_or_prices(move) == True: 
        continue
      elif move == 'NO':  
        break

      else: 
        # this try/except block checks for any invalid inputs 
        try: 
          x0, y0, x1, y1 = move.split(' ')
          initial_position = [int(x0), int(y0)]
          new_position = [int(x1), int(y1)]

          # if the new position is already occupied by the player's other armies (either in a move this turn or prior turns), input is invalid
          if new_position in current_player.spearman or new_position in current_player.archer or new_position in current_player.knight or new_position in current_player.scout: 
            raise ValueError
          if new_position in moveable_spearmen or new_position in moveable_archers or new_position in moveable_knights or new_position in moveable_scouts or new_position == current_player.base: 
            raise ValueError

          #if the initial position doesn't correspond to any of the armies, input is invalid 
          if initial_position not in moveable_spearmen and initial_position not in moveable_archers and initial_position not in moveable_knights and initial_position not in moveable_scouts: 
            raise ValueError

          # if the new position is out of the range of the map, input is invalid 
          elif new_position[0] > width-1 or new_position[0] < 0: 
            raise ValueError
          elif new_position[1] > height-1 or new_position[1] < 0: 
            raise ValueError
          
          # if the initial position is in scouts, the move must either be 1 or 2 steps in the same direction 
          if initial_position in moveable_scouts: 
            
            # if the x-coordinate has stayed the same, the y-coordinate must be 1 or 2 steps up or down 
            if new_position[0] == initial_position[0] and ((new_position[1] != (initial_position[1]+1) and (new_position[1] != (initial_position[1]-1))) and ((new_position[1] != (initial_position[1]+2) and (new_position[1] != initial_position[1]-2)))): 
              raise ValueError

            # if the y-coordinate has stayed the same, the x-coordinate must be 1 or 2 steps to the right or left
            elif new_position[1] == initial_position[1] and ((new_position[0] != (initial_position[0]+1) and (new_position[0] != (initial_position[0]-1))) and ((new_position[0] != (initial_position[0]+2) and (new_position[0] != initial_position[0]-2)))): 
              raise ValueError

            # if both x and y coordinate have changed, the scout has moved in more than one direction thus it is an invaild input 
            elif new_position[0] != initial_position[0] and new_position[1] != initial_position[1]: 
              raise ValueError

          else: #for all other armies, check that the new position is one to the left, right , up or down 
            
            # if x-coordinate has stayed the same, y-coordinate must be exactly 1 step up or down otherwise invalid
            if new_position[0] == initial_position[0] and (new_position[1] != (initial_position[1]+1) and new_position[1] != (initial_position[1]-1)): 
              raise ValueError
            
            # if y-coordinate has stayed the same, x-coordinate must be exactly 1 step right or left 
            elif new_position[1] == initial_position[1] and (new_position[0] != (initial_position[0]+1) and new_position[0] != (initial_position[0]-1)): 
              raise ValueError
            
            # if x and y have both changed, the army has moved in different directions thus the move is invalid 
            elif new_position[0] != initial_position[0] and new_position[1] != initial_position[1]: 
              raise ValueError
          
        except ValueError: #negative case- if the input is invalid, user must try again
          print("Invalid move. Try again.")
          continue

      # --- MOVING A SPEARMAN ----# 
      if initial_position in moveable_spearmen:

        # the move action is applied, and resources are collected
        moveable_spearmen.remove(initial_position) # this spearman can't be moved again this turn
        current_player.move_spearmen(initial_position, new_position)
        print()
        print("You have moved Spearman from {} to {}.".format(tuple(initial_position), tuple(new_position)))
        current_player.collect_resources(new_position)


        if new_position in waters or new_position in alternate_player.archer: 
          print("We lost the army Spearman due to your command!")
          current_player.spearman.remove(new_position) # The Spearman is removed from the current player's current armies because the spearman was defeated

          # If the spearman moved out of a home base surrounding position for either player, this position is now unoccupied and free for recruitment
          if initial_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(initial_position)
          elif initial_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.append(initial_position)
          

        elif new_position in alternate_player.knight:
          print("Great! We defeated the enemy Knight!")
          alternate_player.knight.remove(new_position) # The Knight is removed from the enemy's armies because the knight was defeated 
          
          # If the spearman moved out of a home base surrounding position for either player, this position is now unoccupied and free for recruitment
          if initial_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(initial_position)
          elif initial_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.append(initial_position) 

          # If the spearman moved into a home base surrounding position for either player, this position is now occupied, and not available for recruitment 
          if new_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.remove(new_position)
          elif new_position in alternate_player.surrounding_base: 
            alternate_player.unoccupied_positions.remove(new_position)


        elif new_position in alternate_player.scout: 
          print("Great! We defeated the enemy Scout!") 
          alternate_player.scout.remove(new_position) # The Scout is removed from the enemy's armies because the scout was defeated
         
          # If the spearman moved out of a home base surrounding position for either player, this position is now unoccupied and free for recruitment
          if initial_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(initial_position)
          elif initial_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.append(initial_position)
           
          # If the spearman moved into a home base surrounding position for either player, this position is now occupied and not available for recruitment
          if new_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.remove(new_position)
          elif new_position in alternate_player.surrounding_base: 
            alternate_player.unoccupied_positions.remove(new_position)
        

        elif new_position in alternate_player.spearman: 
          print("We destroyed the enemy Spearman with massive loss!")

          # Both Spearmans are removed from the current player and the enemy's armies because they defeated each other
          current_player.spearman.remove(new_position) 
          alternate_player.spearman.remove(new_position)

          # If the Spearman moved out of a home base surrounding position for either player, this position is now unoccupied and free for recruitment
          if initial_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(initial_position)
          elif initial_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.append(initial_position)

          # As both Spearmen died, if the position they died in was a home base surrounding position for either player, this position is now unoccupied and free for recruitment
          if new_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(new_position)
          elif new_position in alternate_player.surrounding_base: 
            alternate_player.unoccupied_positions.append(new_position)
          
        
        # --- CHECKING FOR WIN ---- # 
        #The following code checks to see if the army captured the enemy capital 
        elif new_position == alternate_player.base:
          print("The army Spearman captured the enemy’s capital.")
          print()
          print("What’s your name, commander?")
          name = input()
          print()
          print("***Congratulation! Emperor {} unified the country in {}.***".format(name, year))
          exit()

        
        #If the spearman did not encounter any armies or resources or win, the move is successful
        else: 

          # If the Spearman moves out of their player's home base surrounding position into another position on the map (surrounding neither home base), the initial position is unoccupied and can be recruited into  
          if initial_position in current_player.surrounding_base and (new_position not in current_player.surrounding_base and new_position not in alternate_player.surrounding_base): 
            current_player.unoccupied_positions.append(initial_position)

          # If the Spearman moves from a position in neither player's surrounding position, to one that is in their home base surrounding positions, this new position is now occupied and cannot be recruited into
          elif initial_position not in current_player.surrounding_base and initial_position not in current_player.surrounding_base and new_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.remove(new_position)
            
          # If the Spearman moves from a position in neither player's surrounding position, to one that is in their enemy's base surrounding positions, this new position is now occupied and cannot be recruited into 
          elif initial_position not in current_player.surrounding_base and initial_position not in alternate_player.surrounding_base and new_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.remove(new_position)
            
          #  If the Spearman moves out of their enemy's home base surrounding position into another position on the map (surrounding neither home base), the initial position is unoccupied and can be recruited into  
          elif initial_position in alternate_player.surrounding_base and new_position not in alternate_player.surrounding_base and new_position not in current_player.surrounding_base:         
            alternate_player.unoccupied_positions.append(initial_position)
            
          # The Spearman is unable to make any other combination of moves. 
 
      # --- MOVING AN ARCHER ----#
      elif initial_position in moveable_archers:

        # The move action is applied, and resources are collected
        moveable_archers.remove(initial_position) # This archer can't be moved again this turn 
        current_player.move_archer(initial_position, new_position)
        print()
        print("You have moved Archer from {} to {}.".format(tuple(initial_position), tuple(new_position)))
        current_player.collect_resources(new_position)


        if new_position in waters or new_position in alternate_player.knight: 
          print("We lost the army Archer due to your command!")
          current_player.archer.remove(new_position) # The Archer is removed from the current player's armies because the Archer was defeated  

          # If the Archer moved out of a home base surrounding position for either player, this position is now unoccupied and free for recruitment
          if initial_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(initial_position)
          elif initial_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.append(initial_position)

        elif new_position in alternate_player.spearman:
          print("Great! We defeated the enemy Spearman!")
          alternate_player.spearman.remove(new_position) # The Spearman is removed from the enemy's armies because the Spearman was defeated

          # If the Archer moved out of a home base surrounding position for either player, this position is now unoccupied and free for recruitment
          if initial_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(initial_position)
          elif initial_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.append(initial_position) 
          
          # If the Archer moved into a home base surrounding position for either player, this position is now occupied, and not available for recruitment
          if new_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.remove(new_position)
          elif new_position in alternate_player.surrounding_base: 
            alternate_player.unoccupied_positions.remove(new_position)

        elif new_position in alternate_player.scout: 
          print("Great! We defeated the enemy Scout!")
          alternate_player.scout.remove(new_position) # The Scout is removed from the enemy's armies because the scout was defeated
          
          # If the Archer moved out of a home base surrounding position for either player, this position is now unoccupied and free for recruitment 
          if initial_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(initial_position)
          elif initial_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.append(initial_position) 
          
          # If the Archer moves into a home base surrounding position for either player, this position is now occupied and not available for recruitment 
          if new_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.remove(new_position)
          elif new_position in alternate_player.surrounding_base: 
            alternate_player.unoccupied_positions.remove(new_position)

        elif new_position in alternate_player.archer: 
          print("We destroyed the enemy Archer with massive loss!")
          
          # The Archers are removed from both the current player and enemy player's armies as they defeated each other
          current_player.archer.remove(new_position)
          alternate_player.archer.remove(new_position)

          #If the Archer moved out of a home base surrounding position for either player, this position is now unoccupied and free for recruitment
          if initial_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(initial_position)
          elif initial_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.append(initial_position) 
          
          # As both Archers died, if the position they died in was a home base surrounding position for either player, this position is now unoccupied and free for recruitment  
          if new_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(new_position)
          elif new_position in alternate_player.surrounding_base: 
            alternate_player.unoccupied_positions.append(new_position)
        

        # --- CHECKING FOR WIN ---# 
        # The following code checks to see if the army captured the enemy capital
        elif new_position == alternate_player.base:
          print("The army Archer captured the enemy’s capital.")
          print()
          print("What’s your name, commander?")
          name = input()
          print()
          print("***Congratulation! Emperor {} unified the country in {}.***".format(name, year))
          exit() 
        

        # If the Archer did not encounter any armies or resources or win, the move is successful
        else: 
          # If the Archer moves out of their player's home base surrounding position into another position on the map (surrounding neither home base), the initial position is unoccupied and can be recruited into 
          if initial_position in current_player.surrounding_base and (new_position not in current_player.surrounding_base and new_position not in alternate_player.surrounding_base): 
            current_player.unoccupied_positions.append(initial_position)
        
          # If the Archer moves from a position in neither player's surrounding position, to one that is in their home base surrounding positions, this new position is now occupied and cannot be recruited into
          elif initial_position not in current_player.surrounding_base and initial_position not in current_player.surrounding_base and new_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.remove(new_position)
            
          # If the Archer moves from a position in neither player's surrounding position, to one that is in their enemy's base surrounding positions, this new position is now occupied and cannot be recruited into 
          elif initial_position not in current_player.surrounding_base and initial_position not in alternate_player.surrounding_base and new_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.remove(new_position)
            
          #  If the Archer moves out of their enemy's home base surrounding position into another position on the map (surrounding neither home base), the initial position is unoccupied and can be recruited into 
          elif initial_position in alternate_player.surrounding_base and new_position not in alternate_player.surrounding_base and new_position not in current_player.surrounding_base:         
            alternate_player.unoccupied_positions.append(initial_position)
            
          # The Archer is unable to make any other combination of moves. 

      # ---MOVING A KNIGHT ---#
      elif initial_position in moveable_knights: 
        # The move action is applied, and resources are collected
        moveable_knights.remove(initial_position) # This knight can't be moved again this turn
        current_player.move_knight(initial_position, new_position)
        print()
        print("You have moved Knight from {} to {}.".format(tuple(initial_position), tuple(new_position)))
        current_player.collect_resources(new_position)



        if new_position in waters or new_position in alternate_player.spearman: 
          print("We lost the army Knight due to your command!")
          current_player.knight.remove(new_position) # The Knight is removed from the current player's armies because the knight was defeated 
          
          # If the Knight moved out of a home base surrounding position for either player, this position is now unoccupied and free for recruitment 
          if initial_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(initial_position)
          elif initial_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.append(initial_position)

        elif new_position in alternate_player.archer:
          print("Great! We defeated the enemy Archer!")
          alternate_player.archer.remove(new_position) # The Archer is removed from the enemy's armies because the Archer was defeated

          # If the Knight moved out of a home base surrounding position for either player, this position is now unoccupied and free for recruitment 
          if initial_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(initial_position)
          elif initial_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.append(initial_position) 
          
          # If the Knight moved into a home base surrounding position for either player, this position is now occupied, and not available for recruitment
          if new_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.remove(new_position)
          elif new_position in alternate_player.surrounding_base: 
            alternate_player.unoccupied_positions.remove(new_position)

        elif new_position in alternate_player.scout: 
          print("Great! We defeated the enemy Scout!") 
          alternate_player.scout.remove(new_position) # The Scout is removed from the enemy's armies because the scout was defeated
          
          # If the Knight moved out of a home base surrounding position for either player, this position is now unoccupied and free for recruitment 
          if initial_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(initial_position)
          elif initial_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.append(initial_position) 
          
          # If the Knight moves into a home base surrounding position for either player, this position is now occupied and not available for recruitment 
          if new_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.remove(new_position)
          elif new_position in alternate_player.surrounding_base: 
            alternate_player.unoccupied_positions.remove(new_position)
        
        elif new_position in alternate_player.knight: 
          print("We destroyed the enemy Knight with massive loss!")
          
          # The Knights are removed from both the current player and enemy player's armies as they defeated each other
          current_player.knight.remove(new_position)
          alternate_player.knight.remove(new_position)

          #If the Knight moved out of a home base surrounding position for either player, this position is now unoccupied and free for recruitment
          if initial_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(initial_position)
          elif initial_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.append(initial_position) 
          
          # As both Knights died, if the position they died in was a home base surrounding position for either player, this position is now unoccupied and free for recruitment  
          if new_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(new_position)
          elif new_position in alternate_player.surrounding_base: 
            alternate_player.unoccupied_positions.append(new_position)
  
        # --- CHECKING FOR WIN ---# 
        # The following code checks to see if the army captured the enemy capital
        elif new_position == alternate_player.base: 
          print("The army Knight captured the enemy’s capital.")
          print()
          print("What’s your name, commander?")
          name = input()
          print()
          print("***Congratulation! Emperor {} unified the ocuntry in {}.***".format(name, year))
          quit()
        
        # If the Knight did not encounter any armies or resources or win, the move is successful
        else: 
          # If the Knight moves out of their player's home base surrounding position into another position on the map (surrounding neither home base), the initial position is unoccupied and can be recruited into 
          if initial_position in current_player.surrounding_base and (new_position not in current_player.surrounding_base and new_position not in alternate_player.surrounding_base): 
            current_player.unoccupied_positions.append(initial_position)
        
          # If the Knight moves from a position in neither player's surrounding position, to one that is in their home base surrounding positions, this new position is now occupied and cannot be recruited into
          elif initial_position not in current_player.surrounding_base and initial_position not in current_player.surrounding_base and new_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.remove(new_position)
            
          # If the Knight moves from a position in neither player's surrounding position, to one that is in their enemy's base surrounding positions, this new position is now occupied and cannot be recruited into 
          elif initial_position not in current_player.surrounding_base and initial_position not in alternate_player.surrounding_base and new_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.remove(new_position)
            
          #  If the Knight moves out of their enemy's home base surrounding position into another position on the map (surrounding neither home base), the initial position is unoccupied and can be recruited into 
          elif initial_position in alternate_player.surrounding_base and new_position not in alternate_player.surrounding_base and new_position not in current_player.surrounding_base:         
            alternate_player.unoccupied_positions.append(initial_position)
            
          # The Knight is unable to make any other combination of moves. 

      # ---- MOVING A SCOUT --- #
      elif initial_position in moveable_scouts: 
        # the move action is applied
        moveable_scouts.remove(initial_position)
        current_player.move_scout(initial_position, new_position)
        print()
        print("You have moved Scout from {} to {}.".format(tuple(initial_position), tuple(new_position)))

        # if the scout has moved two steps in the same direction, the correct actions must be applied for its 'intermediary position', or the one it passed
        if len(current_player.scout_intermediary_positions) > 0: 

          # if the scout passed wood, it collects wood 
          if current_player.scout_intermediary_positions[0] in woods:
            woods.remove(current_player.scout_intermediary_positions[0])
            current_player.wood += 2 
            print("Good. We collected 2 Wood.")

          # if the scout passed food, it collects food
          elif current_player.scout_intermediary_positions[0] in foods:
            foods.remove(current_player.scout_intermediary_positions[0])
            current_player.food += 2
            print("Good. We collected 2 Food.")
          
          # if the scout passed gold, it collects gold
          elif current_player.scout_intermediary_positions[0] in golds:
            golds.remove(current_player.scout_intermediary_positions[0])
            current_player.gold += 2
            print("Good. We collected 2 Gold.")

          # if the scout passed water or an enemy spearman, archer or knight, it is defeated 
          elif current_player.scout_intermediary_positions[0] in waters or current_player.scout_intermediary_positions[0] in alternate_player.spearman or current_player.scout_intermediary_positions[0] in alternate_player.archer or current_player.scout_intermediary_positions[0] in alternate_player.knight:
            print("We lost the army Scout due to your command!")
            current_player.scout.remove(new_position) # The Scout is removed from the current player's armies because the Scout was defeated

            # if the Scout moved out of a home base surrounding position for either player, this position is now unoccupied and free for recruitment 
            if initial_position in current_player.surrounding_base: 
              current_player.unoccupied_positions.append(initial_position)
            elif initial_position in alternate_player.surrounding_base:
              alternate_player.unoccupied_positions.append(initial_position)

            #The intermediary position is reset as this will update for each individual scout move
            # the next stage is skipped because the scout died before it could reach its next position
            current_player.scout_intermediary_positions.pop(0)  
            continue 
        
          # if the Scout passed an enemy Scout, both Scouts are defeated
          elif current_player.scout_intermediary_positions[0] in alternate_player.scout: 
            print("We destroyed the enemy Scout with massive loss!")

            # The Scout is removed from the current player's armies because the Scout was defeated
            # The enemy Scout at this position is removed from the enemy player's armies because it was also defeated
            current_player.scout.remove(new_position)
            alternate_player.scout.remove(current_player.scout_intermediary_positions[0])
            
            # If the Scout moved out of a home base surrounding position for either player, this position is now unoccupied and free for recruitment 
            if initial_position in current_player.surrounding_base: 
              current_player.unoccupied_positions.append(initial_position)
            elif initial_position in alternate_player.surrounding_base:
              alternate_player.unoccupied_positions.append(initial_position)
            
            # As both Scouts died, if the position they died in was a home base surrounding position for either player, this position is now unoccupied and free for recruitment 
            if current_player.scout_intermediary_positions[0] in current_player.surrounding_base:
              current_player.unoccupied_positions.append(current_player.scout_intermediary_positions[0])
            elif current_player.scout_intermediary_positions[0] in alternate_player.surrounding_base:
              alternate_player.unoccupied_positions.append(current_player.scout_intermediary_positions[0])
            
            #The intermediary position is reset as this will update for each individual scout move
            # the next stage is skipped because the scout died before it could reach its next position
            current_player.scout_intermediary_positions.pop(0)
            continue 


          # ----- CHECK FOR WIN ----- #
          # If the Scout passed over the enemy's capital, the player wins 
          elif current_player.scout_intermediary_positions[0] == alternate_player.base:
            print("The army Scout captured the enemy’s capital.")
            print()
            print("What’s your name, commander?")
            name = input()
            print()
            print("***Congratulation! Emperor {} unified the country in {}.***".format(name, year))
            exit()
        
          # the intermediary position will update for every scout move, therefore it must be reset at the end of each scout move 
          current_player.scout_intermediary_positions.pop(0)


        # If the Scout survived passing through its intermediary position, it collects the resources for its new position
        current_player.collect_resources(new_position)

        if new_position in waters or new_position in alternate_player.knight or new_position in alternate_player.spearman or new_position in alternate_player.archer: 
          print("We lost the army Scout due to your command!")
          current_player.scout.remove(new_position) # The Scout is removed from the current player's armies because the Scout was defeated
          
          # If the Scout moved out of a home base surrounding position for either player, this position is now unoccupied and free for recruitment 
          if initial_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(initial_position)
          elif initial_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.append(initial_position)
        
        elif new_position in alternate_player.scout: 
          print("We destroyed the enemy Scout with massive loss!")

          # The Scouts are removed from both the current player and enemy player's armies as they defeated each other
          current_player.scout.remove(new_position)
          alternate_player.scout.remove(new_position)

          # If the Scout moved out of a home base surrounding position for either player, this position is now unoccupied and free for recruitment 
          if initial_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(initial_position)
          elif initial_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.append(initial_position) 
          
          # As both Scouts died, if the position they died in was a home base surrounding position for either player, this position is now unoccupied and free for recruitment
          if new_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(new_position)
          elif new_position in alternate_player.surrounding_base: 
            alternate_player.unoccupied_positions.append(new_position)
        
        # --- CHECKING FOR WIN ---# 
        # The following code checks to see if the army captured the enemy capital
        elif new_position == alternate_player.base: 
          print("The army Scout captured the enemy’s capital.")
          print()
          print("What’s your name, commander?")
          name = input()
          print()
          print("***Congratulation! Emperor {} unified the country in {}.***".format(name, year))
          exit()

        # If the Scout did not encounter any armies or resources or win, the move is successful
        else: 
          # If the Scout moved out of their player's home base surrounding position into another position on the map (surrounding neither home base), the initial position is unoccupied and can be recruited into  
          if initial_position in current_player.surrounding_base and (new_position not in current_player.surrounding_base and new_position not in alternate_player.surrounding_base): 
            current_player.unoccupied_positions.append(initial_position)

          # If the Scout moved out of their player's home base surrounding position into another position surrounding their home base, the intial position is unoccupied (and free for recruitment) while the new position is occupied and unavailable for recruitment 
          # This move behaviour is unique to the Scout 
          elif initial_position in current_player.surrounding_base and new_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.append(initial_position)
            current_player.unoccupied_positions.remove(new_position)
            
          # If the Scout moved out of their player's home base surrounding position into another position surrounding their enemy's home base, the intial position is unoccupied (and free for recruitment) while the new position is occupied and unavailable for recruitment
          # This move behaviour is unique to the Scout  
          elif initial_position in current_player.surrounding_base and new_position in alternate_player.surrounding_base: 
            current_player.unoccupied_positions.append(initial_position)
            alternate_player.unoccupied_positions.remove(new_position)
 
          # If the Scout moves from a position in neither player's surrounding position, to one that is in their home base surrounding positions, this new position is now occupied and cannot be recruited into
          elif initial_position not in current_player.surrounding_base and initial_position not in current_player.surrounding_base and new_position in current_player.surrounding_base: 
            current_player.unoccupied_positions.remove(new_position)
            
          # If the Scout moves from a position in neither player's surrounding position, to one that is in their enemy's base surrounding positions, this new position is now occupied and cannot be recruited into 
          elif initial_position not in current_player.surrounding_base and initial_position not in alternate_player.surrounding_base and new_position in alternate_player.surrounding_base:
            alternate_player.unoccupied_positions.remove(new_position)
             
          #  If the Scout moves out of their enemy's home base surrounding position into another position on the map (surrounding neither home base), the initial position is unoccupied and can be recruited into 
          elif initial_position in alternate_player.surrounding_base and new_position not in alternate_player.surrounding_base and new_position not in current_player.surrounding_base:         
            alternate_player.unoccupied_positions.append(initial_position)
             
          # If the Scout moves out of their enemy's home base surrounding position, to one that is in their home base surrounding position, the initial position is now unoccupied and can be recruited into while the new position is occupied and cannot be recruited into
          # This move behaviour is unique to the Scout
          elif initial_position in alternate_player.surrounding_base and new_position in current_player.surrounding_base: 
            alternate_player.unoccupied_positions.append(initial_position)
            current_player.unoccupied_positions.remove(new_position)
            
          # If the Scout moves out of their enemy's home base surrounding position, to one that is in enemy's home base surrounding position, the initial position is now unoccupied and can be recruited into while the new position is occupied and cannot be recruited into
          # This move behaviour is unique to the Scout
          elif initial_position in alternate_player.surrounding_base and new_position in alternate_player.surrounding_base: 
            alternate_player.unoccupied_positions.append(initial_position)
            alternate_player.unoccupied_positions.remove(new_position)


    # Once the turn is finished, the players switch
    if current_player == player1: 
      current_player = player2
      alternate_player = player1
    elif current_player == player2: 
      current_player = player1
      alternate_player = player2  
      year += 1 # the year increments by one after player 2's turns