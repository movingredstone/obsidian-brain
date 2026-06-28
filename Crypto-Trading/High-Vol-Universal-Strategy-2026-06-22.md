# High-Vol Universal Crypto Strategy Hunt — 2026-06-22

## 목적
한정된 자본에서 빠른 기회를 찾기 위해 Binance USDT 선물의 고변동성 코인 50개를 대상으로 범용적으로 반복 생존하는 전략 family를 찾았다.

## 1차 스크리닝
- 대상: 50개 고변동성/고거래량 코인
- 실험: 코인당 300개 × 4h/8h
- workers: 9
- 결과 파일:
  - `results/optimization/high_vol_50_universal_survivors.csv`
  - `results/optimization/high_vol_50_universal_family.csv`
- 생존 후보: 80개
- 생존 코인: 27개

### 1차 범용 순위
1. `donchian_breakout / 4h` — 13개 코인 생존, 엔진 추가 필요
2. `macd_momentum / 4h` — 9개 코인 생존, paper trader 가능
3. `macd_momentum / 8h` — 9개 코인 생존, paper trader 가능
4. `trend_pullback / 4h` — 8개 코인 생존, paper trader 가능
5. `range_breakout / 4h` — 6개 코인 생존, 엔진 추가 필요

## 2차 대량 탐색
- 대상: 1차 생존 상위 18개 코인
- 실험: 코인당 3,000개 × 4h/8h
- 총 후보: 약 108,000개
- workers: 9
- 결과 파일:
  - `results/optimization/high_vol_stage2_large_survivors.csv`
  - `results/optimization/high_vol_stage2_large_family.csv`

### 2차 범용 순위
1. `macd_momentum / 4h`
   - 생존 코인: 15개
   - 후보 수: 49개
   - median return: +0.720%
   - median PF: 1.779
   - 평균 fold: 5.35/7
   - 총 trades: 3116
   - paper trader 가능

2. `macd_momentum / 8h`
   - 생존 코인: 14개
   - 후보 수: 40개
   - median return: +0.675%
   - median PF: 2.0045
   - 평균 fold: 5.28/7
   - 총 trades: 2464
   - paper trader 가능

3. `keltner_breakout / 4h`
   - 생존 코인: 13개
   - 후보 수: 38개
   - median return: +0.805%
   - median PF: 1.798
   - 평균 fold: 5.53/7
   - 총 trades: 2366
   - paper trader 엔진 추가 필요

4. `rsi_momentum / 4h`
   - 생존 코인: 10개
   - 엔진 추가 필요

5. `trend_pullback / 4h`
   - 생존 코인: 5개
   - median return: +0.925%
   - median PF: 2.001
   - 평균 fold: 6.0/7
   - 총 trades: 485
   - paper trader 가능하지만 범용성은 macd보다 낮음

## Stage-2 Walk-Forward
- 방식: Train 12개월 → 다음 3개월 Test
- windows: 9개
- 결과 파일: `results/optimization/high_vol_stage2_walk_forward_results.csv`
- 모드:
  - `all_families`: breakout 포함
  - `deployable_only`: 현재 paper trader 가능 family만 사용 (`macd_momentum`, `trend_pullback`)

### deployable_only 상위 심볼
1. TONUSDT — avg_test +1.49%, pos 5/6, trades 68
2. NEARUSDT — avg_test +1.35%, pos 7/9, trades 70
3. ADAUSDT — avg_test +1.28%, pos 7/9, trades 141
4. SOLUSDT — avg_test +1.22%, pos 8/9, trades 76
5. UNIUSDT — avg_test +1.16%, pos 9/9, trades 73
6. AVAXUSDT — avg_test +1.03%, pos 7/9, trades 76

### deployable_only family picks
- `macd_momentum / 4h`: 81 picks, avg_test +0.775%, positive 58
- `macd_momentum / 8h`: 65 picks, avg_test +0.723%, positive 47
- `trend_pullback / 4h`: 9 picks, avg_test +0.922%, positive 7
- `trend_pullback / 8h`: 1 pick, avg_test +1.93%, positive 1

## 결론
- 범용 정답: `macd_momentum / 4h`와 `macd_momentum / 8h`.
- 고변동성 코인의 진짜 성능 후보는 `keltner_breakout / 4h`도 강하지만 현재 paper trader 엔진 추가가 필요하다.
- 현재 위험 기준의 walk-forward 평균은 S&P500 분기 허들 +2.41%를 넘지 못했다. 실거래 금지, paper only.
- paper 후보 포트폴리오로는 TON/NEAR/ADA/SOL/UNI/AVAX가 우선순위다.

## 다음 단계
1. 바로 paper 가능한 deployable-only 포트폴리오 구성: TON, NEAR, ADA, SOL, UNI, AVAX 중 자본에 맞게 3~4개 선택.
2. 더 높은 범용 edge를 원하면 `keltner_breakout / 4h`를 `paper_trader_github.py`에 백테스트 엔진과 동일하게 구현.
3. 선택 후보에 대해 bootstrap/split-half/volatility bucket 검증 후 paper trader 적용.

## 관련 파일
- `scripts/high_vol_50_universal_hunt.py`
- `scripts/high_vol_stage2_large_hunt.py`
- `scripts/high_vol_stage2_walk_forward.py`
- `results/optimization/high_vol_50_universal_family.csv`
- `results/optimization/high_vol_stage2_large_family.csv`
- `results/optimization/high_vol_stage2_walk_forward_results.csv`
