import pytest
from utils.csv_reader import read_csv

@pytest.mark.parametrize("rate_col", ["hourly_rate", "rate", "salary"])
def test_read_csv_various_rate_keys(tmp_path, rate_col):
    content = f"id,email,name,department,hours_worked,{rate_col}\n" \
              f"1,alice@example.com,Alice Johnson,Marketing,160,50"
    file = tmp_path / "data.csv"
    file.write_text(content)

    result = read_csv(file)

    assert len(result) == 1
    row = result[0]
    assert row["id"] == "1"
    assert row["email"] == "alice@example.com"
    assert row["name"] == "Alice Johnson"
    assert row["department"] == "Marketing"
    assert row["hours_worked"] == 160
    assert row["hourly_rate"] == 50


def test_read_csv_shuffled_columns(tmp_path):
    content = "email,name,department,hours_worked,salary,id\n" \
              "karen@example.com,Karen White,Sales,165,50,201"
    file = tmp_path / "shuffled.csv"
    file.write_text(content)

    result = read_csv(file)

    assert len(result) == 1
    row = result[0]
    assert row["id"] == "201"
    assert row["email"] == "karen@example.com"
    assert row["name"] == "Karen White"
    assert row["department"] == "Sales"
    assert row["hours_worked"] == 165
    assert row["hourly_rate"] == 50
