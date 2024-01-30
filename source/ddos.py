import random
import requests
import concurrent.futures


def get_random_url():
    return "http://10.126.3.172:8000/convert/" + str(random.randint(0, 999999999999))


def spam():
    while True:
        response = requests.get(get_random_url())
        print(response.json())
        if response.status_code == 404:
            break


nb_thread = 8
pool = concurrent.futures.ThreadPoolExecutor(max_workers=nb_thread)

for i in range(0, nb_thread):
    pool.submit(spam)