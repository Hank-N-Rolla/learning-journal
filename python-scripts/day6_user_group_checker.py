import subprocess

def check_user_info(username):
    try:
        result = subprocess.run(["net", "user", username], capture_output=True, text=True, shell=True)
        output = result.stdout

        if "The user name could not be found" in output:
            print(f"[!] User '{username}' not found.")
            return

        print("\n--- User Info ---")
        print(output)

        # Extract specific details
        lines = output.splitlines()
        for line in lines:
            if "Local Group Memberships" in line or "Global Group memberships" in line:
                print(f"[*] {line.strip()}")
            if "Account active" in line:
                print(f"[*] {line.strip()}")
            if "Password required" in line:
                print(f"[*] {line.strip()}")

    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    username = input("Enter the Windows username to check: ").strip()
    check_user_info(username)
