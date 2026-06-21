# Strategy Details

각 코인별 전략 파라미터. 다른 AI가 바로 코드에 복사해서 쓸 수 있게 JSON 형식.

## DOGEUSDT — macd_momentum/8h

가장 높은 승률(67%). 저변동성 환경에서 MACD+RSI 모멘텀 진입.

```python
DOGE_STRATEGY = {
    "symbol": "DOGEUSDT", "interval": "8h", "family": "macd_momentum",
    "direction_filter": "price_ema100",
    "lookback": 48,
    "volume_min": 1.2,
    "atr_stop_mult": 2.0,
    "take_profit_r": 3.0,
    "max_holding_bars": 12,
    "stop_rule": "swing",
    "adx_min": 20,
    "regime": "low_vol",
    "trailing_atr_mult": None,
    "breakeven_r": 1.0,
    "partial_tp_r": 1.0,
    "rsi_mid": 50,
}
```

**성능**: 61 trades, WR=67%, PF=1.988, MDD=-1.24%, WF=3/3
**종료**: 84% 시간초과(4일), 15% 손절, 1% 익절
**포지션**: $110, 5% risk, 3.5% stop → $157 (1.4x)

## SUIUSDT — macd_momentum/4h

최고 PF(2.54). 고변동성(5.63%/일)에 wide stop.

```python
SUI_STRATEGY = {
    "symbol": "SUIUSDT", "interval": "4h", "family": "macd_momentum",
    "direction_filter": "ema_fast_stack",
    "lookback": 48,
    "volume_min": 2.0,
    "atr_stop_mult": 3.5,
    "take_profit_r": 4.0,
    "max_holding_bars": 48,
    "stop_rule": "hybrid",
    "adx_min": 0,
    "regime": "low_vol",
    "trailing_atr_mult": 2.0,
    "breakeven_r": 1.0,
    "partial_tp_r": None,
    "rsi_mid": 50,
}
```

**성능**: 52 trades, WR=48%, PF=2.544, MDD=-2.59%, WF=2/3
**포지션**: $110, 5% risk, 3.5% stop → $157 (1.4x)

## AVAXUSDT — trend_pullback/8h

Stress 7/7 folds 통과. 최고의 WF 성능(3/3).

```python
AVAX_STRATEGY = {
    "symbol": "AVAXUSDT", "interval": "8h", "family": "trend_pullback",
    "direction_filter": "mtf_trend",       # ← 핵심! ema_fast_stack 아님
    "lookback": 48,
    "volume_min": 0.7,
    "atr_stop_mult": 1.5,
    "take_profit_r": 3.0,
    "max_holding_bars": 24,
    "stop_rule": "atr",                     # ← swing 아님
    "adx_min": 20,
    "regime": "any",
    "trailing_atr_mult": 2.0,
    "breakeven_r": None,
    "partial_tp_r": None,
    "tolerance_pct": 0.006,
    "pullback_ref": "ema20",
}
```

**성능**: 76 trades, WR=45%, PF=1.899, MDD=-2.06%, Ret=+14.47%
**WF**: 3/3 positive (+6.99%, +4.66%, +5.23%)
**Folds**: 7/7 ALL POSITIVE
**Long/Short**: 24L/52S, 둘 다 수익
**종료**: 78% 손절, 18% 익절, 4% 시간초과
**포지션**: $110, 5% risk, 3.0% stop → $183 (1.7x)

## 탈락한 전략 (참고용)

### BTC keltner_breakout/1h (검증 완료, 가격 문제로 제외)

```python
BTC_STRATEGY = {
    "symbol": "BTCUSDT", "interval": "1h", "family": "keltner_breakout",
    "direction_filter": "mtf_trend", "lookback": 96, "volume_min": 0.7,
    "atr_stop_mult": 1.2, "take_profit_r": 3.0, "max_holding_bars": 96,
    "stop_rule": "swing", "adx_min": 0, "regime": "high_vol",
    "trailing_atr_mult": 3.0,
}
```
**성능**: 338 trades, WR=40%, PF=1.264, MDD=-2.80%, WF=6/6
**제외 이유**: BTC=$64K, 소액 계좌에 position size 부담

## 공통 리스크 규칙

- 전략당 리스크: 5% ($5.50)
- 동시 포지션: 최대 3개
- 같은 코인: 1개 포지션만
- 3연속 손실: 당일 거래 중단
- Portfolio DD -15%: 포지션 크기 절반
- Portfolio DD -25%: 전면 중단
