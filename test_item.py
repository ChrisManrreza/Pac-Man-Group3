import pytest
import pygame
from item import Pellet, PowerPellet


@pytest.fixture(scope="module", autouse=True)
def init_pygame():
    """Initialize pygame before running tests"""
    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    yield screen
    pygame.quit()


def test_pellet_initialization():
    pellet = Pellet(10, 20)
    assert pellet.x == 10
    assert pellet.y == 20
    assert pellet.radius == 2
    assert not pellet.collected


def test_power_pellet_initialization():
    power = PowerPellet(50, 60)
    assert power.x == 50
    assert power.y == 60
    assert power.radius == 8
    assert not power.collected


def test_collect_behavior():
    pellet = Pellet(10, 10)
    power = PowerPellet(20, 20)

    pellet.collected = True
    power.collected = True

    assert pellet.collected
    assert power.collected
