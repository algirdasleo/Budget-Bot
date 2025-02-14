import pytest
import os
from helpers import file_helper

def test_find_existing_file():
    assert file_helper.find_file("data/keywords.csv") == os.path.exists("data/keywords.csv")

def test_find_non_existing_file():
    assert file_helper.find_file("data/non_existing.csv") == False
