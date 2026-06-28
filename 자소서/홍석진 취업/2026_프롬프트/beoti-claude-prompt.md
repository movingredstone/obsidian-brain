# 버티(Beoti) 프로젝트 개선을 위한 Claude Code 프롬프트

> **중요: 이 프롬프트는 Claude Code에게 전달할 지시사항입니다. 한 번에 한 기능씩 점진적으로 개선해 주세요.**

---

## 1. 프로젝트 개요

### 1.1 기본 정보
- **프로젝트명**: 버티(Beoti)
- **경로**: `/Users/sam/AndroidStudioProjects/MyApplication/`
- **철학**: "오늘도 버텼다" — 익명 직장인 감정 다이어리. 오늘의 감정을 기록하고 익명으로 공유하며 서로 공감하는 앱.
- **기술스택**: Jetpack Compose + Firebase Auth (이메일/비밀번호 + Google Sign-In) + Firestore + DataStore
- **현재 상태**: Google Sign-In + Firebase Auth 완료, 기본 온보딩 완료, 기본 탭 5개 구현됨 (Today / Feed / Log / Help / Profile)
- **폰트**: Satoshi-Medium TTF (`res/font/satoshi_medium.ttf`)
- **디자인 시스템**: Apple Human Interface Guidelines 기반 — SquircleShape, GlassSurface blur, spring animations, Accent 색상(0xFFE7A33C)

### 1.2 주요 파일 구조
```
app/src/main/java/com/example/myapplication/
├── MainActivity.kt          # AppRoot (BeotiApp), Route 네비게이션, BeotiBottomNav
├── Models.kt                # Mood enum (8종), Entry, Profile, CAUSES, JOBS, REWARD_LINES
├── AuthScreens.kt           # SignInScreen, SignUpScreen, ForgotPasswordScreen, VerifyEmailScreen
├── OnboardingScreen.kt      # 닉네임·직무·연차 설정 + Google 로그인
├── TodayScreen.kt           # 오늘의 감정 기록 (Mood 선택 → 원인 선택 → 텍스트 → 공유여부 → 보상 문구)
├── FeedScreen.kt            # 익명 피드 (LazyColumn, 감정 필터, 공감 리액션)
├── LogScreen.kt             # 감정 통계 (DonutChart, 주간 감정 흐름, 원인 랭킹, 잔디 캘린더)
├── HelpScreen.kt            # 전문가 Q&A
├── ProfileScreen.kt         # 프로필 화면
├── ProfileStore.kt          # DataStore 기반 프로필 저장/로드
├── GoogleAuth.kt            # Google Sign-In + Firebase Auth 구현
├── Components.kt            # BrandGlyph(Canvas 초승달), AmberGlow, BeotiHeader, Cards 등
└── ui/theme/
    ├── Color.kt             # 디자인 토큰 (Accent, Ink, Night, GlassBase, MoodColors 등)
    ├── Type.kt              # 타이포그래피
    ├── Shape.kt             # Shapes (SquircleShape, CardShape, ButtonShape, ChipShape)
    └── Theme.kt             # BeotiTheme (Light/Dark color schemes)
```

---

## 2. 컬러 시스템 (Design Tokens)

절대 직접 Color.copy(RGB 조작)하지 말 것. 아래 정의된 토큰만 사용:

