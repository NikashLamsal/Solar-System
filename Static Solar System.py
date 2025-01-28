import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mid-Point Ellipse Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)


def draw_ellipse_algorithm(xc, yc, rx, ry):
    x = 0
    y = ry
    p1 = (ry**2) - (rx**2 * ry) + (0.25 * (rx**2))
    dx = 2 * (ry**2) * x
    dy = 2 * (rx**2) * y

    # First region
    while dx <= dy:
        screen.set_at((round(x + xc), round(y + yc)), WHITE)
        screen.set_at((round(-x + xc), round(y + yc)), WHITE)
        screen.set_at((round(x + xc), round(-y + yc)), WHITE)
        screen.set_at((round(-x + xc), round(-y + yc)), WHITE)

        if p1 < 0:
            x += 1
            dx = 2 * (ry**2) * x
            p1 += dx + (ry**2)
        else:
            x += 1
            y -= 1
            dx = 2 * (ry**2) * x
            dy = 2 * (rx**2) * y
            p1 += dx - dy + (ry**2)

    p2 = (ry**2) * (x + 0.5)**2 + (rx**2) * (y - 1)**2 - (rx**2) * (ry**2)

    # Second region
    while y > 0:
        screen.set_at((round(x + xc), round(y + yc)), WHITE)
        screen.set_at((round(-x + xc), round(y + yc)), WHITE)
        screen.set_at((round(x + xc), round(-y + yc)), WHITE)
        screen.set_at((round(-x + xc), round(-y + yc)), WHITE)

        if p2 > 0:
            y -= 1
            dy = 2 * (rx**2) * y
            p2 -= dy + (rx**2)
        else:
            x += 1
            y -= 1
            dx = 2 * (ry**2) * x
            dy = 2 * (rx**2) * y
            p2 += dx - dy + (rx**2)

# Function to draw circles (planets and sun)
def draw_circle_algorithm(x, y, r, color):
    X = 0
    Y = r
    d = 1 - r
    while X <= Y:
        screen.set_at((round(X + x), round(Y + y)), color)
        screen.set_at((round(Y + x), round(X + y)), color)
        screen.set_at((round(-Y + x), round(X + y)), color)
        screen.set_at((round(-X + x), round(Y + y)), color)
        screen.set_at((round(-X + x), round(-Y + y)), color)
        screen.set_at((round(-Y + x), round(-X + y)), color)
        screen.set_at((round(Y + x), round(-X + y)), color)
        screen.set_at((round(X + x), round(-Y + y)), color)
        X += 1
        if d < 0:
            d += 2 * X + 1
        else:
            d += 2 * X - 2 * Y + 1
            Y -= 1

# Main function
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # Sun
        for radius in range(30, 0, -1):
            draw_circle_algorithm(400, 300, radius, YELLOW)


        draw_ellipse_algorithm(400, 300, 60, 40)  # Mercury
        draw_ellipse_algorithm(400, 300, 100, 70)  # Venus
        draw_ellipse_algorithm(400, 300, 150, 100)  # Earth
        draw_ellipse_algorithm(400, 300, 200, 140)  # Mars
        draw_ellipse_algorithm(400, 300, 260, 180)  # Jupiter
        draw_ellipse_algorithm(400, 300, 320, 220)  # Saturn
        draw_ellipse_algorithm(400, 300, 380, 260)  # Uranus
        draw_ellipse_algorithm(400, 300, 440, 300)  # Neptune


        # Mercury
        for radius in range(5, 0, -1):
            draw_circle_algorithm(460, 300, radius, RED)

        # Venus
        for radius in range(7, 0, -1):
            draw_circle_algorithm(500, 300, radius, ORANGE)

        # Earth
        for radius in range(9, 0, -1):
            draw_circle_algorithm(550, 300, radius, BLUE)

        # Mars
        for radius in range(8, 0, -1):
            draw_circle_algorithm(600, 300, radius, GREEN)

        # Jupiter
        for radius in range(12, 0, -1):
            draw_circle_algorithm(660, 300, radius, PURPLE)

        # Saturn
        for radius in range(10, 0, -1):
            draw_circle_algorithm(720, 300, radius, ORANGE)

        # Uranus
        for radius in range(8, 0, -1):
            draw_circle_algorithm(780, 300, radius, WHITE)

        # Neptune
        for radius in range(7, 0, -1):
            draw_circle_algorithm(840, 300, radius, BLUE)

        pygame.display.flip()

if __name__ == "__main__":
    main()
