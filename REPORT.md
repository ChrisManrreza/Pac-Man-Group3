Team Contributions Report:

- Chris Manrreza (Leader) Implemented the Player feature player.py
tests test_player.py. Reviewed teammate PRs and managed overall branch coordination.

- Nihar Chegireddy Implemented the Game_Board feature gameboard.py tests test_gameboard.py. 

- Jacob Kang Implemented the Ghost feature ghost.py, created test file and tested using test_ghost.py. 
Implemented the item feature item.py, created test file and tested using test_item.py. 
Identified bug in ghost.py and fixed it. Reviewed teammate PRs.

Accidentally commented the code:
#def __init__(self, x, y, color):

Consequently, failed all tests:
test_ghost.py::test_ghost_initialization 
test_ghost.py::test_ghost_move_without_collision 
test_ghost.py::test_ghost_collision_with_wall 
test_ghost.py::test_ghost_scared_state
test_ghost.py::test_ghost_draw

Fixed by uncommenting it:
def __init__(self, x, y, color):

Now, passed all tests:
test_ghost.py::test_ghost_initialization PASSED
test_ghost.py::test_ghost_move_without_collision PASSED
test_ghost.py::test_ghost_collision_with_wall PASSED
test_ghost.py::test_ghost_scared_state PASSED
test_ghost.py::test_ghost_draw PASSED

- Lokesh NOTHING
