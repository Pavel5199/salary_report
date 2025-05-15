import io
import sys
import os
import pytest
from reports.payout import PayoutReport
from utils.csv_reader import read_csv

@pytest.fixture
def sample_data():
    return [
        {
            "id": "1",
            "email": "alice@example.com",
            "name": "Alice Johnson",
            "department": "Marketing",
            "hours_worked": 160,
            "hourly_rate": 50
        },
        {
            "id": "2",
            "email": "bob@example.com",
            "name": "Bob Smith",
            "department": "Design",
            "hours_worked": 150,
            "hourly_rate": 40
        },
        {
            "id": "3",
            "email": "carol@example.com",
            "name": "Carol Williams",
            "department": "Design",
            "hours_worked": 170,
            "hourly_rate": 60
        },
    ]

def test_payout_output(sample_data):
    report = PayoutReport()
    captured = io.StringIO()
    sys.stdout = captured
    report.generate(sample_data)
    sys.stdout = sys.__stdout__

    output = captured.getvalue()
    assert "Alice Johnson" in output
    assert "8000" in output  # 160 * 50
    assert "Bob Smith" in output
    assert "6000" in output  # 150 * 40
    assert "Carol Williams" in output
    assert "10200" in output  # 170 * 60

def test_csv_reader_hourly_rate(tmp_path):
    content = "id,email,name,department,hours_worked,hourly_rate\n1,a,b,c,160,20"
    file = tmp_path / "file1.csv"
    file.write_text(content)

    records = read_csv(file)
    assert records[0]["hourly_rate"] == 20
    assert records[0]["hours_worked"] == 160

@pytest.mark.parametrize("rate_col", ["rate", "salary"])
def test_csv_reader_alt_rate_names(tmp_path, rate_col):
    content = f"id,email,name,department,hours_worked,{rate_col}\n1,a,b,c,160,25"
    file = tmp_path / "file2.csv"
    file.write_text(content)

    records = read_csv(file)
    assert records[0]["hourly_rate"] == 25.0
