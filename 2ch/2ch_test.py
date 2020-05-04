import api2ch
import html2text
api = api2ch.DvachApi('gg')
thread = api.get_thread(795678)
print(f'Total {len(thread)} posts in thread')
pic = []
print(thread[0].files)
for i in range(0, len(thread[0].files)):
    pic.append("https://2ch.hk" + thread[0].files[i].thumbnail)

print(thread[0].subject)