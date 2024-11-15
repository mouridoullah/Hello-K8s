import requests
import threading
import time

URL = "http://192.168.49.2:32100"
REQUEST_COUNT = 1000  # Nombre de requêtes
CONCURRENT_THREADS = 50  # Nombre de threads concurrents

def make_request():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print("Réponse OK:", response.text)
        else:
            print("Erreur:", response.status_code)
    except Exception as e:
        print("Échec de la requête:", e)

def run_load_test():
    threads = []
    start_time = time.time()
    
    for _ in range(REQUEST_COUNT):
        if len(threads) >= CONCURRENT_THREADS:
            # Attendre que tous les threads en cours se terminent avant de continuer
            for thread in threads:
                thread.join()
            threads = []
        
        # Démarrer un nouveau thread pour chaque requête
        thread = threading.Thread(target=make_request)
        threads.append(thread)
        thread.start()

    # Attendre que tous les threads terminent
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Temps total: {end_time - start_time} secondes")

if __name__ == "__main__":
    run_load_test()