```kotlin
// ── Accents ──
val Accent = Color(0xFFE7A33C)        // 랜턴 앰버, 브랜드 시그니처
val AccentDeep = Color(0xFFD67A1A)    // 어두운 앰버 (강조)
val AccentSoft = Color(0xFFFFF4EB)    // 앰버 배경
val AccentInk = Color(0xFF8B5D15)     // 앰버 텍스트

// ── Brand Ink ──
val Ink = Color(0xFF1B2336)           // 다크 네이비 (본문)
val Ink2 = Color(0xFF2A3447)          // 보조 네이비
val InkSoft = Color(0xFF5B6478)
val InkFaint = Color(0xFF8C94A4)
val InkGhost = Color(0xFFB6BCC8)

// ── Surfaces (Light) ──
val BeotiBg = Color(0xFFFBF7F0)       // 메인 배경 (베이지)
val Surface = Color(0xFFF5EEE1)       // 라이트 크림
val Surface2 = Color(0xFFE9DFD1)      // 어두운 크림
val Surface3 = Color(0xFFD4C4B3)
val Line = Color(0xFFECE6DA)
val Line2 = Color(0xFFE2DBCC)

// ── Night Surfaces ──
val Night = Color(0xFF141A29)         // 다크 배경
val Night2 = Color(0xFF1E2740)
val Night3 = Color(0xFF28324C)
val NightLine = Color(0x1AFFFFFF)
val NightSoft = Color(0x9EFFFFFF)
val NightFaint = Color(0x66FFFFFF)

// ── Glassmorphism ──
val GlassBase = Color(0xB8FBF7F0)     // rgba(251,247,240,.72) — 바텀바 프로스트

// ── Mood Colors (감정별 8종 fg+bg 페어) ──
// 현타(Hyunta), 분노(Anger), 무기력(Lethargy), 억울함(Unfair),
// 웃김(Funny), 뿌듯함(Proud), 그냥버팀(JustHoldingOn), 퇴사마려움(QuitWanted)
// 각각 MoodColors.현타Fg / MoodColors.현타Bg 형태로 접근
```

---

## 3. Mood Enum (Models.kt)

```kotlin
@Serializable
enum class Mood(val key: String, val emoji: String, val fg: Long, val bg: Long) {
    Hyunta("현타", "😶‍🌫️", 0xFF6E7C97, 0xFFE8ECF3),
    Anger("분노", "😤", 0xFFC46B4A, 0xFFF6E3DA),
    Lethargy("무기력", "🫠", 0xFF8B919E, 0xFFECEDF1),
    Unfair("억울함", "😮‍💨", 0xFF8E78BE, 0xFFECE6F5),
    Funny("웃김", "🙃", 0xFFD69A2E, 0xFFF8ECCB),
    Proud("뿌듯함", "🌱", 0xFF549B81, 0xFFDBEDE4),
    JustHoldingOn("그냥버팀", "🪨", 0xFF5E6E91, 0xFFE5E9F2),
    QuitWanted("퇴사마려움", "🏃", 0xFFDA8743, 0xFFF8E5D2);

    val fgColor get() = Color(fg)
    val bgColor get() = Color(bg)
}
```

---

## 4. 주요 Pitfalls (절대 지킬 것)

1. **Row/Column 파라미터 순서**: `Row(Modifier, horizontalArrangement, verticalAlignment)` — 반드시 Modifier가 첫 번째 인자!
2. **Material Icons 확장**: `Icons.Rounded.Info` 같은 건 `material-icons-core`에 없고 `material-icons-extended`에만 있음 → `Icons.Rounded.Person` 등 core 아이콘으로 대체
3. **`coerceIn(min, max)` 크래시**: `min > max`이면 `IllegalArgumentException` 발생 → 사전에 `min <= max` 보정 필수
4. **파일 편집 시 `patch(mode='replace')` 사용**: `write_file`로 전체 파일 덮어쓰지 말 것. `old_string` + `new_string`으로 타겟 수정
5. **`Color.copy(alpha=...)` 외 RGB 직접 조작 금지**: 브랜드 팔레트 깨짐. alpha 변경만 허용. RGB 값 변경 절대 금지.
6. **Compose BOM 2025.02.00은 `fillRule` 미지원**: Canvas Path에 `fillRule` 파라미터 사용하지 말 것
7. **CFF/OTF 폰트 금지**: Compose가 읽지 못함. **무조건 TTF만 사용**
8. **Google Sign-In 연동 시 `google-services.json` 재다운로드 필수**: Firebase Console에서 Google Sign-In 활성화 후 반드시 새로 받을 것

---

## 5. 개선 요청 사항 (순차적으로 하나씩 진행)

### 5.1 Firestore 연동 — Entry 저장/조회

