import requests
import os
import time

def print_banner():
    print("""\033[95m
██╗░░██╗███████╗██╗░░░██╗███╗░░██╗
██║░░██║╚════██║╚██╗░██╔╝████╗░██║
███████║░░░░██╔╝░╚████╔╝░██╔██╗██║
██╔══██║░░░██╔╝░░░╚██╔╝░░██║╚████║
██║░░██║░░██╔╝░░░░░██║░░░██║░╚███║
╚═╝░░╚═╝░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚══╝
    >> H7yn ONION SCANNER v1.6 <<
\033[0m""")

def check_onion(url, port):
    proxies = {
        'http': f'socks5h://127.0.0.1:{port}',
        'https': f'socks5h://127.0.0.1:{port}'
    }
    
    try:
        response = requests.get(url, proxies=proxies, timeout=30)
        if response.status_code == 200:
            return "ONLINE"
        return f"ERR {response.status_code}"
    except Exception:
        return "OFFLINE"

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()

    if not os.path.exists("links.txt"):
        print("\033[91m[!] Error: 'links.txt' not found in this folder.\033[0m")
        return

    port = 9150 
    
    with open("links.txt", "r") as f:
        links = [line.strip() for line in f if line.strip()]

    print(f"[*] Port: {port} | Targets: {len(links)}\n")

    results = []
    for link in links:
        print(f"[*] Checking: {link[:30]}...", end="\r")
        status = check_onion(link, port)
        
        color = "\033[92m" if status == "ONLINE" else "\033[91m"
        print(f"{color}[{status}]\033[0m - {link}")
        
        results.append(f"{link} | {status}")
        time.sleep(0.5)

    with open("scan_report.txt", "w") as f:
        f.write("\n".join(results))

    print(f"\n\033[95m[*] Scan Complete. Results saved to 'scan_report.txt'\033[0m")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()