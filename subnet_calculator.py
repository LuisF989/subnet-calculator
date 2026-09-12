import ipaddress
import sys

def calculate_subnet(ip_cidr: str):
    try:
        network = ipaddress.IPv4Network(ip_cidr, strict=False)
        host = ipaddress.IPv4Interface(ip_cidr)

        print("\n" + "=" * 50)
        print(f"   RESULTADOS PARA: {ip_cidr}")
        print("=" * 50)
        print(f"  Dirección IP ingresada : {host.ip}")
        print(f"  Máscara de Red         : {network.netmask}")
        print(f"  Máscara Wildcard       : {network.hostmask}")
        print(f"  Notación CIDR          : /{network.prefixlen}")
        print("-" * 50)
        print(f"  Dirección de Red       : {network.network_address}")
        print(f"  Dirección Broadcast    : {network.broadcast_address}")
        print(f"  Primera IP utilizable  : {network.network_address + 1 if network.num_addresses > 2 else 'N/A'}")
        print(f"  Última IP utilizable   : {network.broadcast_address - 1 if network.num_addresses > 2 else 'N/A'}")
        print(f"  Total de IP (Hosts)    : {network.num_addresses}")
        print(f"  Hosts Utilizables      : {max(0, network.num_addresses - 2)}")
        print(f"  Es IP Privada          : {'Sí' if host.ip.is_private else 'No'}")
        print("=" * 50 + "\n")

    except ValueError as e:
        print(f"\n[!] Error de entrada: La IP o máscara '{ip_cidr}' no es válida.")
        print(f"    Detalle: {e}\n")

def main():
    print("==================================================")
    print("      VALIDADOR Y CALCULADOR DE SUBREDES IP      ")
    print("==================================================")
    
    while True:
        user_input = input("Ingresa IP con CIDR (ej. 192.168.1.50/24) o 'q' para salir: ").strip()
        
        if user_input.lower() == 'q':
            print("¡Hasta luego!")
            sys.exit()
            
        if not user_input:
            continue
            
        calculate_subnet(user_input)

if __name__ == "__main__":
    main()