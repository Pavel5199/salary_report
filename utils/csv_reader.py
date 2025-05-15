from typing import List, Dict

def read_csv(file_path: str) -> List[Dict[str, object]]:
    with open(file_path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    headers = lines[0].split(",")
    rate_keys = {"hourly_rate", "rate", "salary"}

    data = []
    for line in lines[1:]:
        values = line.split(",")
        row = dict(zip(headers, values))

        row["hourly_rate"] = int(next(row[k] for k in rate_keys if k in row))
        row["hours_worked"] = int(row["hours_worked"])
        data.append(row)

    return data
