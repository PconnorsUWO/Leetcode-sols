def hardestWorker(n, logs):
    hash_table = {}
    maximum_task = 0
    for i in logs:
        if i not in hash_table:
            hash_table[i[0]] = i[1]
            maximum_task = max(maximum_task, i[1])
        else:
            cur_task_time = i[1] - hash_table[i[0]]
            hash_table[i[0]] = cur_task_time
            maximum_task = max(cur_task_time, maximum_task)
    return maximum_task