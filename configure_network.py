import subprocess
import os
import ctypes
import sys
import time

INTERFACE_NAME = "Wi-Fi"  # Change to the correct name if it's not "Wi-Fi"

def is_admin():
    """Checks if the script is being run as administrator."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def restart_as_admin():
    """Restarts the script as administrator."""
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )

def set_static_ip():
    print(f"Configuring static IP for interface: {INTERFACE_NAME}...")
    try:
        subprocess.run([
            "netsh", "interface", "ip", "set", "address",
            f"name={INTERFACE_NAME}",
            "source=static",
            "addr=[your ip]",
            "mask=[your mask]",
            "gateway=[your gateway]"
        ], check=True)

        time.sleep(2)

        subprocess.run([
            "netsh", "interface", "ip", "set", "dns",
            f"name={INTERFACE_NAME}",
            "source=static",
            "addr=8.8.8.8"
        ], check=True)
        
        subprocess.run([
            "netsh", "interface", "ip", "add", "dns",
            f"name={INTERFACE_NAME}",
            "addr=8.8.4.4",
            "index=2"
        ], check=True)

        print("Static IP configuration completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error configuring static IP: {e}")

def set_dynamic_ip():
    print(f"Configuring dynamic IP for interface: {INTERFACE_NAME}...")
    try:
        subprocess.run([
            "netsh", "interface", "ip", "set", "address",
            f"name={INTERFACE_NAME}",
            "source=dhcp"
        ], check=True)
        
        subprocess.run([
            "netsh", "interface", "ip", "set", "dns",
            f"name={INTERFACE_NAME}",
            "source=dhcp"
        ], check=True)
        
        print("Dynamic IP configuration completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error configuring dynamic IP: {e}")

def main():
    if not is_admin():
        print("This script requires administrator privileges. Restarting...")
        restart_as_admin()
        sys.exit()
    
    print("=== Network Configuration Manager ===")
    print("1. Configure IP and DNS automatically")
    print("2. Configure IP and DNS manually")
    print("============================================")
    
    try:
        choice = int(input("Choose an option (1 or 2): "))
        if choice == 1:
            set_dynamic_ip()
        elif choice == 2:
            set_static_ip()
        else:
            print("Invalid option. Please choose 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()