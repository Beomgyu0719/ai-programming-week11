import pytest
from load_scores import load_scores


def test_valid_and_duplicate_names(tmp_path):
    p = tmp_path / "test.csv"
    p.write_text("이름,점수\n김민수,85\n김민수,90\n", encoding="utf-8")
    kept, skipped = load_scores(str(p))
    assert kept == [("김민수", 85), ("김민수", 90)]
    assert skipped == []


def test_missing_file():
    with pytest.raises(FileNotFoundError):
        load_scores("missing.csv")


def test_only_header(tmp_path):
    p = tmp_path / "header.csv"
    p.write_text("이름,점수\n", encoding="utf-8")
    kept, skipped = load_scores(str(p))
    assert kept == []
    assert skipped == []


@pytest.mark.parametrize("score, valid", [(-1, False), (0, True), (100, True), (101, False)])
def test_score_boundaries(tmp_path, score, valid):
    p = tmp_path / "bound.csv"
    p.write_text(f"이름,점수\n학생,{score}\n", encoding="utf-8")
    kept, skipped = load_scores(str(p))
    assert (len(kept) == 1) == valid