def main():
    print("You are in a dark room. You can go left or right.")
    choice = input("Which way? (left/right):").lower()
    if choice == "left":
        print("You found a treasure!.")
    else:
        print("A monster appears! ⛄ Game over,")

if __name__ == "__main__":
    main()