---
title: 부동산 가격 예측 AI 어시스턴트
created: 2026-06-28
updated: 2026-06-28
type: project-plan
tags: [부동산, 시계열예측, TimesFM, 멀티에이전트, Hermes-Agent]
---

# 🏠 부동산 가격 예측 AI 어시스턴트

## 프로젝트 개요

대한민국 부동산 실거래가 + 경제지표 + 유동인구 데이터를 기반으로 한 **멀티에이전트 AI 예측 시스템**. Hermes Agent가 n8n 없이 직접 오케스트레이션.

## 아키텍처

```
너(질문) → 👤 Hermes Agent (Orchestrator)
              ├── 🏡 Property Search Agent (RAG + ChromaDB)
              ├── 📡 Data Collection Agent (API 수집)
              ├── 📊 Market Analysis Agent (지표→파생변수)
              ├── 🔮 Prediction Engine (TimesFM 2.5 + XGBoost)
              ├── 🚨 Alert Agent (급등/조건매물 알림)
              └── 📝 Report Agent (주간/월간 리포트)
```

## 핵심 ML 모델

- **TimesFM 2.5** (Google Research) — 시계열 파운데이션 모델
  - 200M 파라미터, 16K 컨텍스트, 맥북 MPS 지원
  - XReg로 금리·유동인구 등 외부 변수 주입 가능
  - LoRA 파인튜닝으로 한국 부동산 맞춤
  - Quantile 예측: "70% 확률로 4.8~5.2억"
  - `pip install timesfm[torch]`

## 필요한 API Key

| 순서 | API | 발급처 | 상태 |
|------|-----|--------|:--:|
| 1 | 국토교통부 실거래가 | data.go.kr → 활용신청 | ⏳ 발급 필요 |
| 2 | 한국은행 ECOS | ecos.bok.or.kr → 인증키 신청 | ⏳ 발급 필요 |
| 3 | 서울 생활인구 | data.seoul.go.kr | 🔮 추후 |
| 4 | 통계청 KOSIS | kosis.kr | 🔮 추후 |

## 데이터 소스

- **거래:** 국토부 실거래가 API (14개 엔드포인트, data.go.kr)
- **경제:** 한국은행 ECOS (기준금리·대출금리·M2 — 샘플키 작동 확인 ✅)
- **유동인구:** 서울 열린데이터광장 생활인구 API ✅
- **시세:** KB부동산, 호갱노노 (크롤링)
- **지역:** 카카오맵 API, 서울 열린데이터

## 기술 스택

| 컴포넌트 | 기술 |
|----------|------|
| Orchestrator | Hermes Agent (native) |
| Web UI | Streamlit |
| Voice | 11 Labs (선택) |
| Vector DB | ChromaDB |
| Time-series DB | TimeScaleDB |
| Relational DB | PostgreSQL |
| Cache | Redis |
| Model Registry | MLflow |
| File Storage | MinIO / Parquet |
| 알림 | Telegram Bot |

## 구현 로드맵

### 1단계: API 수집 ◻️
- [ ] data.go.kr 회원가입 → 활용신청
- [ ] ecos.bok.or.kr 회원가입 → 인증키 신청
- [ ] Hermes cronjob: 매일 08:00 데이터 수집

### 2단계: 저장 + 분석 ◻️
- [ ] TimeScaleDB + PostgreSQL 구축
- [ ] Feature Engineering 파이프라인
- [ ] 대시보드: 지역별 히트맵

### 3단계: 예측 모델 ◻️
- [ ] TimesFM 2.5 설치 + 기본 예측
- [ ] XReg: 금리·유동인구·공급량
- [ ] LoRA 파인튜닝 (한국 부동산)

### 4단계: 서비스화 ◻️
- [ ] Streamlit 대시보드
- [ ] Property Search (자연어 → 매물 검색)
- [ ] Telegram 알림봇
- [ ] 주간 리포트 자동 생성

## 확장 아이디어

- **Property Search:** "강남 1억대 투룸 찾아줘" → ChromaDB + LLM
- **유동인구 분석:** 서울 생활인구 API → 역세권 평가
- **비트코인 예측:** 동일한 TimesFM 파이프라인, XReg만 교체
- **n8n 불필요:** Hermes가 직접 오케스트레이션 (드래그앤드롭보다 강력)

## 연관 파일

- 아키텍처 다이어그램: `~/Desktop/realestate-prediction-architecture.html`
- 참고 영상: [Jarvis AI Assistant with n8n](https://www.youtube.com/watch?v=KUvSzvFeZls)
- TimesFM: https://github.com/google-research/timesfm

---
*마지막 업데이트: 2026-06-28*
