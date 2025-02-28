import pytest

from jupyter_assignment import READ_INTRODUCTION, LEARNED_ABOUT_JUPYTER, ACCESS_COLABORATORY, CREATED_GITHUB_ACCOUNT, github_username, my_name, greet

from matplotlib_assignment import Student_ID, task_id, my_function

import os


score = 0.0


def test_read_introduction():
    global score
    assert READ_INTRODUCTION == True, "Please, read the instruction!"
    score += 0.05
    # print(f"Score is {score}")


def test_learn_jupyter():
    global score
    assert LEARNED_ABOUT_JUPYTER == True, "Please, learn about Jupyter!"
    score += 0.05
    # print(f"Score is {score}")


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
    request.addfinalizer(print_score)
# def pytest_report_header(config):
#     return f"Score is {score}"
    
# print(f"Score is {score}")
