import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


# --- check_guess ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_hint_says_go_lower():
    # Bug was: hint said "Go HIGHER!" when guess was too high
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_hint_says_go_higher():
    # Bug was: hint said "Go LOWER!" when guess was too low
    _, message = check_guess(40, 50)
    assert "HIGHER" in message


# --- get_range_for_difficulty ---

def test_hard_range_is_wider_than_normal():
    # Bug was: Hard returned 1–50, making it easier than Normal (1–100)
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 100

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 200


# --- update_score ---

def test_win_increases_score():
    new_score = update_score(0, "Win", attempt_number=1)
    assert new_score > 0

def test_too_high_decreases_score():
    # Bug was: on even attempts, "Too High" gave +5 instead of -5
    score_odd = update_score(100, "Too High", attempt_number=1)
    score_even = update_score(100, "Too High", attempt_number=2)
    assert score_odd < 100
    assert score_even < 100

def test_too_low_decreases_score():
    new_score = update_score(100, "Too Low", attempt_number=1)
    assert new_score < 100


# --- parse_guess ---

def test_parse_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert err == "Enter a guess."

def test_parse_none():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert err == "Enter a guess."

def test_parse_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert err == "That is not a number."

def test_parse_float_string():
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7
