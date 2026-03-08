import argparse
from tasks import add_task, list_tasks, delete_task, mark_done

def main():
    parser = argparse.ArgumentParser(description="CLI Менеджер задач")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list")
    
    add = subparsers.add_parser("add")
    add.add_argument("title", type=str)
    
    done = subparsers.add_parser("done")
    done.add_argument("index", type=int)
    
    delete = subparsers.add_parser("delete")
    delete.add_argument("index", type=int)

    args = parser.parse_args()

    if args.command == "list":
        for i, t in enumerate(list_tasks()):
            status = "[x]" if t['done'] else "[ ]"
            print(f"{i}. {status} {t['title']}")
    elif args.command == "add":
        add_task(args.title)
        print(f"Задача '{args.title}' добавлена.")
    elif args.command == "done":
        if mark_done(args.index):
            print("Задача выполнена!")
    elif args.command == "delete":
        if delete_task(args.index):
            print("Задача удалена.")

if __name__ == "__main__":
    main()
