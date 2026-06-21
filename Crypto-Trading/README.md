# Crypto Trading System

> 마지막 업데이트: 2026-06-21
> 담당 AI: Hermes Agent (DeepSeek v4)
> 프로젝트 경로: ~/Desktop/hermes/investmentsystem

## 개요

암호화폐 선물 트레이딩을 위한 체계적인 백테스트/최적화 파이프라인.
7개 코인 검증 완료, 3개 코인 포트폴리오 선정.

## 퀵 링크

- [[Pipeline]] — 전체 최적화 파이프라인
- [[Strategies]] — 코인별 전략 상세
- [[Glossary]] — PF, WR, WF 등 용어
- [[Architecture]] — 자동화 설계
- [[Current-State]] — 현재 상태 & 다음 할 일

## 주요 발견

1. **AI는 라이브 트레이딩에 불필요** — 모든 시그널/포지션 계산이 순수 산수
2. **regime 필터가 생명** — 제거 시 PF 1.26→0.99로 붕괴
3. **주식 멀티팩터는 WF 탈락** — 강세장에서 타이밍이 buy-and-hold보다 못함
4. **12개월 training은 부족** — 18개월+ 필요 (과최적화 발견)
5. **BTC vwap_pullback이 overfitting** — 확장 training에서 발견
6. **고변동 코인일수록 stress survivor 증가**

## 선정된 포트폴리오 ($330, 페이퍼 트레이딩)

| Coin | Price | Strategy | PF | WR | WF | Alloc | Risk |
|------|-------|----------|----|----|----|----|------|
| DOGE | $0.08 | macd_momentum/8h | 1.99 | 67% | 3/3 | $110 | 5% |
| SUI | $0.90 | macd_momentum/4h | 2.54 | 48% | 2/3 | $110 | 5% |
| AVAX | $6.23 | trend_pullback/8h | 1.90 | 45% | 3/3 | $110 | 5% |

## GitHub Actions (페이퍼 트레이딩)

- `paper_signal.py`: 독립형 시그널 체커
- `.github/workflows/signal.yml`: 4시간마다 실행
- 무료 (월 1.5시간 사용), 컴퓨터 OFF 가능
- [[Current-State]] 참고

## 포지션 사이징 공식

```
position_size = (capital × risk%) / stop_distance%
leverage = position_size / capital
```

$110, 5% risk, 3.5% stop → $157 position, 1.4x leverage
**AI 불필요. 곱하기 나누기.**

## 파일 구조

```
~/Desktop/hermes/investmentsystem/
├── main.py                  # CLI: fold-eval, optimize, tvt, paper
├── config.yaml              # 기본 설정 (1% risk)
├── config_2pct.yaml         # 2% risk 설정
├── src/
│   ├── research_engine.py   # 백테스트 엔진, 전략 로직
│   ├── fold_evaluator.py    # 7-fold 평가 (source_top_path, focus_override 지원)
│   ├── tvt_evaluator.py     # Train/Val/Test forward 검증
│   ├── optimizer.py         # multi-stage 최적화 (broad→stress→refine)
│   ├── paper_trader.py      # 페이퍼 트레이딩 (--mode baseline|optimized)
│   ├── stock_factors.py     # 주식 멀티팩터 (실패)
│   ├── regime_classifier.py # 8-regime 분류기
│   └── binance_data.py      # Binance 데이터 로더
├── scripts/
│   ├── crypto_signals.py    # 3코인 통합 시그널 체커
│   ├── final_verify.py      # 6-fold walk-forward 검증
│   ├── sui_pipeline.py      # SUI 전체 파이프라인
│   ├── doge_broad.py        # DOGE broad search
│   ├── fast_5coins.py       # 5코인 빠른 파이프라인
│   ├── stock_pipeline.py    # 주식 파이프라인
│   └── verify1/2/3          # 독립 검증 스크립트
└── results/
    ├── optimization/        # broad + stress 결과
    ├── tvt/                 # TVT 검증 결과
    └── paper/               # 페이퍼 트레이딩 결과
```
