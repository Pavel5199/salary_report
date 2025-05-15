from reports.payout import PayoutReport

def get_report(report_name: str) -> PayoutReport:
    reports = {
        "payout": PayoutReport,
    }
    if report_name not in reports:
        raise ValueError(f"Неизвестный отчет: {report_name}")
    return reports[report_name]()
