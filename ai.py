import pytest
from load_scores import load_scores


def test_load_scores_normal(tmp_path):
    csv_file = tmp_path / "scores.csv"
    csv_file.write_text("이름,점수\n홍길동,90\n김철수,0\n이영희,100\n", encoding="utf-8")
    kept, skipped = load_scores(str(csv_file))
    assert kept == [("홍길동", 90), ("김철수", 0), ("이영희", 100)]
    assert skipped == []


def test_load_scores_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_scores("no_such_file.csv")


def test_load_scores_header_only(tmp_path):
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("이름,점수\n", encoding="utf-8")
    kept, skipped = load_scores(str(csv_file))
    assert kept == []
    assert skipped == []


@pytest.mark.parametrize(
    "line, expected_reason",
    [
        ("홍길동", "열 개수가 2가 아님"),
        (",80", "이름이 비어 있음"),
        ("홍길동,", "점수가 비어 있음"),
        ("홍길동,abc", "점수가 정수가 아님"),
        ("홍길동,-1", "점수가 0~100 밖"),
        ("홍길동,101", "점수가 0~100 밖"),
    ],
)
def test_load_scores_skipped(tmp_path, line, expected_reason):
    csv_file = tmp_path / "weird.csv"
    csv_file.write_text(f"이름,점수\n{line}\n", encoding="utf-8")
    kept, skipped = load_scores(str(csv_file))
    assert kept == []
    assert len(skipped) == 1
    assert skipped[0][2] == expected_reason