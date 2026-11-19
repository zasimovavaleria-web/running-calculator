def calculate_pace(distance, minutes, seconds):
    total_seconds = minutes * 60 + seconds
    pace_seconds = total_seconds / distance
    pace_min = int(pace_seconds // 60)
    pace_sec = int(pace_seconds % 60)
    return pace_min, pace_sec


def calculate_speed(distance, minutes, seconds):
    total_seconds = minutes * 60 + seconds
    total_hours = total_seconds / 3600
    speed = distance / total_hours
    return speed

while True:
    try:
        dist = float(input("Введите дистанцию (в км): ").replace(",", "."))
        mins = float(input("Сколько минут заняла пробежка: ").replace(",", "."))
        secs = float(input("Сколько ещё секунд: ").replace(",", "."))

        if dist <= 0 or (mins * 60 + secs) <= 0:
            print("Ошибка: дистанция и время должны быть больше нуля!")
        else:
            p_min, p_sec = calculate_pace(dist, mins, secs)
            avg_speed = calculate_speed(dist, mins, secs)

            print("\n--- Итоги пробежки ---")
            print(f"{'Общее время:':<18} {mins * 60 + secs:.0f} сек")
            print(f"{'Средний темп:':<18} {p_min} мин {p_sec:02d} сек на 1 км")
            print(f"{'Cредняя скорость:':<18} {avg_speed:.2f} км/ч")
            break

    except ValueError:
        print("Ошибка: пожалуйста, вводите только числа (например, 5 или 10,5).")

