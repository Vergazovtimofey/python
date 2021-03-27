with open('nginx_logs.txt', 'r', encoding='utf-8') as my_file:
    my_list = []
    for el in my_file:
        el = el.split(' ')
        remote_addr = el[0:1]
        request_type = el[5:6]
        requested_resource = el[6:7]
        remote_addr = remote_addr.pop(0)
        request_type = request_type.pop(0)
        requested_resource = requested_resource.pop(0)


        all_things = remote_addr, request_type, requested_resource
        all_things = tuple(all_things)
        my_list.append(all_things)
    print(my_list)





