print("You arrive at a digital gate in the firewall...")
print("Two paths lie ahead: 'scan' or 'brute force'. Choose wisely.")

choice = input("What do you do? ").lower()

if choice == "scan":
    print("You scan the ports and find a hidden SSH backdoor. Smart move!")
elif choice == "brute force":
    print("Security alarms triggered! You've been flagged by the system!")
else:
    print("You hesitate, and the system logs your indecision. Time's up.")
