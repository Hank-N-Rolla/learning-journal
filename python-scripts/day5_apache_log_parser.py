from collections import Counter

def extract_ips(log_path):
    ip_counter = Counter()
    try:
        with open(log_path, 'r') as log_file:
            for line in log_file:
                parts = line.split()
                if parts:
                    ip = parts[0]
                    ip_counter[ip] += 1
    except FileNotFoundError:
        print(f"[!] File not found: {log_path}")
        return

    print("\n--- Apache Log Summary ---")
    print(f"Total Requests: {sum(ip_counter.values())}")
    print(f"Unique IPs: {len(ip_counter)}")

    print("\nTop 5 IPs by Request Count:")
    for ip, count in ip_counter.most_common(5):
        print(f"{ip} → {count} requests")

if __name__ == "__main__":
    log_file = input("Enter the path to access.log: ").strip()
    extract_ips(log_file)
