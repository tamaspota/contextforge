def generate_daily_focus(projects):
    critical = [p for p in projects if p.get("priority") == "critical"]
    active = [p for p in projects if p.get("status") == "active"]

    focus = []

    for item in critical + active:
        if item not in focus:
            focus.append(item)

    return focus[:3]


def detect_overload(projects):
    active_count = sum(1 for p in projects if p.get("status") == "active")
    critical_count = sum(1 for p in projects if p.get("priority") == "critical")

    warnings = []

    if active_count > 3:
        warnings.append("Too many active projects.")

    if critical_count > 2:
        warnings.append("Too many critical projects.")

    return warnings
