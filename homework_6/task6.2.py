from collections import Counter

with open('nginx_logs.txt', 'r', encoding='utf-8') as my_file:
    my_list = []
    for el in my_file:
        el = el.split(' ')
        remote_addr = el[0]
        my_list.append(remote_addr)
print('Топ 5 спамеров')
ip_spam, times = Counter(my_list).most_common(1)[0]
print(f' IP спамера {ip_spam} количество запросов {times}')

ip_spam, times = Counter(my_list).most_common(2)[1]
print(f' IP спамера {ip_spam} количество запросов {times}')

ip_spam, times = Counter(my_list).most_common(3)[2]
print(f' IP спамера {ip_spam} количество запросов {times}')

ip_spam, times = Counter(my_list).most_common(4)[3]
print(f' IP спамера {ip_spam} количество запросов {times}')

ip_spam, times = Counter(my_list).most_common(5)[4]
print(f' IP спамера {ip_spam} количество запросов {times}')





