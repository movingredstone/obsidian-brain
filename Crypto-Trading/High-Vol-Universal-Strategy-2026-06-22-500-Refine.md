# High-Vol Universal Strategy — Current 4 +500 Refinement

## 요청
사용자 요청: “벤치마크 보다 더 벌어? 학습 각 500개 정도 더해.”

## 추가 실행
- 대상: 현재 paper 포트폴리오 4개 심볼 `UNIUSDT`, `NEARUSDT`, `SOLUSDT`, `ADAUSDT`
- 추가 탐색: 각 심볼당 `500 experiments × 4h/8h`
- workers: 9
- seed: 20260624
- 스크립트: `scripts/current4_500_refine.py`
- 결과:
  - `results/optimization/current4_500_refine_survivors.csv`
  - `results/optimization/current4_500_refine_family.csv`
  - `results/optimization/current4_500_refine_walk_forward.csv`
  - `results/optimization/current4_500_refine_walk_forward_5pct.csv`
  - `results/optimization/deployed4_fixed_wf_0p5pct.csv`
  - `results/optimization/deployed4_fixed_wf_5pct.csv`

## 추가 500개 탐색 결과 — R1/R2/R4/R5
- UNI: stress_rows=75, R1/R2=32, R4=6, R5=4, deployable=3
- NEAR: stress_rows=75, R1/R2=31, R4=9, R5=9, deployable=4
- SOL: stress_rows=75, R1/R2=28, R4=11, R5=8, deployable=0
- ADA: stress_rows=75, R1/R2=31, R4=8, R5=6, deployable=2

## 추가 500개 후보 기반 walk-forward
0.5% risk basis:
- portfolio avgQ: +0.736%
- positive windows: 7/9
- annualized: +2.98%
- S&P500 quarterly hurdle +2.41% 미달

5% risk basis:
- portfolio avgQ: +7.211%
- positive windows: 7/9
- annualized: +32.12%
- S&P500 quarterly hurdle +2.41% 초과

주의: 추가 500개 후보 기반 WF에서는 SOL deployable 후보가 없었으므로 portfolio 계산은 UNI/NEAR/ADA 중심이다. 기존 3,000-experiment SOL 후보를 자동 폐기하지는 않는다.

## 현재 배포된 4개 고정 전략 walk-forward
현재 `paper_trader_github.py`의 정확한 4개 전략을 고정 파라미터로 다시 검증했다.

0.5% risk basis:
- portfolio avgQ: +1.220%
- positive windows: 7/9
- annualized: +4.97%
- S&P500 quarterly hurdle +2.41% 미달

5% risk basis:
- portfolio avgQ: +12.171%
- positive windows: 7/9
- annualized: +58.31%
- S&P500 quarterly hurdle +2.41% 초과

## 결론
- 보수적 연구 기준 0.5% risk/trade에서는 아직 S&P500을 못 이긴다.
- 현재 paper trader가 쓰는 5% risk/trade 기준으로는 백테스트/워크포워드상 S&P500보다 훨씬 높게 나온다.
- 그러나 5% risk는 공격적이고 변동성이 크다. 실거래 금지, paper only.
- 다음 단계는 keltner_breakout/4h 엔진 추가 또는 현재 4개 포트폴리오 paper monitoring이다.
