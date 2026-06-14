---
title: BOOK ME UP
created: 2026-06-05
type: project
tags: [Android, Kotlin, Jetpack Compose, Firebase]
---

# BOOK ME UP — Android 캘린더 예약 앱

## 개요
사용자의 캘린더 빈 시간을 자동으로 찾아 지인에게 공유하고, 약속을 쉽게 잡을 수 있게 해주는 Android 앱.

## 기술 스택
- **언어**: Kotlin
- **UI**: Jetpack Compose
- **백엔드**: Firebase Firestore, Firebase Auth
- **아키텍처**: MVVM

## 주요 기능
- 구글 캘린더 연동 → 빈 Slot 자동 추출
- Firestore에 Slot 공유 → 지인이 직접 예약
- Busy/Discover 모드 전환
- 실시간 동기화

## 배운 점
- Compose 상태 관리 (remember, key())
- Firestore 쿼리 최적화 (composite index)
- Google Calendar API (observeMyCalendar)

## 관련 링크
- GitHub: [movingredstone/BOOK-ME-UP](https://github.com/movingredstone/BOOK-ME-UP)
- [[ls-electric]] — 동시 진행한 취업 활동
