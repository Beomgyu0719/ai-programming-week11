cd ..

cat << 'EOF' >> README.md

## 데이터

- **출처**: 12주차 실습 배포 파일 (`scores_2026.csv`, 검증용 `mini.csv`)
- **규모**: 원본 `scores_2026.csv` 기준 114행 5열 (정제 후 100행 남음)[cite: 1, 2]
- **열 설명**:
  - `학번`: 학생 식별 번호 (문자열)[cite: 1]
  - `이름`: 학생 이름 (문자열)[cite: 1]
  - `반`: 소속 반 (문자열, 정제 후 `'1반'`, `'2반'`)[cite: 1, 2]
  - `과목`: 수강 과목 (문자열, 정제 후 `'수학'`, `'영어'`, `'프로그래밍'`)[cite: 1, 2]
  - `점수`: 과목별 시험 점수 (정수, 유효 범위 `0` 이상 `100` 이하)[cite: 1]
- **빈 칸(결측치) 처리 방법 및 이유**: `점수`가 비어 있는 6개 행은 `dropna(subset=["점수"])`로 삭제했습니다[cite: 2]. 점수가 빈 행을 임의의 값으로 채우면 반별·과목별 평균과 중앙값 같은 통계 수치가 왜곡되므로, 실제 점수가 기록된 데이터만 남기기 위해 제외했습니다[cite: 2].
EOF

git status
git add week12/analysis.py
git commit -m "feat: 성적 CSV 정제와 반별 통계 분석 추가"
git push

git add week12/test_analysis.py README.md
git commit -m "test: 행 수 · 합계 · 손계산 검증 네 케이스 추가"
git push