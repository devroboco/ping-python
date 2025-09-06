import os

def ping_host(host):
    print(f"Pinging {host}...")
    response = os.system(f"ping -n 4 {host}")
    if response == 0:
        print(f"{host} está acessível.")
    else:
        print(f"{host} não está acessível.")

if __name__ == "__main__":
    alvo = input("Digite o IP ou domínio que deseja testar: ")
    ping_host(alvo)