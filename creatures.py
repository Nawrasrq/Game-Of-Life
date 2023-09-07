import numpy as np

# Block
BLOCK = np.array([[255, 255],
                  [255, 255]])

# Blinker
BLINKER = np.array([[255, 255, 255]])

# Glider
GLIDER = np.array([[0, 0, 255],
                   [255, 0, 255],
                   [0, 255, 255]])

# Gosper glider gun
gun = np.zeros(11 * 38).reshape(11, 38)

gun[5][1] = gun[5][2] = 255
gun[6][1] = gun[6][2] = 255

gun[3][13] = gun[3][14] = 255
gun[4][12] = gun[4][16] = 255
gun[5][11] = gun[5][17] = 255
gun[6][11] = gun[6][15] = gun[6][17] = gun[6][18] = 255
gun[7][11] = gun[7][17] = 255
gun[8][12] = gun[8][16] = 255
gun[9][13] = gun[9][14] = 255

gun[1][25] = 255
gun[2][23] = gun[2][25] = 255
gun[3][21] = gun[3][22] = 255
gun[4][21] = gun[4][22] = 255
gun[5][21] = gun[5][22] = 255
gun[6][23] = gun[6][25] = 255
gun[7][25] = 255

gun[3][35] = gun[3][36] = 255
gun[4][35] = gun[4][36] = 255
