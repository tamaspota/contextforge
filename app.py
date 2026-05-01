from db import init_db, import_tsv, get_projects, upsert_project
from rules import generate_daily_focus, detect_overload
from ai import parse_brain_dump


def print_projects(projects):
    for p in projects:
        print(f"- {p['project']} | {p['status']} | {p['priority']} | next: {p['next_step']}")


def main():
    init_db()
    import_tsv("seed_projects_demo.tsv")

    print("\nContextForge MVP")
    print("----------------")
    print("1. Show projects")
    print("2. Parse brain dump")
    print("3. Show daily focus")

    choice = input("\nChoose: ").strip()

    if choice == "1":
        projects = get_projects()
        print_projects(projects)

    elif choice == "2":
        text = input("\nPaste brain dump:\n")
        project = parse_brain_dump(text)
        upsert_project(project)

        print("\nParsed project state:")
        for key, value in project.items():
            print(f"{key}: {value}")

    elif choice == "3":
        projects = get_projects()
        focus = generate_daily_focus(projects)
        warnings = detect_overload(projects)

        print("\nToday focus:")
        print_projects(focus)

        if warnings:
            print("\nWarnings:")
            for warning in warnings:
                print(f"- {warning}")

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
