# RU_SHAMPOO — Source 로그

> 접근일시: 2026-09-01 (동일 세션 내)
> 주요 운영사: **Wildberries** (마켓플레이스), **eapteka.ru** (러시아 온라인 약국)
> Ozоn·Yandex·Bing은 CAPTCHA/봇차단 실측 (§3.5) → Wildberries API + eapteka 채널로 전환.

| # | URL | 접근일시 | 확인내용 | 운영사 |
|---|---|---|---|---|
| 1 | https://search.wb.ru/exactmatch/ru/common/v4/search?query=детский шампунь&resultset=catalog&sort=popular | 2026-09-01 | детский шампунь 카탈로그 인기정렬 100개 수신. 제품명·브랜드·rating·feedbacks(리뷰수)·가격 추출 | Wildberries (마켓플레이스) |
| 2 | https://www.wildberries.ru/catalog/536097594/detail.aspx | 2026-09-01 | Ла-Кри Шампунь-пенка 0+ 150ml, 420₽, 리뷰1497, r5.0 | Wildberries |
| 3 | https://www.wildberries.ru/catalog/171576712/detail.aspx | 2026-09-01 | Lulu бессульфатный для новорожденных, 396₽, 리뷰1743(최다), r5.0 | Wildberries |
| 4 | https://www.wildberries.ru/catalog/659345783/detail.aspx | 2026-09-01 | Johnson's Baby ромашка 300ml, 382₽, 리뷰316, r5.0 | Wildberries |
| 5 | https://www.wildberries.ru/catalog/542301348/detail.aspx | 2026-09-01 | Принцесса Калинка-Малинка 400ml, 358₽, 리뷰508, r5.0 | Wildberries |
| 6 | https://www.wildberries.ru/catalog/169049429/detail.aspx | 2026-09-01 | Лапочка мягкий 400ml, 304₽, 리뷰182, r5.0 | Wildberries |
| 7 | https://www.eapteka.ru/search/?q=Ла-Кри+шампунь | 2026-09-01 | **Crossref**: Ла-Кри Шампунь-пенка 0+ 150ml **421₽** (WB 420₽와 일치). itemId 227398·234690 | eapteka.ru (온라인 약국) |
| 8 | https://www.eapteka.ru/search/?q=Лапочка+шампунь | 2026-09-01 | Лапочка Мягкий Шампунь 400ml 등록 확인(itemId 521129), **품절(itemStock=false, itemPrice=none)** — 약국 가격 미확인 | eapteka.ru |
| 9 | https://www.eapteka.ru/search/?q=Johnson%27s+Baby+шампунь | 2026-09-01 | 약국 카탈로그에서 Johnson's 대신 littleyogi 샴푸 등 노출 — Johnson's 화장품 샴푸 약국 섹션 분류상 크로스체크 미확보 | eapteka.ru |

**제한 명시 (§5.1):** 판매량 순위 POS/NielsenIQ/Euromonitor 실자료 없음. 리뷰수(feedbacks)를 프록시로 사용. 각 리테일러 페이지 접근일시 미기록은 도구 스냅샷 한계(상기 동일 세션 날짜로 대체).

**접근 불가 (§3.4):** ozon.ru(연결오류/CAPTCHA), yandex.ru(CAPTCHA), bing.com(검색결과 미렌더), wildberries.ru 브라우저 페이지(빈 페이지) → Wildberries 공개 search API로 우회, eapteka HTTP 200으로 대체. 로그인/구매/결제/개인정보 접근 없음.
