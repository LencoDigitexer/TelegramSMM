import api2ch
api = api2ch.DvachApi('gg')
thread = api.get_thread(795678)
print(f'Total {len(thread)} posts in thread')

pic_in_thread = []

for post in thread:
    for file in post.files:
        pic_in_thread.append(api2ch.CHAN_URL + file.path)
print(pic_in_thread[0])