**목표**: 오늘의 감정 기록(`Entry`)을 Firestore에 저장하고 조회한다.

**Firestore 구조**:
- Collection: `entries`
- 문서 ID: `userId + "_" + timestamp` (자동 생성 또는 UUID)
- 필드:
  ```
  userId: String        // Firebase Auth uid
  mood: String          // Mood enum name (e.g., "Hyunta")
  causes: List<String>  // 선택된 원인 목록 (e.g., ["상사", "업무량"])
  text: String          // 감정 텍스트
  share: Boolean        // 익명 공유 여부
  timestamp: Long       // System.currentTimeMillis()
  reward: String        // 보상 문구
  authorNick: String    // 익명 닉네임
  authorJob: String     // 직무 (e.g., "개발")
  authorYear: String    // 연차 (e.g., "2–3년차")
  ```

**구현 가이드**:
- `FirebaseFirestore.getInstance()` 로 Firestore 인스턴스 획득
- `TodayScreen.kt`의 기록 저장 버튼에서 `entries` 컬렉션에 `add()` 또는 `set()` 호출
- 저장 후 Toast로 "기록 저장 완료" 표시
- `LogScreen.kt`에서 현재 사용자의 Entry를 `whereEqualTo("userId", uid)`로 조회하여 통계 계산

**중요**: Firestore 보안 규칙은 추후 설정한다고 가정하고, 지금은 클라이언트에서 직접 읽기/쓰기 허용 (`allow read, write: if true;`) 상태라고 가정한다.

---

### 5.2 Firebase Auth — 이메일 인증 후 자동 프로필 저장

**목표**: 이메일/비밀번호 회원가입 후 이메일 인증이 완료되면 자동으로 기본 프로필을 Firestore에 저장한다.

**구현 가이드**:
- `AuthScreens.kt`의 `SignUpScreen`에서 회원가입 성공 시 Firestore `profiles` 컬렉션에 사용자 문서 생성
- `profiles` 컬렉션 구조:
  ```
  userId: String
  email: String
  nick: String        // 기본 랜덤 닉네임 (makeNick() 사용)
  job: String         // 기본값 "" (온보딩에서 설정)
  year: String        // 기본값 ""
  field: String       // 기본값 ""
  verified: Boolean   // true
  createdAt: Timestamp
  ```
- `VerifyEmailScreen`에서 인증 완료 콜백 시 `Onboarding`으로 이동하기 전에 프로필 저장

---

### 5.3 감정 통계 화면(LogScreen) 개선

**목표**: 현재 더미 데이터 기반인 LogScreen을 실제 Firestore 데이터 기반으로 개선하고, 주간/월간 차트와 연속 기록일(Streak)을 표시한다.

**구현 사항**:
1. **주간 감정 차트**: 현재 주의 요일별 감정을 Firestore에서 `userId`로 조회하여 실제 데이터로 대체
2. **월간 감정 분포 파이차트**: 이번 달 Entry에서 Mood별 카운트를 집계하여 `DonutChart`에 반영
3. **연속 기록일(Streak)**: 오늘부터 역순으로 며칠 연속 기록했는지 계산하여 표시. `getStreakCheer(n)` 함수 활용 (Models.kt에 이미 정의됨)
4. **원인 랭킹**: 실제 데이터 기반 `BarRow` 표시
5. **잔디 캘린더**: 더미 `random()` → 실제 기록 날짜 기반 색상 채우기

**코드 예시 (Streak 계산)**:
```kotlin
fun calculateStreak(entries: List<Entry>): Int {
    val sortedDates = entries.map { 
        java.time.Instant.ofEpochMilli(it.timestamp)
            .atZone(java.time.ZoneId.systemDefault())
            .toLocalDate()
    }.distinct().sortedDescending()
    
    if (sortedDates.isEmpty()) return 0
    
    var streak = 1
    var current = java.time.LocalDate.now()
    
    // 오늘 기록이 없으면 어제부터 체크
    if (sortedDates[0] != current) {
        current = current.minusDays(1)
        if (sortedDates[0] != current) return 0
    }
    
    for (i in 1 until sortedDates.size) {
        val expected = current.minusDays(i.toLong())
        if (sortedDates[i] == expected) streak++ else break
    }
    return streak
}
```

