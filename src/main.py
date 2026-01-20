#!/usr/bin/env python3
"""
Rock Paper Scissors

A small CLI game to practice:
- input validation
- control flow
- simple game state (score tracking)
"""

from __future__ import annotations

import random
from dataclasses import dataclass


ROCK = "r"
PAPER = "p"
SCISSORS = "s"

EMOJIS = {ROCK: "🪨", PAPER: "📃", SCISSORS: "✂️"}
CHOICES = (ROCK, PAPER, SCISSORS)


@dataclass
class Score:
    wins: int = 0
    losses: int = 0
    ties: int = 0


def ask_yes_no(prompt: str) -> bool:
    while True:
        ans = input(prompt).strip().lower()
        if ans in {"y", "yes"}:
            return True
        if ans in {"n", "no"}:
            return False
        print("Please answer with 'y' or 'n'.")


def get_user_choice() -> str:
    while True:
        user_choice = input("Rock, paper, or scissors? (r/p/s): ").strip().lower()
        if user_choice in CHOICES:
            return user_choice
        print("Invalid choice. Please enter r, p, or s.")


def display_choices(user_choice: str, computer_choice: str) -> None:
    print(f"You chose:      {EMOJIS[user_choice]}")
    print(f"Computer chose: {EMOJIS[computer_choice]}")


def determine_result(user_choice: str, computer_choice: str) -> str:
    if user_choice == computer_choice:
        return "tie"
    if (
        (user_choice == ROCK and computer_choice == SCISSORS)
        or (user_choice == SCISSORS and computer_choice == PAPER)
        or (user_choice == PAPER and computer_choice == ROCK)
    ):
        return "win"
    return "loss"


def update_score(score: Score, result: str) -> None:
    if result == "win":
        score.wins += 1
    elif result == "loss":
        score.losses += 1
    else:
        score.ties += 1


def print_score(score: Score) -> None:
    print(f"Score — Wins: {score.wins} | Losses: {score.losses} | Ties: {score.ties}")


def main() -> None:
    print("=== Rock Paper Scissors ===\n")
    score = Score()

    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(CHOICES)

        print()
        display_choices(user_choice, computer_choice)

        result = determine_result(user_choice, computer_choice)
        update_score(score, result)

        if result == "win":
            print("✅ You win!")
        elif result == "loss":
            print("❌ You lose!")
        else:
            print("🤝 It's a tie!")

        print_score(score)
        print()

        if not ask_yes_no("Play another round? (y/n): "):
            break
        print()

    print("\nThanks for playing!")
    print_score(score)


if __name__ == "__main__":
    main()
