import heapq

def min_cost_to_connect_cables(cables):
    # Ініціалізуємо мінімальну купу
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Виймаємо два найкоротших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # З'єднуємо їх
        combined_length = first + second
        total_cost += combined_length
        
        # Додаємо новий кабель назад в купу
        heapq.heappush(cables, combined_length)
    
    return total_cost

# Приклад
cables = [8, 4, 6, 12]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))