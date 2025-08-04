import json

def plus():
    with open("VRC.json", "r") as f:
        data = json.load(f)
    settings = data.get("settings", [])
    for item in settings:
        if "counter" in item:
            current = item["counter"].get("counter", 0)
            item["counter"]["counter"] = current + 1
            break
    else:
        settings.append({ "counter": { "counter": 1 } })
    with open("VRC.json", "w") as f:
        json.dump(data, f, indent=4)
    return current +1

