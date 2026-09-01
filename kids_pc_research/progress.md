# Kids Personal Care 3국 시장조사 — Progress

**시작:** 2026-09-01
**총괄:** Claude Code (기획·분할·통합·최종QA)
**수집 워커:** DeepSeek (Hermes CLI, `hermes -z`) — 토큰 집약 작업
**검증 워커:** Codex — Source·수치·표기 검증
**실행 모드:** 병렬 (사용자 지시로 §3.1 순차 규칙 override)

---

## 역할 분담

| 주체 | 담당 |
|---|---|
| Claude Code | Research Plan, 스키마 확정, Task 분할, 결과 통합, 최종 분석(§10~13), 최종 QA(§15), Excel 산출 |
| DeepSeek ×6 | 시장별 Long List(Tier A) + Top5 Proxy 심층(Tier B) 수집, sources 기록 |
| Codex ×1 | §15 QA 체크리스트 검증, 가격환산 재계산, Source 중복계산 적발, Top5=MarketShare 오표기 적발 |

**모델 임의 전환 금지.** 총괄은 Claude Code 고정.

---

## 6개 시장 (병렬)

| # | 시장 코드 | 국가 | 카테고리 | 상태 | Long List | Top5 | 담당 |
|---|---|---|---|---|---|---|---|
| 1 | RU_SHAMPOO | 러시아 | Kids Shampoo | ✅ 완료 | 12 | 5 | DeepSeek-1 |
| 2 | RU_BODYWASH | 러시아 | Kids Body Wash | 🟡 수집중 | - | - | DeepSeek |
| 3 | KZ_SHAMPOO | 카자흐스탄 | Kids Shampoo | 🟡 수집중 | - | - | DeepSeek |
| 4 | KZ_BODYWASH | 카자흐스탄 | Kids Body Wash | 🟡 수집중 | - | - | DeepSeek |
| 5 | UZ_SHAMPOO | 우즈베키스탄 | Kids Shampoo | 🟡 수집중 | - | - | DeepSeek |
| 6 | UZ_BODYWASH | 우즈베키스탄 | Kids Body Wash | 🟡 수집중 | - | - | DeepSeek |
| 7 | CROSS_QA | — | 전체 검증 | ⬜ 대기(deps) | — | — | Codex |
| 8 | SYNTHESIS | — | 최종 분석·Excel | ⬜ 대기 | — | — | Claude Code |

**진척률: 2 / 8 (25%)** — 기획·스키마·Run·Task·워커기동 완료. 6개 시장 수집 진행중.

---

## Orca Orchestration 상태

- **Run:** `run_41465fab11ab`
- **Coordinator:** Claude Code (`term_df501086`)
- **워커 매핑:** `/tmp/worker_map.txt`

| 시장 | Task | Terminal |
|---|---|---|
| RU_SHAMPOO | task_a6c3dc628cb2 | term_0bb7abbb |
| RU_BODYWASH | task_ed52599f1218 | term_0ae69314 |
| KZ_SHAMPOO | task_aa47eda0efa3 | term_24d40bc3 |
| KZ_BODYWASH | task_7dbef87bc171 | term_a430645a |
| UZ_SHAMPOO | task_77359cb119c8 | term_3573c057 |
| UZ_BODYWASH | task_fa2f9dda07d4 | term_5565fee1 |
| CROSS_QA | task_b14026b21689 | (deps 대기) |

---

## 알려진 제약 (실측)

1. **hermes `--agent` TUI 주입 실패** — 124줄 프롬프트 injection이 `agent_prompt_stalled`로 6/6 실패.
   → bare shell + `hermes --yolo -z "$(cat prompts/{시장}.txt)"` oneshot 경로로 전환 (가이드 지원 경로).

2. **hermes `web` 툴셋 비활성** — EXA/TAVILY/PARALLEL/FIRECRAWL API 키 전부 미설정.
   → 워커는 **web search API 사용 불가**. `browser` 툴셋(Playwright Chromium)으로 Yandex/Google 검색 후 상품페이지 직접 접근.
   → 수집 속도·커버리지에 영향. Long List가 8개 미만이면 이 제약이 원인일 수 있음.

3. **DeepSeek 401 (해결됨)** — `model.base_url`이 Codex 엔드포인트(`chatgpt.com/backend-api/codex`)에 고정되어 있어 DeepSeek 키가 401.
   → `https://api.deepseek.com`로 수정, `model.default=deepseek-chat`. `hermes -z` PONG 응답 확인.

---

## 시장당 예산 상한 (§3.2)

- 검색/페치 합계: **25회**
- Long List: **8~12개** (억지로 채우지 말 것)
- Top 5 심층조사 툴콜: **15회**

초과 시 현 상태로 마감. 확보 가능한 실제 수를 기록.

---

## 사이트 접근성 (§3.5 — 실측)

| 사이트 | 상태 | 대응 |
|---|---|---|
| kaspi.kz | fetch 가능 | KZ 1차 수집원 |
| ozon.ru | robots 차단 | 스니펫에서 평점·리뷰수만. 가격은 Chrome/앵커채널 |
| uzum.uz | JS 렌더링 | Chrome 필수 |
| wildberries.ru | 부분 차단 | 스니펫 의존 |
| oxymed.uz | fetch 가능 | UZ 유일 원격조회 채널 (약국 120지점) |
| cosmart.kz / pharmaclick.uz | JS | 조회 불가 |

**판매량순 정렬 = 3국 모두 로그인 필요 → 불가.** 리뷰수를 프록시로 쓰고 그 사실 명시.

**Fallback:** 핵심 Marketplace가 Web/Search로 미검증 시 → Windows Hermes + cua-driver로 실제 Windows Chrome 사용. 근거는 URL·접근일시·확인내용과 함께 `raw_data/sources/` 보존.

---

## 로그

| 시각 | 이벤트 |
|---|---|
| 2026-09-01 | 프로젝트 폴더 생성, progress.md·스키마 생성 |
| 2026-09-01 | RU_SHAMPOO 완료 (DeepSeek-1): longlist 12·top5 5·sources 기록. 채널: Wildberries 공개 search API (`search.wb.ru/.../v4/search?sort=popular`) HTTP 200 성공 — 브라우저 차단 우회. eapteka.ru 약국 크로스체크(Ла-Кри 421₽ 일치) |
