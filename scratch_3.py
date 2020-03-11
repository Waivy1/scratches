from threading import Thread
import time

def parse_site(name):
    import random

    s = random.randint(1, 6)
    time.sleep(s)

    print(name, s)


if __name__ == "__main__":
    for url in ['http://123', 'ass', 'bark', 'dog']:
        print(f'starting thread: {url}')
        Thread(target=parse_site, args=(url, )).start()

    print('waiting for the last thread')



def run(site):
    url = site.pop(site[0]) # a
    parse(url)


sites = ['a', 'b', 'c', 'd', 'e', 'ff', 'hth', 'htht', 'ntht']
for vid_id in range(3):
    print(f'doing {vid_id}')
    Thread(target=run, args=(sites, )).start()


print('w8ing')
