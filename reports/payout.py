from collections import defaultdict
from typing import List, Dict, Any

class PayoutReport:
    def generate(self, data: List[Dict[str, Any]]) -> None:
        departments: defaultdict[str, List[Dict[str, Any]]] = defaultdict(list)
        for row in data:
            departments[row["department"]].append(row)

        columns = [("id", 6), ("email", 25), ("name", 20),
                   ("hours_worked", 15), ("hourly_rate", 13), ("payout", 10)]

        print("".join(f"{col:<{wid}}" for col, wid in columns))

        for department, records in departments.items():
            print(f"\n {department}")

            for row in records:
                payout = row["hours_worked"] * row["hourly_rate"]
                print("".join(
                    f"{int(payout):<{wid}}" if col == "payout"
                    else f"{int(row[col]):<{wid}}" if col in {"hours_worked", "hourly_rate"}
                    else f"{row[col]:<{wid}}"
                    for col, wid in columns
                ))
