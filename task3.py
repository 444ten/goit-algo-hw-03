
def move_disk(source, target, rods):
    disk = rods[source].pop()
    rods[target].append(disk)

    print(f"Move disk from {source} to {target}: {disk}")
    print(f"Intermediate state: {rods}")

def hanoi(n, a, b, c, rods):
    """
    Recursive function to solve Towers of Hanoi.
    
    n         - number of disks to move
    a    - source      rod (e.g., 'A')
    b - helper      rod (e.g., 'B')
    c    - destination rod (e.g., 'C')
    
    rods      - dictionary holding the current state of disks
    """
    if n == 1:
        # Base case: Just move one disk directly
        move_disk(a, c, rods)
    else:
        # Step 1: Move n-1 disks from Source to Auxiliary (using Target as buffer)
        hanoi(n - 1, a, c, b, rods)
        
        # Step 2: Move the nth (largest) disk from Source to Target
        move_disk(a, c, rods)
        
        # Step 3: Move n-1 disks from Auxiliary to Target (using Source as buffer)
        hanoi(n - 1, b, a, c, rods)

def main():
    try:
        n_input = input("Enter the number of disks: ")
        n = int(n_input)
        
        if n < 1:
            print("Please enter a positive integer.")
            return

        rods = {
            'A': list(range(n, 0, -1)),
            'B': [],
            'C': []
        }

        print(f"Initial state: {rods}")
        
        hanoi(n, 'A', 'B', 'C', rods)
        
        print(f"Final state: {rods}")

    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
