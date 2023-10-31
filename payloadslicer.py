def main():
    payload = input("Input your payload here: ")

    try:
        vrble = input("Enter the variable name [Str is Default]: ")
        variable = str(vrble) if vrble else 'Str'
    except ValueError:
        print("Invalid input. Using default variable name 'Str'")
        variable = "Str"
        
    # Get padding number with default as 50
    try:
        padding = input("Enter the padding number [50 is default]: ")
        n = int(padding) if padding else 50
    except ValueError:
        print("Invalid input. Using default padding of 50.")
        n = 50

    # Print the payload in chunks
    for i in range(0, len(payload), n):
        print(f'{variable} = {variable} + "{payload[i:i+n]}"')

if __name__ == "__main__":
    main()