---

### 5.4 익명 피드(FeedScreen) 개선

**목표**: 현재 하드코딩된 `INITIAL_FEED`를 Firestore 기반 실시간 피드로 전환하고, 무한스크롤과 공감 기능을 추가한다.

**구현 사항**:
1. **Firestore 쿼리**: `entries` 컬렉션에서 `share == true`인 문서만 `orderBy("timestamp", DESCENDING)`로 조회
2. **무한스크롤**: `LazyColumn` + `snapshotFlow`로 마지막 아이템 감지 → `startAfter(lastDocument)`로 페이지네이션
3. **공감(Reactions)**: 각 Post에 `reactions` 서브컬렉션 또는 Map 필드 추가. 사용자가 리액션 탭하면 Firestore에 `arrayUnion`/`arrayRemove`로 토글
4. **익명 표시**: 작성자 정보를 `authorNick`, `authorJob`, `authorYear`로 표시

**Firestore 쿼리 예시**:
```kotlin
// FeedScreen에서
var feedEntries by remember { mutableStateOf<List<Entry>>(emptyList()) }
var lastDoc by remember { mutableStateOf<DocumentSnapshot?>(null) }
var isLoadingMore by remember { mutableStateOf(false) }

fun loadFeed() {
    val query = FirebaseFirestore.getInstance()
        .collection("entries")
        .whereEqualTo("share", true)
        .orderBy("timestamp", Query.Direction.DESCENDING)
        .limit(20)
    
    query.get().addOnSuccessListener { snapshot ->
        feedEntries = snapshot.toObjects(Entry::class.java)
        lastDoc = snapshot.documents.lastOrNull()
    }
}

fun loadMore() {
    if (isLoadingMore || lastDoc == null) return
    isLoadingMore = true
    val query = FirebaseFirestore.getInstance()
        .collection("entries")
        .whereEqualTo("share", true)
        .orderBy("timestamp", Query.Direction.DESCENDING)
        .startAfter(lastDoc!!)
        .limit(20)
    
    query.get().addOnSuccessListener { snapshot ->
        feedEntries = feedEntries + snapshot.toObjects(Entry::class.java)
        lastDoc = snapshot.documents.lastOrNull()
        isLoadingMore = false
    }
}
```

---

### 5.5 FCM 푸시 알림 — 매일 저녁 8시 리마인더

**목표**: Firebase Cloud Messaging을 통해 매일 저녁 8시 "오늘 하루 어땠나요?" 리마인더를 보낸다.

**구현 가이드**:
1. **Firebase Console 설정**:
   - 프로젝트 설정 → 클라우드 메시징 → FCM 서버 키 발급
   - `google-services.json` 재다운로드
2. **Android 클라이언트**:
   - `FirebaseMessagingService`를 상속하는 `BeotiFCMService.kt` 생성
   - `AndroidManifest.xml`에 서비스 등록 및 `POST_NOTIFICATIONS` 권한 추가
   - `onNewToken`에서 FCM 토큰을 Firestore `users/{uid}` 문서의 `fcmToken` 필드에 저장
3. **알림 채널**: "beoti_reminder" 채널 생성 (Android 8.0+)
4. **스케줄링**: Firebase Cloud Functions 또는 로컬 WorkManager 사용
   - **권장**: 로컬 `WorkManager` + `PeriodicWorkRequest` (24시간 주기, 저녁 8시 타겟)
   - FCM 토픽 구독(`/topics/daily_reminder`) 후 Cloud Functions에서 Pub/Sub 스케줄러로 전송

