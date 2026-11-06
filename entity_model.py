import json
from typing import Any


def build_well_passport() -> dict[str, Any]:
    """Создаёт цифровой паспорт нефтяной скважины."""

    return {
        "well_id": "W-133",
        "depth_m": 3150,
        "q_liq": 55.5,
        "w_pct": 78.0,
        "is_active": True,
        "pump": {
            "model": "ЭЦН5-80-1800",
            "power_kw": 105.0
        },
        "field_name": "Приобское"
    }


def save_to_json(
    data: dict[str, Any],
    filename: str = "data.json"
) -> None:
    """Сохраняет паспорт в JSON-файл."""

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )


def load_from_json(
    filename: str = "data.json"
) -> dict[str, Any]:
    """Загружает паспорт из JSON-файла."""

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def print_passport_summary(
    passport: dict[str, Any]
) -> None:
    """Выводит сводку по паспорту скважины."""

    q_oil = passport["q_liq"] * (
        1 - passport["w_pct"] / 100
    )

    pump = passport["pump"]

    print("=" * 40)
    print("ПАСПОРТ НЕФТЯНОЙ СКВАЖИНЫ")
    print("=" * 40)
    print(f"Код скважины: {passport['well_id']}")
    print(f"Месторождение: {passport['field_name']}")
    print(f"Глубина: {passport['depth_m']} м")
    print(f"Дебит жидкости: {passport['q_liq']:.1f} м³/сут")
    print(f"Обводнённость: {passport['w_pct']:.1f}%")
    print(f"Дебит чистой нефти: {q_oil:.2f} м³/сут")
    print(f"Скважина активна: {passport['is_active']}")
    print(f"Модель насоса: {pump['model']}")
    print(f"Мощность насоса: {pump['power_kw']:.1f} кВт")


if __name__ == "__main__":
    passport = build_well_passport()

    save_to_json(passport)
    print("[OK] Файл data.json успешно записан.")

    loaded_passport = load_from_json()
    print("[OK] Файл data.json успешно прочитан.")

    print_passport_summary(loaded_passport)