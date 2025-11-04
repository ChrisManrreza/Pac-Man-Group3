import pygame
import pytest
from gameboard import GameBoard  # adjust if your file name differs


@pytest.fixture(scope="module", autouse=True)

#Initialize and quit pygame for all tests.
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()

#Ensure the GameBoard initializes with expected elements
def test_setup_maze_creates_walls_and_pellets():
    
    board = GameBoard()

    # Basic sanity checks
    assert board.width == 800
    assert board.height == 600
    assert len(board.walls) > 0, "No walls created"
    assert len(board.pellets) > 0, "No pellets created"
    assert len(board.power_pellets) == 4, "Should have 4 power pellets"

    # Check power pellet positions (corner placement)
    expected_positions = {(50, 50), (750, 50), (50, 550), (750, 550)}
    actual_positions = {(p.x, p.y) for p in board.power_pellets}
    assert actual_positions == expected_positions


# Make sure draw method runs without error
def test_draw_runs_without_error():
    board = GameBoard()
    screen = pygame.Surface((board.width, board.height))

    try:
        board.draw(screen)
    except Exception as e:
        pytest.fail(f"draw() raised an exception: {e}")
