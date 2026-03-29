def get_candidate_score(leadership_exp, motivation_level, achievements_count):
    score = 0
    # Баллы за лидерский опыт (проекты, волонтерство)
    score += leadership_exp * 15 
    
    # Баллы за мотивацию (от 1 до 10)
    score += motivation_level * 5
    
    # Баллы за конкретные достижения
    score += achievements_count * 10
        
    return score

# Тестовый расчет для кандидата в InVision U
print("Анализ потенциала лидера...")
print(f"Итоговый балл кандидата: {get_candidate_score(3, 9, 5)}")
print("Пояснение: Оценка сформирована на основе лидерского опыта и уровня мотивации.")
