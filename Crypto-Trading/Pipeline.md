# Pipeline

전체 최적화 파이프라인. 5단계로 구성.

## Stage 1: Broad Fold Evaluation

```bash
python main.py fold-eval --symbol BTCUSDT --intervals 1h 4h 8h \
  --experiments 5000 --workers 9 --top-n 75 --mode baseline
```

- 랜덤 experiment 생성 → 7개 반기 fold로 평가
- 5000개/interval, 9 worker 병렬
- output: `results/optimization/<SYMBOL>_baseline_<ts>_fold_flat.csv`

## Stage 2: Stress Test

```bash
python main.py optimize --symbol BTCUSDT --intervals 1h 4h 8h \
  --experiments 75 --workers 9 --top-n 75 --stage stress \
  --source-top-path <baseline_csv>
```

- Top 75 candidates를 9가지 harsh condition으로 재테스트
- 조건: 2x slippage, taker fee, 1bar delay, conservative stop, funding cost, 1x leverage, 1 trade/day, 3 loss limit
- output: `results/optimization/<SYMBOL>_stress_<ts>_fold_flat.csv`

## Stage 3: TVT (Train/Validate/Test)

```bash
python main.py tvt --symbol BTCUSDT \
  --source-csv <stress_csv> --top-n 10
```

- Train=2023-01~2024-10 (21개월), Val=2024-10~2025-07, Test=2025-07~2026-06
- Forward time split → overfitting 감지
- Gap = train_return - (val_return + test_return)/2
- Gap이 양수이고 크면 overfitting

## Stage 4: Walk-Forward Verification

6-fold rolling:
- 각 fold마다 Train 12개월 → Test 3개월
- 6/6 positive = robust ✅
- 별도 스크립트: `scripts/final_verify.py`

## Stage 5: Paper Trading

```bash
python main.py paper
python main.py paper --mode optimized
```

- Forward 2026 데이터로 시뮬레이션
- baseline: 모든 regime, equal weight
- optimized: regime filter + risk-parity

## 고변동 코인용 Focus Override

```python
HIGH_VOL_FOCUS = {
    "atr_stop_mults": [1.5, 2.0, 2.5, 3.0, 4.0],
    "take_profit_rs": [2.0, 3.0, 4.0, 5.0],
    "lookbacks": [48, 96, 144],
}
```

`evaluate_folds(focus_override=HIGH_VOL_FOCUS)`로 전달.

## 버그 수정 내역

1. `evaluate_folds()`가 `source_top_path` 무시 → stress가 랜덤 experiment 재생성. **수정됨.**
2. `backtest_experiment` 리턴 키: `return_pct`, `trades`, `fees`, `slippage_cost` (NOT `total_` prefix)
3. `main.py` pandas import 누락. **수정됨.**

## Elimination Chain (Stress)

- R1: Baseline ≥5/7 folds
- R2: Stress ≥5/7 folds
- R4: Trade count ≥40 (or ≥15 for low-frequency)
- R5: PF honesty (no inf PF, no single-fold PF > 20)