**코드 구조 예시**:
```kotlin
// BeotiFCMService.kt
class BeotiFCMService : FirebaseMessagingService() {
    override fun onNewToken(token: String) {
        super.onNewToken(token)
        // Firestore users/{uid}에 fcmToken 저장
        val uid = FirebaseAuth.getInstance().currentUser?.uid ?: return
        FirebaseFirestore.getInstance()
            .collection("users").document(uid)
            .update("fcmToken", token)
    }

    override fun onMessageReceived(message: RemoteMessage) {
        super.onMessageReceived(message)
        val channelId = "beoti_reminder"
        val notificationManager = getSystemService(NOTIFICATION_SERVICE) as NotificationManager
        
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val channel = NotificationChannel(
                channelId, "버티 리마인더",
                NotificationManager.IMPORTANCE_DEFAULT
            )
            notificationManager.createNotificationChannel(channel)
        }
        
        val notification = NotificationCompat.Builder(this, channelId)
            .setSmallIcon(R.drawable.ic_launcher_foreground)
            .setContentTitle("오늘도 버텼나요?")
            .setContentText(message.data.getOrDefault("body", "오늘 하루 어땠나요? 기록을 남겨보세요."))
            .setAutoCancel(true)
            .build()
        
        notificationManager.notify(1001, notification)
    }
}
```

---

### 5.6 다크모드 지원

**목표**: `BeotiTheme`에 다크모드를 추가하여 시스템 다크모드 설정에 연동한다.

**현재 상태**: `Theme.kt`에 `DarkColorScheme`이 이미 정의되어 있고 `Night` 계열 색상 변수도 존재함. `BeotiTheme(darkTheme = isSystemInDarkTheme())`으로 파라미터만 받고 있음.

**구현 사항**:
1. **컴포넌트별 다크모드 대응**: `BeotiBg` (Light) / `Night` (Dark) 전환을 위해 `MaterialTheme.colorScheme.background` 사용
2. **TodayScreen 배경**: 현재 `BeotiBg` 하드코딩 → `MaterialTheme.colorScheme.background`로 변경
3. **FeedScreen 배경**: `BeotiBg` → `MaterialTheme.colorScheme.background`
4. **LogScreen 배경**: `BeotiBg` → `MaterialTheme.colorScheme.background`
5. **HelpScreen / ProfileScreen**: 동일하게 배경색 전환
6. **Bottom Nav 프로스트 글래스**: 다크모드일 때 `GlassBase`를 `Night.copy(alpha=0.72f)`로 변경
7. **텍스트 색상**: `Ink`, `InkSoft` 등 직접 참조 대신 `MaterialTheme.colorScheme.onBackground`, `MaterialTheme.colorScheme.onSurfaceVariant` 사용을 권장하나, 브랜드 컬러 유지를 위해 필요 최소한만 전환

**Bottom Nav 다크모드 대응 예시**:
```kotlin
val isDark = isSystemInDarkTheme()
val glassBg = if (isDark) Night.copy(alpha = 0.72f) else GlassBase
```

---

### 5.7 프로필 통계 표시

**목표**: ProfileScreen에 Firestore 데이터 기반 통계를 표시한다.

**Profile 데이터 모델 확장** (Models.kt):
```kotlin
@Serializable
data class Profile(
    val nick: String,
    val job: String,
    val year: String,
    val field: String,
    val verified: Boolean = false,
    // 통계 필드 (Firestore 집계 or 클라이언트 계산)
    val totalDays: Int = 0,       // 총 기록일 수
    val streak: Int = 0,          // 현재 연속 기록일
    val topMood: String = "",     // 가장 많이 기록한 감정 (한글명)
    val empathyReceived: Int = 0  // 받은 공감 총 횟수
)
```

**구현 사항**:
1. `ProfileScreen.kt`에서 Firestore `entries` 컬렉션을 `userId`로 조회하여 통계 계산
2. 표시할 통계:
   - **총 기록일**: `entries`의 distinct 날짜 수
   - **연속 기록일**: `calculateStreak()` 함수 결과
   - **가장 많은 감정**: Mood별 count 집계 후 최빈값
   - **받은 공감 수**: `reactions` 필드 합산 또는 별도 카운트
3. 통계 카드 UI: 기존 `StatItem` 컴포넌트 재활용

---

## 6. Claude Code 작업 지시사항

