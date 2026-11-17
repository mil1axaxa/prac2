# Практическая работа №2: Проектирование структур данных (Вариант Б)
**Студенты:** Милана (№19), Камила (№14)  
**Индивидуальный номер N:** 33  

## 1. Таблица полей (Data Dictionary)
| Поле (путь) | Описание смысла поля | Тип Python | Тип JSON | Обяз.? | Пример (ваши данные) |
|---|---|---|---|---|---|
| pad_id | Номер кустовой площадки | str | string | Да | "PAD-23" |
| well_id | Код скважины | str | string | Да | "W-233" |
| p_res_mpa | Пластовое давление, МПа | float | number | Да | 28.5 |
| p_bhp_mpa | Забойное давление, МПа | float | number | Да | 17.2 |
| mode | Режим эксплуатации скважины | str | string | Да | "PUMPING" |
| is_online | Признак связи со станцией (Челлендж 1) | bool | boolean | Да | true |
| sensors | Список замеров с датчиков | list[dict] | array | Да | [{...}, {...}, {...}] |
| sensors[].code | Код датчика в массиве | str | string | Да | "T-01", "Q-01", "P-01" |
| sensors[].value | Измеренное показание датчика | float | number | Да | 49.5, 92.0, 17.2 |
| sensors[].unit | Единица измерения датчика | str | string | Да | "C", "m3/d", "MPa" |

## 2. ER-диаграмма
```mermaid
erDiagram
    TELEMETRY_PACKET ||--|{ SENSOR_ITEM : "включает массив"
    TELEMETRY_PACKET {
        string pad_id "Номер куста"
        string well_id "Код скважины"
        number p_res_mpa "Пластовое давление"
        number p_bhp_mpa "Забойное давление"
        string mode "Режим работы"
        boolean is_online "Связь со станцией"
    }
    SENSOR_ITEM {
        string code "Код датчика"
        number value "Значение"
        string unit "Единица измерения"
    }
