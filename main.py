import argparse
from typing import List
from utils.csv_reader import read_csv
from reports import get_report

def main():
    parser = argparse.ArgumentParser(description="Генератор отчётов по зарплатам")
    parser.add_argument("files", nargs="+", help="CSV-файлы с данными сотрудников")
    parser.add_argument("--report", required=True, help="Тип отчёта")

    args = parser.parse_args()

    try:
        all_records: List[dict] = []
        for file in args.files:
            records = read_csv(file)
            all_records.extend(records)

        report_name: str = args.report
        report_class = get_report(report_name)

        report_class.generate(all_records)

    except FileNotFoundError as e:
        print(f"Файл не найден: {e.filename}")
    except Exception as e:
        print("Ошибка при выполнении скрипта:")
        print(e)

if __name__ == "__main__":
    main()
