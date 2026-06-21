# Current State

> 2026-06-21 최종 | Hermes Agent (DeepSeek v4)

## 현재 상태: GitHub Actions 페이퍼 트레이딩 준비 완료

모든 백테스트 검증 완료. 코드 준비 완료.
GitHub Actions로 4시간마다 시그널 체크 (컴퓨터 OFF 가능, 무료).

## 선정된 포트폴리오

3코인, $330 (각 $110):

| # | Coin | Strategy | Interval | Price | PF | WR | WF | Folds |
|---|------|----------|----------|-------|-----|-----|-----|-------|
| 1 | DOGE | macd_momentum | 8h | $0.08 | 1.99 | 67% | 3/3 | 7/7 |
| 2 | SUI | macd_momentum | 4h | $0.90 | 2.54 | 48% | 2/3 | 5/7 |
| 3 | AVAX | trend_pullback | 8h | $6.23 | 1.90 | 45% | 3/3 | 7/7 |

## GitHub Actions 셋업 (진행 중)

준비된 파일:
  ✅ paper_signal.py          — 독립형 시그널 체커 (외부 의존성 없음)
  ✅ requirements_paper.txt    — pandas, numpy, requests
  ✅ .github/workflows/signal.yml — 4시간마다 자동 실행

남은 작업:
  ⬜ GitHub 저장소 생성 (public)
  ⬜ TELEGRAM_TOKEN, TELEGRAM_CHAT_ID secrets 설정
  ⬜ git push → 자동 활성화

## 탈락한 코인/전략

- **BTC**: $64K로 소액 부적합. keltner_breakout/1h는 338t, WF 6/6 검증 완료
- **XRP**: stress survivor 부족
- **SOL**: PF 1.35로 낮음
- **vwap_pullback/4h**: overfitting 발견 (gap +2.17%)
- **주식**: QLD/SOXL/TQQQ multi-factor WF 탈락

## Cron 상태

- `6d7767f1af30`: ⏸️ PAUSED (컴퓨터 OFF 시 작동 불가)
- `b73e6d781845`: ⏸️ PAUSED

→ GitHub Actions로 대체 예정

## 다음 할 일

1. GitHub 저장소 생성 + push
2. Telegram secrets 설정
3. 첫 시그널 확인 (4시간 후)
4. 30일 페이퍼 트레이딩 관찰
5. 승률/수익이 백테스트와 일치하는지 검증
6. 일치하면 실거래 검토

## 검증 완료 목록

- [x] 7코인 broad fold evaluation
- [x] Stress test (9 harsh conditions)
- [x] TVT (21개월 training)
- [x] BTC 6-fold walk-forward (6/6)
- [x] BTC 3중 독립 검증
- [x] DOGE 전체 파이프라인
- [x] SUI 전체 파이프라인
- [x] AVAX 파라미터 수정 + 재검증
- [x] Stock 멀티팩터 (WF 탈락)
- [x] GitHub Actions 코드 준비

## 다른 AI가 이어서 할 때

1. 옵시디언 `Crypto-Trading/README.md` 부터 읽기
2. 프로젝트: `~/Desktop/hermes/investmentsystem`
3. Python: `.venv/bin/python`
4. GitHub Actions 파일은 `.github/workflows/signal.yml`
5. 시그널 스크립트: `paper_signal.py`
6. 전략 파라미터: [[Strategies]]
7. 백테스트: `python main.py fold-eval --help`
