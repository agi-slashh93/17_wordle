from game import WordleGame


if __name__ == "__main__":
    while True:
        choice = input("Choose word length (4, 5, or 6), or q to quit: ").strip().lower()

        if choice == "q":
            break

        if choice not in {"4", "5", "6"}:
            print("Enter 4, 5, or 6.")
            continue

        WordleGame(length=int(choice)).run()
        break