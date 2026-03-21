from utils import add, substract

def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print("Sum:", add(x, y))
    print("Substraction", substract(x, y))

if __name__ == "__main__":
    main()