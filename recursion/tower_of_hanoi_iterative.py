import userin # Contains input querying functions

# Global variables
g_init_tower_height = 0
g_init_tower_start = 0
g_init_tower_target = 0

# Initalizes the the variable that holds values in the different towers.
def init_towers():
    global g_tower_matrix  # Defines g_tower_matrix as global

    # Creates a global 2d list with 3 towers
    tower_count, height = 2, 0
    g_tower_matrix = [[0 for x in range(height)] for y in range(tower_count)]

    # Fill the matrix with the first tower from the bottom up
    for height in range(g_init_tower_height):
        print ( g_init_tower_height - height )
        g_tower_matrix[g_init_tower_start].append(g_init_tower_height - height)

# Explain program and get initial user input
def init_program ():
    # Allows the global variables to be modified.
    global g_init_tower_height
    global g_init_tower_start
    global g_init_tower_target

    init_message = ("This program is meant to give you instructions on how "
                    "to solve an n height, tower of hanoi puzzle. \n")

    print( init_message )

    g_init_tower_height = userin.get_user_int("How tall is the initial tower?")

    print( ("\n"
            "        |   |   |\n"
            "        |   |   |\n"
            "        0___1___2\n"
            "Example of Tower of Hanoi.\n") )

    g_init_tower_start = userin.get_user_int("Which position does the tower start in?", 0, 2)

    g_init_tower_target = userin.get_user_int("Which position is the tower being moved into?", 0, 2)

    init_towers()

def get_value_from_tower(depth_value, tower_number):
    pass  #TODO: get value from matrix

def solve_problem():
    pass  #TODO: solution loop

init_program()

solve_problem()

print( "Done! ^^ " )
