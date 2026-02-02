from concurrent.futures import ThreadPoolExecutor

def check_web(url):
    # Simula una petición de red
    return f"URL {url} analizada"

urls = ["Google", "Apple", "Python", "GitHub"]

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as executor:
        resultados = list(executor.map(check_web, urls))
    
    print(resultados)