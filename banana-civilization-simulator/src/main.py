import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_json(name: str):
    with open(DATA_DIR / name, "r", encoding="utf-8") as f:
        return json.load(f)


def clamp(value: int, low: int, high: int) -> int:
    return max(low, min(high, value))


def apply_effects(resources: dict, effects: dict):
    for key, delta in effects.items():
        resources[key] = resources.get(key, 0) + delta


def update_npc_memory_and_relations(npcs: list, event: dict):
    tags = set(event.get("tags", []))
    for npc in npcs:
        npc["memory"].append(event["title"])
        npc["memory"] = npc["memory"][-5:]

        relations = npc.get("relations", {})
        for faction_id, score in relations.items():
            if "conflict" in tags and faction_id == "koopa_legion":
                relations[faction_id] = clamp(score - 2, -100, 100)
            if "aid" in tags and faction_id == "yoshi_agri_zone":
                relations[faction_id] = clamp(score + 1, -100, 100)
            if "tribute" in tags and faction_id == "dk_tribe":
                relations[faction_id] = clamp(score - 1, -100, 100)


def run_simulation(days: int = 10):
    factions = load_json("factions.json")
    resources = load_json("resources.json")
    events = load_json("events.json")
    npcs = load_json("npcs.json")

    print("=== Banana Civilization Simulator (MVP) ===")
    print("(Private text-only prototype, no official assets)\n")

    for day in range(1, days + 1):
        logs = [f"=== Day {day} ==="]

        # 1) 每回合固定五類核心事件
        for event in events:
            if event["id"] == "town_stability_shift":
                shift = random.choice([-2, -1, 0, 1, 2])
                event_effects = dict(event["effects"])
                event_effects["town_stability"] = shift
                apply_effects(resources, event_effects)
                logs.append(f"{event['title']} ({'+' if shift >= 0 else ''}{shift})")
            else:
                apply_effects(resources, event["effects"])
                logs.append(event["title"])

            update_npc_memory_and_relations(npcs, event)

        # 2) 額外市場事件：香蕉價格波動
        banana_delta = random.choice([-2, -1, 1, 2])
        resources["banana_price"] = max(1, resources["banana_price"] + banana_delta)
        if banana_delta > 0:
            logs.append("🍌 香蕉價格上升")
        else:
            logs.append("🍌 香蕉價格下降")

        # 3) 蘑菇王國穩定度跟隨城鎮穩定度
        for faction in factions:
            if faction["id"] == "mushroom_kingdom":
                faction["stability"] = clamp(
                    faction["stability"] + (resources["town_stability"] - 70) // 10,
                    0,
                    100,
                )

        resources["town_stability"] = clamp(resources["town_stability"], 0, 100)

        for line in logs:
            print(line)
        print(
            f"資源: coins={resources['coins']} food={resources['food']} wood={resources['wood']} "
            f"bananas={resources['bananas']} military={resources['military']} "
            f"town_stability={resources['town_stability']} banana_price={resources['banana_price']}"
        )
        print()

    print("=== Final Summary ===")
    for faction in factions:
        print(f"{faction['name']} stability={faction['stability']}")


if __name__ == "__main__":
    run_simulation(days=10)
