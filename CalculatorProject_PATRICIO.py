import time
import os

# Initialize a global history list
history = []

def clear_screen():
    """Clear the console screen for a clean look."""
    os.system("cls" if os.name == "nt" else "clear")

def digital_loader(message="Loading"):
    """Simulates a loading effect for better digital design."""
    for _ in range(3):
        print(f"{message}{'.' * (_ + 1)}", end="\r", flush=True)
        time.sleep(0.4)
    print(f"{message}... Done!")

def print_header(title):
    """Displays a stylized header with ASCII art."""
    clear_screen()
    print("\n" + "=" * 60)
    print(f"{'⚡ NUMBER PROCESSING TERMINAL ⚡'.center(60)}")
    print("=" * 60)
    print(f"\n{title.center(60)}\n")
    print("-" * 60)

def delayed_print(label, value):
    """Prints a result with a delay for effect."""
    time.sleep(0.8)
    print(f"  ➡ {label:<20} {value}")

def display_history():
    """Displays the history of inputs and results."""
    print_header("📜 History of Sessions")
    if not history:
        print("No previous sessions found. Start analyzing numbers!")
    else:
        for idx, session in enumerate(history, start=1):
            print(f"Session {idx}:")
            delayed_print("Numbers Entered:", ', '.join(map(str, session['numbers'])))
            delayed_print("Total Sum:", session['total_sum'])
            delayed_print("Even Count:", session['even_count'])
            delayed_print("Sum of Evens:", session['even_sum'])
            delayed_print("Odd Count:", session['odd_count'])
            delayed_print("Sum of Odds:", session['odd_sum'])
            print("-" * 60)
            time.sleep(1)
    input("\nPress Enter to return to the main menu...")

def process_numbers():
    """Process numbers entered by the user and display results."""
    while True:
        print_header("Welcome to the Digital Processor")
        
        # Create an empty list to store the numbers
        numbers = []
        
        # Ask the user to input 5 numbers
        print("🔢 Input 5 numbers to analyze:")
        for i in range(5):
            while True:
                try:
                    num = int(input(f"  ➡ Enter Number {i + 1}: "))
                    break
                except ValueError:
                    print("     [❌ ERROR] Please enter a valid integer.")
            numbers.append(num)
        
        # Display a loading effect before showing results
        digital_loader("Processing numbers")
        
        # Compute the sum of all numbers in the list
        total_sum = sum(numbers)
        
        # Count the number of odd and even numbers
        odd_count, even_count = 0, 0
        odd_sum, even_sum = 0, 0
        
        for num in numbers:
            if num % 2 == 0:
                even_count += 1
                even_sum += num
            else:
                odd_count += 1
                odd_sum += num
        
        # Display the results with delays
        print_header("Processing Complete")
        print("📜 Results Summary:")
        delayed_print("Numbers Entered:", ', '.join(map(str, numbers)))
        delayed_print("Total Sum:", total_sum)
        delayed_print("Even Count:", even_count)
        delayed_print("Sum of Evens:", even_sum)
        delayed_print("Odd Count:", odd_count)
        delayed_print("Sum of Odds:", odd_sum)
        print("-" * 60)
        
        # Save the results in the history
        session_data = {
            "numbers": numbers,
            "total_sum": total_sum,
            "even_count": even_count,
            "even_sum": even_sum,
            "odd_count": odd_count,
            "odd_sum": odd_sum,
        }
        history.append(session_data)
        
        # Ask the user if they want to continue inputting numbers
        print("\n🔄 Would you like to:")
        print("  1. Input another set of numbers")
        print("  2. Return to the Main Menu")
        choice = input("➡ Enter your choice [1-2]: ").strip()
        
        if choice == '1':
            digital_loader("Reloading for new input")
        elif choice == '2':
            print("Returning to Main Menu...")
            time.sleep(1)
            break
        else:
            print("[❌ ERROR] Invalid choice. Returning to Main Menu.")
            time.sleep(1)
            break

# Main program loop with options
while True:
    print_header("MAIN MENU")
    print("Select an option:")
    print("  1. Analyze Numbers")
    print("  2. View History")
    print("  3. Exit")
    
    choice = input("\n➡ Enter your choice [1-3]: ").strip()
    
    if choice == '1':
        process_numbers()
    elif choice == '2':
        display_history()
    elif choice == '3':
        print_header("Thank You!")
        print("💻 Exiting the Number Processing Terminal. See you next time!")
        break
    else:
        print("\n[❌ ERROR] Invalid choice. Please select a valid option.")
        time.sleep(2)