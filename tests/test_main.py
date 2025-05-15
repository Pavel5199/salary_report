import pytest
import sys
from pathlib import Path
from io import StringIO
from main import main

@pytest.fixture
def sample_files(tmp_path):
    file1 = tmp_path / "file1.csv"
    file1.write_text("id,email,name,department,hours_worked,hourly_rate\n1,alice@example.com,Alice Johnson,Marketing,160,50")

    file2 = tmp_path / "file2.csv"
    file2.write_text("department,id,email,name,hours_worked,rate\nHR,101,grace@example.com,Grace Lee,160,45")

    return [str(file1), str(file2)]

def test_main_payout_report(monkeypatch, sample_files):
    test_args = ["main.py", *sample_files, "--report", "payout"]
    monkeypatch.setattr(sys, "argv", test_args)

    output = StringIO()
    monkeypatch.setattr(sys, "stdout", output)

    main()
    result = output.getvalue()

    assert "id" in result
    assert "email" in result
    assert "Alice Johnson" in result
    assert "Grace Lee" in result