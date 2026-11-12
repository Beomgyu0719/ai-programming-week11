# 성적 관리 프로그램 (CSV 성적 검증기)

## 1. 무엇을 하나요 (What)
성적 데이터가 담긴 CSV 파일을 읽어 유효한 학생 이름과 점수(0~100점 정수) 목록(`kept`)을 추출하고, 형식이 잘못되거나 범위를 벗어난 행은 건너뛴 기록(`skipped`)으로 분리해 반환하는 파이썬 프로그램입니다.

## 2. 왜 만들었나요 (Why)
현장의 실제 성적 CSV 파일에는 빈 줄, 누락된 점수, 100점을 초과하는 오기입 데이터, 동명이인 등 예외 상황이 빈번하게 섞여 있습니다. 이를 별도 검증 없이 단순 파싱하면 프로그램이 비정상 종료되거나 잘못된 통계가 산출되므로, 명세에 기반한 방어적 데이터 검증과 자동화된 단위 테스트(`pytest`)로 코드의 신뢰성을 보장하기 위해 만들었습니다.

## 3. 어떻게 쓰나요 (How)
### 환경 준비 및 패키지 설치
Python 3.10 이상 환경에서 아래 명령어로 테스트 도구를 설치합니다.
```bash
pip install pytest pytest-cov
```

### 프로그램 실행
기본 파일(`scores.csv`) 또는 원하는 CSV 파일 경로를 인자로 전달해 실행합니다.
```bash
python3 load_scores.py scores.csv
```

## 4. 어떻게 테스트하나요 (Test)
### 단위 테스트 실행
```bash
pytest test_load_scores.py
```

### 코드 커버리지 측정
```bash
pytest --cov=load_scores --cov-report=term-missing
```

### 통과 화면 예시
```text
$ pytest test_load_scores.py
========================= test session starts =========================
collected 12 items

test_load_scores.py ............                                [100%]

========================= 12 passed in 0.04s ==========================
```

## 5. 파일 구성
* `load_scores.py`: 성적 CSV 파일을 읽고 유효성 검증 후 `(kept, skipped)`를 반환하는 핵심 모듈
* `test_load_scores.py`: 정상·예외·경계값(-1, 0, 100, 101) 및 잘못된 형식 처리를 검증하는 `pytest` 테스트 코드
* `test_ai_A.py`: AI에게 구현 코드를 제공하고 생성한 비교 실험용 테스트 코드
* `test_ai_B.py`: AI에게 명세서 6칸만 제공하고 생성한 비교 실험용 테스트 코드
* `scores.csv` / `empty.csv` / `weird.csv`: 정상, 빈 헤더, 비정상 데이터 검증용 샘플 CSV 파일
* `LICENSE`: MIT License

## 6. 만든 사람
* **작성자**: 권범규 (2026101090)
* **AI 활용 내역**:
  * 프롬프트 A(코드 제공)와 프롬프트 B(명세 제공) 방식에 따른 AI 생성 단위 테스트의 품질 및 버그 고착화 현상 비교 실험에 활용
  * `test_load_scores.py`의 경계값 테스트 구조화 및 `README.md` 문서 초안 검토에 활용