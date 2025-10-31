import pytest
import pygame
from ghost import Ghost

class MockPlayer:
    def __init__(self, x, y):
        self.x = x
        self.y = y


@pytest.fixture
def walls():
    return [
        pygame.Rect(0, 0, 20, 600),     # Left wall
        pygame.Rect(780, 0, 20, 600),   # Right wall
        pygame.Rect(200, 200, 20, 20),  # Small obstacle
    ]


@pytest.fixture
def player():
    return MockPlayer(100, 100)


@pytest.fixture
def ghost():
    return Ghost(50, 50, (255, 0, 0))


def test_ghost_initialization(ghost):
    assert ghost.x == 50
    assert ghost.y == 50
    assert ghost.color == (255, 0, 0)
    assert ghost.speed == 1
    assert ghost.radius == 10
    assert ghost.direction in ["right", "left", "up", "down"]
    assert not ghost.scared
    assert ghost.scared_timer == 0


def test_ghost_move_without_collision(ghost, walls, player):
    # Move ghost toward player (100,100)
    ghost.x, ghost.y = 50, 50
    old_x, old_y = ghost.x, ghost.y
    ghost.direction = "right"
    ghost.move(walls, player)
    # Ghost should move by its speed to the right
    assert ghost.x in (old_x + ghost.speed, old_x - ghost.speed, old_x)
    assert isinstance(ghost.y, int)


def test_ghost_collision_with_wall(ghost, walls, player):
    # Place ghost right next to left wall and move left
    ghost.x = 25
    ghost.y = 100
    ghost.direction = "left"
    ghost.move(walls, player)
    # Should not move through wall (still roughly same x)
    assert ghost.x >= 25 - ghost.radius

    # Place ghost near obstacle and move right
    ghost.x = 190
    ghost.y = 210
    ghost.direction = "right"
    prev_x = ghost.x
    ghost.move(walls, player)
    # Should not move through obstacle
    assert ghost.x == prev_x or ghost.x < 200


def test_ghost_scared_state(ghost, walls, player):
    ghost.scared = True
    ghost.scared_timer = 2
    old_x, old_y = ghost.x, ghost.y

    # Move twice, should decrement timer
    ghost.move(walls, player)
    assert ghost.scared_timer == 1
    ghost.move(walls, player)
    assert ghost.scared_timer == 0
    assert not ghost.scared  # timer expired → no longer scared


def test_ghost_draw(ghost):
    # Just check that it runs without error
    screen = pygame.Surface((200, 200))
    ghost.draw(screen)
    assert True  # If no pygame error occurs, pass
