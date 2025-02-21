import subprocess
import os
import ctypes
import sys
import time

INTERFACE_NAME = "Wi-Fi"  # Alterar para o nome correto caso não seja "Wi-Fi"

def is_admin():
    """Verifica se o script está sendo executado como administrador."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def restart_as_admin():
    """Reinicia o script como administrador."""
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )

def set_static_ip():
    print(f"Configurando IP estático para a interface: {INTERFACE_NAME}...")
    try:
        subprocess.run([
            "netsh", "interface", "ip", "set", "address",
            f"name={INTERFACE_NAME}",
            "source=static",
            "addr=[your ip]",
            "mask=[your mask]",
            "gateway=1[your gateway]"
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

        print("Configuração de IP estático concluída com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao configurar IP estático: {e}")

def set_dynamic_ip():
    print(f"Configurando IP dinâmico para a interface: {INTERFACE_NAME}...")
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
        
        print("Configuração de IP dinâmico concluída com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao configurar IP dinâmico: {e}")

def main():
    if not is_admin():
        print("Este script precisa de privilégios de administrador. Reiniciando...")
        restart_as_admin()
        sys.exit()
    
    print("=== Gerenciador de Configurações de Rede ===")
    print("1. Configurar IP e DNS automaticamente")
    print("2. Configurar IP e DNS manualmente")
    print("============================================")
    
    try:
        choice = int(input("Escolha uma opção (1 ou 2): "))
        if choice == 1:
            set_dynamic_ip()
        elif choice == 2:
            set_static_ip()
        else:
            print("Opção inválida. Por favor, escolha 1 ou 2.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")

if __name__ == "__main__":
    main()
