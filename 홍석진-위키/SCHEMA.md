---
title: Wiki Schema
created: 2026-06-03
updated: 2026-06-03
type: meta
---

# Wiki Schema — 홍석진 Career Wiki

## Domain
홍석진의 커리어, 자기소개서, 면접, 이력서, 경험을 체계화한 개인 지식 베이스.
국내 대기업(현대, 한화, GS, 기아, KT&G 등) 해외영업/사업개발 직무 지원 자료.

## Conventions
- 파일명: 영문 lowercase + hyphens (예: `hyundai-mobis.md`)
- 한국어 콘텐츠는 한국어 그대로 유지
- 모든 페이지는 YAML frontmatter 필수
- `[[wikilinks]]`로 페이지 간 연결 (페이지당 최소 2개 아웃바운드 링크)
- 새 페이지 생성 시 `index.md`에 추가
- 모든 작업은 `log.md`에 기록

## Frontmatter Template
```yaml
---
title: 페이지 제목
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: company | role | experience | project | interview | resume | career | cert | education | knowledge
tags: [tag1, tag2]
companies: [연관회사]
roles: [연관직무]
skills: [보유스킬]
sources: [raw/applications/YYYY/source-file.pdf]
---
```

## Tag Taxonomy
- 회사유형: 대기업, 중견기업, 공기업, 스타트업
- 직무: 해외영업, 사업개발, 사업기획, 마케팅, 물류, 공급망
- 산업: 자동차, 에너지, 석유화학, 방산, 항공, 건설, IT, 금융, 무역
- 스킬: 협상, 가격전략, 시장분석, PT발표, 데이터분석
- 언어: 영어, 중국어, 일본어
- 경험유형: 인턴, 정규직_경력, 프로젝트, 학술
- 지역: 국내, 해외, 동남아, 중동, 유럽
- 면접: PT면접, 역량면접, 임원면접, 영어면접

## Page Thresholds
- **Create**: 회사/직무/경험이 2개 이상 문서에 등장하거나 하나의 문서에서 핵심일 때
- **Update**: 기존 페이지에 새 정보가 있을 때
- **Don't create**: 단순 언급만 있는 경우
- **Split**: 200줄 초과 시 하위 페이지로 분할

## Update Policy
- 상충 정보 발견 시: 두 주장 모두 날짜와 함께 기록
- `contradictions: [page-name]` 프론트매터에 표시
- 사용자 검토 플래그
