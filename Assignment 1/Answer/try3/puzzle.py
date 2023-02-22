def read_state(filename):
    with open(filename) as f:
        lines = f.readlines()
        state = [[int(x) for x in line.split()] for line in lines if line.strip() != "END OF FILE"]
    return state

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)

def move(state, action):
    i, j = find_blank(state)
    new_state = [row[:] for row in state]
    if action == "Up":
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
    elif action == "Down":
        new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
    elif action == "Left":
        new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
    elif action == "Right":
        new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
    return new_state

def actions(state):
    actions = []
    i, j = find_blank(state)
    if i > 0:
        actions.append("Up")
    if i < 2:
        actions.append("Down")
    if j > 0:
        actions.append("Left")
    if j < 2:
        actions.append("Right")
    return actions

def goal_test(state, goal):
    return state == goal
