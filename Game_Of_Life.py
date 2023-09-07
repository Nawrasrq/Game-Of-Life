import random
import creatures
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Cell states
LIVE = 255
DEAD = 0

# Generates an empty grid
def empty_grid(size):
    return np.zeros(size*size).reshape(size, size)

# Generates a random grid
def random_grid(size):
    return np.random.choice([LIVE, DEAD], size * size, p=[0.1, 0.9]).reshape(size, size)

# Adds an amount of blocks randomly
def add_blocks(grid, size, amount):
    if size <= 3:
        return

    for i in range(0, amount):
        i = random.randrange(0, size-3)
        j = random.randrange(0, size-3)
        grid[i:i + 2, j:j + 2] = creatures.BLOCK

# Adds an amount of blinkers randomly
def add_blinkers(grid, size, amount):
    if size <= 4:
        return

    for i in range(0, amount):
        i = random.randrange(0, size-2)
        j = random.randrange(0, size-4)
        grid[i:i+1, j:j + 3] = creatures.BLINKER

# Adds an amount of gliders randomly
def add_gliders(grid, size, amount):
    if size <= 4:
        return

    for i in range(0, amount):
        i = random.randrange(0, size-4)
        j = random.randrange(0, size-4)
        grid[i:i + 3, j:j + 3] = creatures.GLIDER

# Adds an amount of gosper glider guns randomly
def add_gosper_gg(grid, size, amount):
    if size <= 39:
        return

    for i in range(0, amount):
        i = random.randrange(0, size-12)
        j = random.randrange(0, size-39)
        grid[i:i + 11, j:j + 38] = creatures.gun

# Update cells
def update(frame_num, img, grid, size):
    new_grid = np.array(grid, copy=True)

    for i in range(size):
        for j in range(size):
            # Compute the 8-neighbor sum
            total_neighbor = (int((grid[i, (j - 1) % size] + grid[i, (j + 1) % size] +  # Left and right cells
                         grid[(i - 1) % size, j] + grid[(i + 1) % size, j] +  # Top and bottom cells
                         grid[(i - 1) % size, (j - 1) % size] + grid[(i - 1) % size, (j + 1) % size] +  # Top-diagonal
                         grid[(i + 1) % size, (j - 1) % size] + grid[(i + 1) % size, (j + 1) % size]  # Bottom-diagonal
                         ) / 255))

            # Conway's rules
            if grid[i, j] == LIVE:
                if (total_neighbor < 2) or (total_neighbor > 3):
                    new_grid[i, j] = DEAD
            else:
                if total_neighbor == 3:
                    new_grid[i, j] = LIVE

    # update cells
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,

def main():
    # Grid settings
    size = 100
    interval = 50

    # Initialize grid
    grid = np.array([])
    # grid = random_grid(size)
    grid = empty_grid(size)

    # Add some creatures
    add_gliders(grid, size, 10)
    add_gosper_gg(grid, size, 2)
    add_blocks(grid, size, 10)
    add_blinkers(grid, size, 5)

    # Initialize plot and animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig,
                                  update,
                                  fargs=(img, grid, size,),
                                  interval=interval,
                                  save_count=50)
    plt.show()

if __name__ == '__main__':
    main()
