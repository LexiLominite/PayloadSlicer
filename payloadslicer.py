def main():
    payload = input("Input your payload here: ")

    # Get padding number with default as 50
    try:
        padding = input("Enter the padding number [50 is default]: ")
        n = int(padding) if padding else 50
    except ValueError:
        print("Invalid input. Using default padding of 50.")
        n = 50

    # Print the payload in chunks
    for i in range(0, len(payload), n):
        print("Str = Str + " + '"' + payload[i:i+n] + '"')

if __name__ == "__main__":
    main()
