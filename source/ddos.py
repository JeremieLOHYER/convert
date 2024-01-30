import requests
import concurrent.futures


def get_random_url():
    return "http://tonSiteConnard"


def spam():
    while True:
        response = requests.get(get_random_url())
        print(response.json())
        if response.status_code == 404:
            break


if __name__ == '__main__':
    nb_thread = 8
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=nb_thread)

    for i in range(0, nb_thread):
        pool.submit(spam)