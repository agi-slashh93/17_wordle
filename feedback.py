def evaluate(target, guess):
    result = ["gray"] * len(guess)
    remaining = {}

    # Mark greens and count unmatched target letters.
    for i, ch in enumerate(target):
        if ch == guess[i]:
            result[i] = "green"
        else:
            remaining[ch] = remaining.get(ch, 0) + 1

    # Use each remaining target copy for at most one yellow.
    for i, ch in enumerate(guess):
        if result[i] == "green":
            continue
        if remaining.get(ch, 0) > 0:
            result[i] = "yellow"
            remaining[ch] -= 1

    return result