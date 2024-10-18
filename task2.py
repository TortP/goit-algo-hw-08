import heapq

def merge_k_lists(lists):
    heap = []
    result = []
    
    # Додаємо перший елемент з кожного списку в купу
    for i, sorted_list in enumerate(lists):
        if sorted_list:
            heapq.heappush(heap, (sorted_list[0], i, 0))  # (значення, індекс списку, індекс елемента)
    
    while heap:
        value, list_idx, element_idx = heapq.heappop(heap)
        result.append(value)
        
        # Додаємо наступний елемент з цього ж списку, якщо він існує
        if element_idx + 1 < len(lists[list_idx]):
            next_element = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_element, list_idx, element_idx + 1))
    
    return result

# Приклад
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)