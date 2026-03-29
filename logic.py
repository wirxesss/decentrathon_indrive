# Даем баллы за опыт
    score += years_active * 5 
    
    # Если уже получал субсидии и вырос — это плюс
    if had_subsidies_before and efficiency_growth > 0:
        score += 20
        
    return score

# Тестовый запуск
print("Проверка системы скоринга...")
print(f"Балл фермера: {get_farmer_score(10, True, 0.15)}")
