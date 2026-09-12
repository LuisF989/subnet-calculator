 IPv4 Subnet Calculator & Validator

Un calculador y validador de subredes IP en Python diseñado para administradores de red y técnicos ISP/WISP. Permite calcular rápidamente rangos de direcciones, máscaras, broadcast y capacidad de hosts a partir de una notación CIDR.

 Características
* **Análisis de Direccionamiento:** Calcula dirección de red, broadcast, primera/última IP utilizable y total de hosts.
* **Soporte CIDR:** Procesa máscaras de red flexibles desde `/1` hasta `/32`.
* **Identificación de Ámbito:** Determina automáticamente si una dirección pertenece al rango de IP Privadas (RFC 1918).
* **Validación de Entrada:** Captura errores de sintaxis o rangos fuera de norma mediante manejo estricto de excepciones.

 Tecnologías
* **Lenguaje:** Python 3.x
* **Librerías:** `ipaddress` (Librería nativa del lenguaje, sin dependencias externas)

 Uso
1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/LuisF989/subnet-calculator.git](https://github.com/LuisF989/subnet-calculator.git)
