import requests

def chk_proxy(proxy):
    """
    Verifica si una proxy es funcional enviando una solicitud a un servicio de detección de IP.

    Args:
        proxy (str): La proxy en formato "IP:PUERTO".

    Returns:
        bool: True si la proxy es funcional, False en caso contrario.
    """
    url = "http://httpbin.org/ip"  # Servicio para obtener la IP pública
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        if response.status_code == 200:
            return True
    except Exception:
        print("error")
    return False

    
def load_proxies_from_file(file_path):
    """
    Carga una lista de proxies desde un archivo de texto.

    Args:
        file_path (str): Ruta al archivo que contiene las proxies.

    Returns:
        list: Lista de proxies.
    """
    with open(file_path, "r") as file:
        return file.read().splitlines()

def save_working_proxies(file_path, working_proxies):
    """
    Guarda una lista de proxies funcionales en un archivo de texto.

    Args:
        file_path (str): Ruta al archivo donde se guardarán las proxies funcionales.
        working_proxies (list): Lista de proxies funcionales.
    """
    with open(file_path, "w") as file:
        file.write("\n".join(working_proxies))
def save_working_proxy(file_path, proxy):
    """
    Guarda una proxy funcional en un archivo de texto.

    Args:
        file_path (str): Ruta al archivo donde se guardará la proxy funcional.
        proxy (str): Proxy funcional a guardar.
    """
    with open(file_path, "a") as file:
        file.write(proxy + "\n")
        
if __name__ == "__main__":
    proxies_file = "C:\\Users\\CARLO\\Documents\\python\\chk\\checker git\\proxies.txt"  # Nombre del archivo que contiene las proxies
    output_file = "working_proxies.txt"  # Nombre del archivo para guardar las proxies funcionales
    proxies = load_proxies_from_file(proxies_file)

    working_proxies = []

    for proxy in proxies:
        if chk_proxy(proxy):
            print(f"Proxy funcional: {proxy}")
            save_working_proxy(output_file, proxy)
        else:
            print(f"Proxy no funcional: {proxy}")