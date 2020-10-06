from hash_game import main, winner, valid_move, hash_board
import pytest


def test_winner():
    tabs =( 
        ([[1,1,1],[0,2,0],[0,0,2]], True),
        ([[1,0,0],[1,0,2],[1,2,0]], True),
        ([[1,2,0],[2,1,0],[0,0,1]], True),
        ([[0,2,1],[0,1,2],[1,0,0]], True),
        ([[1,2,2],[1,2,2],[2,1,0]], True),
        ([[0,0,0],[0,0,0],[0,0,0]], False),
        ([[0,1,0],[2,0,2],[0,1,0]], False),
        ([[1,0,0],[0,2,0],[0,0,1]], False),
        ([[1,2,1],[1,2,2],[2,1,1]], False),
        ([[1,2,2],[2,1,1],[1,1,2]], False)
        )

    for (tab, end) in tabs:

        assert winner(tab) == end

test_winner()