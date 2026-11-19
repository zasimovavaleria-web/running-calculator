KM_PER_MILE = 1.60934


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
        dist_km = float(input("Введите дистанцию (в км): ").replace(",", "."))
        mins = float(input("Сколько минут заняла пробежка: ").replace(",", "."))
        secs = float(input("Сколько ещё секунд: ").replace(",", "."))

        if dist_km <= 0 or (mins * 60 + secs) <= 0:
            print("Ошибка: дистанция и время должны быть больше нуля!")
        else:
            dist_mi = dist_km / KM_PER_MILE

            # Расчёты для километров
            p_min_km, p_sec_km = calculate_pace(dist_km, mins, secs)
            avg_speed_kmh = calculate_speed(dist_km, mins, secs)

            # Расчёты для миль
            p_min_mi, p_sec_mi = calculate_pace(dist_mi, mins, secs)
            avg_speed_mph = calculate_speed(dist_mi, mins, secs)

            print("\n--- Итоги пробежки ---")
            print(f"{'Дистанция:':<26} {dist_km:.2f} км ({dist_mi:.2f} миль)")
            print(f"{'Общее время:':<26} {mins * 60 + secs:.0f} сек")
            print(f"{'Средний темп (на 1 км):':<26} {p_min_km} мин {p_sec_km:02d} сек на 1 км")
            print(f"{'Средний темп (на 1 милю):':<26} {p_min_mi} мин {p_sec_mi:02d} сек на 1 милю")
            print(f"{'Cредняя скорость (км/ч):':<26} {avg_speed_kmh:.2f} км/ч")
            print(f"{'Средняя скорость (миль/ч):':<26} {avg_speed_mph:.2f} миль/ч")
            break

    except ValueError:
        print("Ошибка: пожалуйста, вводите только числа (например, 5 или 10,5).")

