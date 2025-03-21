import pytest

from jupyter_assignment import READ_INTRODUCTION, LEARNED_ABOUT_JUPYTER, ACCESS_COLABORATORY, CREATED_GITHUB_ACCOUNT, github_username, my_name, greet

from matplotlib_assignment import Student_ID, task_id, my_function, dot_product

# from pandas_assignment import dataset_id, columns, answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8

import os


score = 0.0


def test_read_introduction():
    global score
    assert READ_INTRODUCTION == True, "Please, read the instruction!"
    score += 0.05


def test_learn_jupyter():
    global score
    assert LEARNED_ABOUT_JUPYTER == True, "Please, learn about Jupyter!"
    score += 0.05


def test_access_colaboratory():
    global score
    assert ACCESS_COLABORATORY == True, "Please, configure Google Colab!"
    score += 0.05


def test_create_github():
    global score
    assert CREATED_GITHUB_ACCOUNT == True, "Please, create a GitHub Account!"
    score += 0.05
    

def test_greet():
    global score
    assert greet(my_name) == f"Hello, {my_name}!"
    assert greet("Test User") == "Hello, Test User!"
    score += 0.2


def test_github():
    # print(os.getenv('GITHUB_REPOSITORY'))
    # print(github_username)
    assert os.getenv('GITHUB_REPOSITORY', '').endswith(github_username), f"Your GitHub username doesn't match. Did you forget to update 'github_username' variable or are you trying to cheat by submitting someone else's work?"


def test_student_id():
    if Student_ID is not None:
        assert Student_ID > 0 and Student_ID < 100, "Invalid Student ID!"


def test_task_id():
    if Student_ID is not None:
        assert task_id > 0 and task_id <= 25, "Invalid task ID!"


def test_maths():
    if Student_ID is not None:
        import numpy as np
        import math
        if task_id == 1:
            assert my_function(np.array([1]),1,1,1,1) == 4
            assert my_function(np.array([2]),2,2,2,2) == 78
        elif task_id == 2:
            assert math.isclose(my_function(np.array([0]),2,2,0,0), 0)
            assert math.isclose(my_function(np.array([0]),2,2,0,-10), 0)


def test_dot_product():
    answers = [
        13550, 16870, 8137, 13145, 14620, 8880, 5371, 15377, 3292, 13487, 8604, 7911, 11224, 20706, 
        11852, 8611, 5489, 14160, 18076, 15480, 11748, 11954, 15400, 17489, 14071, 10334, 12960, 
        13837, 6484, 4829, 13419, 9578, 16590, 18355, 10887, 18960, 10665, 12946, 20941, 14179, 11574
    ]
    assert dot_product == answers[Student_ID], "Invalid value of dot product!"
    

# def test_dataset_id():
#     if Student_ID is not None:
#         assert dataset_id >= 0 and task_id < 3, "Invalid dataset ID!"


# def test_columns():
#     from collections.abc import Iterable
#     assert isinstance(columns, Iterable)
#     for col in columns:
#         assert isinstance(col, str), f"Column {col} has invalid type!"
#         assert col.islower()


# def test_answers():
#     assert answer1 not in [None, ...]
#     assert answer2 not in [None, ...]
#     assert answer3 not in [None, ...]
#     assert answer4 not in [None, ...]
#     assert answer5 not in [None, ...]
#     assert answer6 not in [None, ...]
#     assert answer7 not in [None, ...]
#     assert answer8 not in [None, ...]


@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    def print_score():
        global score
        if greet(3.14) == "Hello, 3.14!" and greet(42) == "Hello, 42!":
            score += 0.1
        if greet(['Alice']) == "Hello, Alice!":
            score += 0.1
        if greet(['Alice', 'Bob', 'Charlie']) == "Hello, Alice, Bob and Charlie!":
            score += 0.2
        if greet(['Alice', 3.14, {'key'}]) == "Hello, Alice, 3.14 and {'key'}!":
            score += 0.2
        print(f"\nScore is {score}")
        print(f"TASKID is {Student_ID}")
    request.addfinalizer(print_score)
