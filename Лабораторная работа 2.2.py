salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# Подушка = сумма всех дефицитов за 10 месяцев
capital = 0
current_spend = spend

for _ in range(months):
    capital += current_spend - salary
    current_spend *= (1 + increase)

print(f"Нужно денег: {capital:.0f} руб.")
