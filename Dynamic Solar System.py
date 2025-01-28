import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" Our Solar System ")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)

planets = [
    {"color": RED, "radius": 8, "orbit_radius_x": 50, "orbit_radius_y": 30, "speed": 0.05},
    {"color": ORANGE, "radius": 10, "orbit_radius_x": 100, "orbit_radius_y": 60, "speed": 0.03},
    {"color": BLUE, "radius": 12, "orbit_radius_x": 150, "orbit_radius_y": 90, "speed": 0.02},
    {"color": GREEN, "radius": 14, "orbit_radius_x": 200, "orbit_radius_y": 120, "speed": 0.01},
    {"color": PURPLE, "radius": 16, "orbit_radius_x": 250, "orbit_radius_y": 150, "speed": 0.008},
    {"color": CYAN, "radius": 18, "orbit_radius_x": 300, "orbit_radius_y": 180, "speed": 0.006},
]

SUN_COLOR = YELLOW
SUN_RADIUS = 30

def draw_circle(x, y, radius, color):
    pygame.draw.circle(screen, color, (round(x), round(y)), radius)

def draw_orbit(xc, yc, rx, ry, color):
    for angle in range(0, 360):
        theta = math.radians(angle)
        x = xc + rx * math.cos(theta)
        y = yc + ry * math.sin(theta)
        screen.set_at((round(x), round(y)), color)

def main():
    clock = pygame.time.Clock()
    t = 0  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        draw_circle(WIDTH // 2, HEIGHT // 2, SUN_RADIUS, SUN_COLOR)

        for planet in planets:
            draw_orbit(WIDTH // 2, HEIGHT // 2, planet["orbit_radius_x"], planet["orbit_radius_y"], WHITE)

            angle = t * planet["speed"]
            x = WIDTH // 2 + planet["orbit_radius_x"] * math.cos(angle)
            y = HEIGHT // 2 + planet["orbit_radius_y"] * math.sin(angle)

            draw_circle(x, y, planet["radius"], planet["color"])

        pygame.display.flip()

        t += 1
        clock.tick(60)  

if __name__ == "__main__":
    main()
