def get_task_counts(get_todo_list):
    completed_task_count = 0
    pending_task_count = len(get_todo_list)
    total_task_count = pending_task_count
    for list_items in get_todo_list:
        if list_items.completed:
            completed_task_count += 1
            pending_task_count -= 1
    return total_task_count, pending_task_count, completed_task_count
