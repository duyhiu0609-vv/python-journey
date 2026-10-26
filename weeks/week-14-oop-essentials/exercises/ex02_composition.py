"""Exercise 02: compose Bot with a strategy."""

from collections.abc import Callable

State = dict[str, int]
Strategy = Callable[[State], str]


class Bot:
    """A bot delegates its decision to a replaceable strategy."""

    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def choose_action(self, state: State) -> str:
        return self.strategy(state)


def move_toward_goal(state: State) -> str:
    """Return one step toward the goal, supporting goals on either side."""
    position = state["position"]
    goal = state["goal"]

    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def defensive(state: State) -> str:
    """Wait when the opponent is adjacent; otherwise move toward the goal."""
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state: State) -> str:
    """Use a steady, direct movement strategy."""
    return move_toward_goal(state)


def aggressive(state: State) -> str:
    """Move directly toward the goal."""
    return move_toward_goal(state)


if __name__ == "__main__":
    state = {"position": 1, "opponent_position": 4, "goal": 4}

    for strategy in (defensive, balanced, aggressive):
        bot = Bot(strategy)
        print(f"{strategy.__name__}: {bot.choose_action(state)}")

    # Strategy can be changed without changing the Bot class.
    bot = Bot(balanced)
    print("Before:", bot.choose_action(state))
    bot.strategy = defensive
    print("After:", bot.choose_action(state))
