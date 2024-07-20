def _merge_patterns(base: dict, add: dict) -> dict:
        base["front"] += add.get("front", [])
        base["back"] += add.get("back", [])