### 6.1 절대 원칙

- **절대 전체 리팩토링 하지 말 것** — 한 번에 한 기능씩 점진적으로 개선
- **한 작업당 한 파일 범위 내에서 완료할 것** — 여러 파일을 동시에 수정해야 하면 명시적으로 보고 후 진행
- **매 작업 완료 후 `./gradlew assembleDebug` 빌드 검증 필수**
- **파일 편집은 `patch(mode='replace')` 사용**: `old_string`과 `new_string`을 정확히 매칭하여 수정. 절대 `write_file`로 전체 덮어쓰기 하지 말 것
- **`Color.copy(RGB 조작)` 절대 금지**: `Color.copy(alpha=...)` 형태의 alpha 변경만 허용
- **기존 애니메이션/디자인 톤 유지**: Apple HIG 기반 spring animations, SquircleShape, GlassSurface blur 등 유지
- **기존 컴포넌트 재활용**: `BeotiHeader`, `StaggeredItem`, `MoodTag`, `FeedCard`, `ReactionPill`, `DonutChart`, `BarRow`, `StatItem`, `InsightCard` 등

### 6.2 작업 순서 권장

아래 순서로 하나씩 진행하세요. 각 단계 완료 후 빌드 검증까지 완료해야 다음 단계로 넘어갑니다.

1. **Firestore 연동** (5.1) — 가장 기초가 되는 데이터 레이어
2. **이메일 인증 후 프로필 저장** (5.2) — Auth + Firestore 연결
3. **LogScreen 통계 개선** (5.3) — 실제 데이터 기반 차트
4. **FeedScreen Firestore 전환** (5.4) — 실시간 피드
5. **FCM 푸시 알림** (5.5) — 클라이언트 + WorkManager
6. **다크모드 지원** (5.6) — 테마 확장
7. **프로필 통계** (5.7) — 통계 카드 추가

### 6.3 빌드 검증 명령어

```bash
cd /Users/sam/AndroidStudioProjects/MyApplication
./gradlew assembleDebug
```

### 6.4 Kotlin/Compose 코딩 컨벤션

- Compose 함수는 `@Composable` 어노테이션, `PascalCase`
- Composable 파라미터 순서: 필수 파라미터 → `Modifier` (기본값 `Modifier`) → 콜백 → `@Composable content`
- `Row`/`Column` 파라미터 순서: `Modifier`, `horizontalArrangement`/`verticalArrangement`, `verticalAlignment`/`horizontalAlignment`
- `remember`, `LaunchedEffect`, `mutableStateOf` 적극 활용
- `kotlinx.coroutines` 사용 (Firestore callback → `suspend`/`await()` 패턴 권장)
- Firebase 연산은 `try-catch`로 감싸고 사용자에게 Toast로 피드백

### 6.5 현재 gradle 의존성 참고

Firebase 관련 의존성이 이미 `build.gradle.kts`에 포함되어 있을 가능성이 높습니다. 새 의존성 추가가 필요하면 다음과 같이 추가:
```kotlin
// app/build.gradle.kts
implementation(platform("com.google.firebase:firebase-bom:33.0.0"))
implementation("com.google.firebase:firebase-firestore-ktx")
implementation("com.google.firebase:firebase-messaging-ktx")
implementation("androidx.work:work-runtime-ktx:2.9.0")
```

---

## 7. 작업 시작 전 확인사항

Claude Code가 이 프롬프트를 받으면 가장 먼저 해야 할 일:
1. `/Users/sam/AndroidStudioProjects/MyApplication/` 디렉토리 존재 확인
2. `app/build.gradle.kts`에서 현재 의존성 목록 확인
3. `MainActivity.kt`의 전체 구조 파악 (Route, Navigation)
4. 위 Pitfalls(4번 섹션)을 숙지
5. **"어떤 기능부터 시작할까요?"라고 사용자에게 확인 후 첫 작업 시작**

---

*이 프롬프트는 2026년 6월 28일 기준 버티 프로젝트 상태를 반영합니다.*
