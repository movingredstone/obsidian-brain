# Glossary

## PF (Profit Factor) = 수익팩터

```
PF = 총이익 ÷ 총손실
```

| PF | 의미 |
|----|------|
| < 1.0 | 손실. 이익보다 손실이 큼 |
| = 1.0 | 본전 |
| 1.2~1.5 | 양호. 작지만 꾸준한 엣지 |
| 1.5~2.0 | 우수 |
| 2.0+ | 매우 우수 (SUI=2.54) |

**주의**: 저빈도 전략에서 PF=inf 나올 수 있음 (모든 trade 승리). artifact이므로 제외.

## WR (Win Rate) = 승률

```
WR = 이긴 거래 수 ÷ 전체 거래 수 × 100%
```

- WR 67% = 10번 중 7번 이김 (DOGE)
- WR 40% = 10번 중 4번 이김 (BTC keltner)
- **WR만 보면 안 됨**. WR 40% + PF 1.3 = 이길 때 크게 벌어서 OK

## WF (Walk-Forward) = 시간 분할 검증

과거 데이터로 학습 → **본 적 없는 미래 데이터**로 테스트.

```
Train: 2023-01 ~ 2024-01 (12개월)
Test:  2024-01 ~ 2024-04 (3개월, unseen)
```

| WF | 의미 |
|-----|------|
| 3/3 | 모든 미래 구간 수익 ✅ |
| 2/3 | 2개 구간 수익, 1개 손실 ⚠️ |
| 1/3 | 위험. 특정 구간에만 맞음 |
| 0/3 | 과최적화(overfitting) → 실전 망함 |

**핵심**: WF 통과 = 전략이 특정 기간에만 맞는 게 아니라는 증거.

## TVT (Train / Validate / Test)

WF의 변형. 3-way forward split:
- Train: 2023-01 ~ 2024-10 (21개월) — 파라미터 학습
- Validate: 2024-10 ~ 2025-07 (9개월) — 중간 검증
- Test: 2025-07 ~ 2026-06 (11개월) — 최종 검증

**Gap** = Train return - (Val+Test 평균)
- Gap < 0: forward로 개선 중 (좋음)
- Gap > 2%: overfitting 의심

## MDD (Maximum Drawdown) = 최대 낙폭

```
MDD = (최고점 - 최저점) ÷ 최고점 × 100%
```

- MDD -3%: $330 → $320까지 내려감
- MDD -15%: $330 → $280 → position size 절반으로
- MDD -25%: $330 → $247 → 전면 중단

## Regime (시장 국면)

8가지 분류 (src/regime_classifier.py):
- trend_up, trend_down, squeeze, post_breakout
- range, high_vol, low_vol, weekend

**핵심 발견**: regime="any"로 필터 제거 시 PF 1.26→0.99로 붕괴.
각 전략은 자신에게 맞는 regime에서만 진입해야 함.

## Overfitting (과최적화)

과거 데이터에만 완벽하게 맞고 미래에는 망하는 현상.
**발견 사례**: BTC vwap_pullback/4h — Train +4.50%, Test +0.85% (gap +2.17%).
확장 training(18→21개월)으로 발견.
