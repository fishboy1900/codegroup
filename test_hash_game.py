from hash_game import main, winner, valid_move, hash_board
import pytest


@pytest.fixture( params=[
    {"input": [[1,1,1],[0,2,0],[0,0,2]], "expectedResult" : True},
    {"input": [[1,0,0],[1,0,2],[1,2,0]], "expectedResult" : True},
    {"input": [[1,2,0],[2,1,0],[0,0,1]], "expectedResult" : True},
    {"input": [[0,2,1],[0,1,2],[1,0,0]], "expectedResult" : True},
    {"input": [[1,2,2],[1,2,2],[2,1,0]], "expectedResult" : True},
    {"input": [[0,0,0],[0,0,0],[0,0,0]], "expectedResult" : False},
    {"input": [[0,1,0],[2,0,2],[0,1,0]], "expectedResult" : False},
    {"input": [[1,0,0],[0,2,0],[0,0,1]], "expectedResult" : False},
    {"input": [[1,2,1],[1,2,2],[2,1,1]], "expectedResult" : False},
    {"input": [[1,2,2],[2,1,1],[1,1,2]], "expectedResult" : False}])

def testCase(request):
    return request.param

def test_winner(testCase):
    result = winner(testCase["input"])
    assert result == testCase["expectedResult"]