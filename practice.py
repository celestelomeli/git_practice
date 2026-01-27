# This function receives user input for "name" and prints out a greeting plus user input


def main():
	
	name = input("Enter your name: ").strip()
	
	print(f"Hello, {name}!")
	print(f"How are you, {name}?")

if __name__ == "__main__":
    main()

