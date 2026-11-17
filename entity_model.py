"""Этап 1 (Вариант Б): Моделирование пакета телеметрии, сохранение и чтение JSON."""

import json
from typing import Any

def build_telemetry_packet() -> dict[str, Any]:
    """Формирует пакет телеметрии для Миланы (19) и Камилы (14), N = 33."""
    return {
        "pad_id": "PAD-23",
        "well_id": "W-233",
        "p_res_mpa": 28.5,
        "p_bhp_mpa": 17.2,
        "mode": "PUMPING",
        "is_online": True,  # Челлендж №1
        "sensors": [
            {"code": "T-01", "value": 49.5, "unit": "C"},
            {"code": "Q-01", "value": 92.0, "unit": "m3/d"},
            {"code": "P-01", "value": 17.2, "unit": "MPa"}  # 3-й датчик по Челленджу №1
        ]
    }

def save_to_json(data: dict[str, Any], filename: str = "data.json") -> None:
    """Сериализует словарь Python в текстовый файл формата JSON."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_from_json(filename: str = "data.json") -> dict[str, Any]:
    """Десериализует (читает) JSON-файл с диска обратно в словарь Python."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def print_telemetry_summary(packet: dict[str, Any]) -> None:
    """Выводит красивую сводку по прочитанному пакету телеметрии."""
    print("=" * 56)
    print(f"ПАКЕТ ТЕЛЕМЕТРИИ: куст {packet['pad_id']} | скважина {packet['well_id']}")
    print("=" * 56)
    print(f"Режим работы:       {packet['mode']}")
    print(f"Связь со станцией:  {packet['is_online']}")
    print(f"Пластовое давл.:    {packet['p_res_mpa']} МПа")
    print(f"Забойное давл.:     {packet['p_bhp_mpa']} МПа")
    print("-" * 56)
    print("Показания датчиков:")
    for s in packet["sensors"]:
        print(f"  - датчик [{s['code']}]: {s['value']} {s['unit']}")
    print("=" * 56)

if __name__ == "__main__":
    pkt = build_telemetry_packet()
    save_to_json(pkt, "data.json")
    print("[OK] Файл data.json успешно записан на диск!")

    loaded_pkt = load_from_json("data.json")
    assert loaded_pkt == pkt, "Ошибка: прочитанный пакет не совпал с исходным!"
    print("[OK] Обратное чтение через json.load() прошло без потерь!")

    print_telemetry_summary(loaded_pkt)
