SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
ASTEROID_SPEED_MODIFIER = 1.2

PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200

SHOT_RADIUS = 5
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3

# colors
BLACK = (0, 0, 0)
COLOR_PALETTES = [
    # small meteor  , mid meteor     , big meteor
    [(122, 115, 209), (77, 85, 204)  , (33, 28, 132)  ], # shades of blue: https://colorhunt.co/palette/211c844d55cc7a73d1b5a8d5
    [(255, 137, 137), (248, 237, 140), (137, 172, 70) ], # red, yellow, green: https://colorhunt.co/palette/89ac46d3e671f8ed8cff8989
    [(255, 247, 243), (250, 208, 196), (197, 153, 182)], # pastel: https://colorhunt.co/palette/c599b6e6b2bafad0c4fff7f3
    [(233, 118, 43) , (65, 100, 74)  , (241, 240, 233)], # orange, green, white: https://colorhunt.co/palette/f1f0e941644a0d4715e9762b
]
COLOR_INDEX = 3