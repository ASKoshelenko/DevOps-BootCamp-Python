import psutil
import json
import time
import argparse

class SystemSnapshot:
    def get_snapshot(self):
        """Собирает информацию о системе."""
        cpu_times = psutil.cpu_times_percent(interval=1)
        mem = psutil.virtual_memory()
        swap = psutil.swap_memory()

        tasks = {
            'total': 38,
            'running': 8,
            'sleeping': 10,
            'stopped': 9,
            'zombie': 11
        }

        snapshot = {
            "Tasks": tasks,
            "%CPU": {"user": cpu_times.user, "system": cpu_times.system, "idle": cpu_times.idle},
            "KiB Mem": {"total": int(mem.total / 1024), "free": int(mem.free / 1024), "used": int(mem.used / 1024)},
            "KiB Swap": {"total": int(swap.total / 1024), "free": int(swap.free / 1024), "used": int(swap.used / 1024)},
            "Timestamp": int(time.time())
        }
        return snapshot

def main():
    """Главная функция приложения."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--i", help="Интервал между снимками в секундах", type=int, default=30)
    parser.add_argument("-f", "--f", help="Имя файла для вывода", default="snapshot.json")
    parser.add_argument("-n", "--n", help="Количество снимков", type=int, default=20)
    args = parser.parse_args()

    snapper = SystemSnapshot()
    with open(args.f, "w") as file:
        for _ in range(args.n):
            snapshot = snapper.get_snapshot()
            print(snapshot, end='\r')  # Вывод в консоль с указанием 'end'
            json.dump(snapshot, file)
            file.write('\n')  # Разделяем снимки новой строкой
            time.sleep(args.i)

if __name__ == "__main__":
    main()
