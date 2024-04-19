import pygame
import random

# Define constants
WIDTH = 400
HEIGHT = 400
GRID_SIZE = 10
SPEED = 10
BLACK = (0, 0, 0)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


class Grid:
    @staticmethod
    def draw():
        for x in range(0, WIDTH, GRID_SIZE):
            for y in range(0, HEIGHT, GRID_SIZE):
                rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(screen, BLACK, rect, 1)


class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.dx, self.dy = GRID_SIZE, 0

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.dx, head_y + self.dy)
        self.body.pop()
        self.body.insert(0, new_head)

    def change_direction(self, new_dx, new_dy):
        self.dx, self.dy = new_dx, new_dy

    def eat_food(self, food):
        self.body.insert(0, food)

    def collided_with_self(self):
        return self.body[0] in self.body[1:]

    def out_of_bounds(self):
        head_x, head_y = self.body[0]
        return head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT

    def draw(self):
        for pos in self.body:
            rect = pygame.Rect(pos[0], pos[1], GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, GREEN, rect)


class Food:
    def __init__(self):
        self.position = self.random_position()
        self.weight = self.random_weight()

    @staticmethod
    def random_position():
        x = random.randint(0, WIDTH - GRID_SIZE)
        y = random.randint(0, HEIGHT - GRID_SIZE)
        return x // GRID_SIZE * GRID_SIZE, y // GRID_SIZE * GRID_SIZE

    @staticmethod
    def random_weight():
        return random.randint(50, 200)

    def update_position(self):
        self.position = self.random_position()
        self.weight = self.random_weight()

    def draw(self):
        rect = pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE)
        food_color = (255 - self.weight, 0, self.weight)
        pygame.draw.rect(screen, food_color, rect)


def main():
    snake = Snake()
    food = Food()
    score = 0
    level = 1
    timer = 0
    disappearing_food = False

    # Game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.dx == 0:
                    snake.change_direction(-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake.dx == 0:
                    snake.change_direction(GRID_SIZE, 0)
                elif event.key == pygame.K_UP and snake.dy == 0:
                    snake.change_direction(0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN and snake.dy == 0:
                    snake.change_direction(0, GRID_SIZE)

        # Move snake
        snake.move()

        # Check for collisions
        if snake.body[0] == food.position:
            snake.eat_food(food.position)
            score += food.weight
            food.update_position()
            timer = 0
            disappearing_food = False
            if score % 50 == 0:
                level += 1
        elif snake.out_of_bounds() or snake.collided_with_self():
            running = False

        # Spawn disappearing food
        timer += 1
        if timer == 100:
            timer = 0
            if not disappearing_food:
                food.update_position()
                disappearing_food = True
            else:
                disappearing_food = False

        # Draw game objects
        screen.fill(LIGHT_GRAY)
        screen.fill(BLACK)
        Grid.draw()
        snake.draw()
        food.draw()
        pygame.display.update()

        # Set game speed based on level
        clock.tick(SPEED + level * 2)

    # Display game over message
    font = pygame.font.SysFont(None, 30)
    text = font.render(f"Game Over - Score: {score}", True, RED)
    screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(3000)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()