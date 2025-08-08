📘 프론트엔드 수업 요약 – new.html + Flex vs Grid 한 장 정리
────────────────────────────────────────────────────────────

[1] 페이지(new.html) 개요
- HTML5 문서: <!DOCTYPE html>, <html lang="ko">로 한국어 문서 지정
- <head>: UTF-8, 모바일 대응 뷰포트, <title>FrontEnd</title>, 파비콘(/images/favicon.png)
- 전역 스타일:
  • html, body 여백 초기화 (margin:0; padding:0)
  • * { text-align:center } 로 텍스트 중앙 정렬
  • header, footer: 동일 배경색 / 높이 100px
  • main: CSS Grid 2열 레이아웃 (grid-template-columns: 100px auto)
  • main 높이: calc(100vh - 200px) → 헤더·푸터 제외한 영역을 꽉 채움
- 문서 뼈대(의미론적 태그): header / main(aside + section) / footer
- <script>는 자리만 잡아둔 상태(향후 DOM 조작, 이벤트 처리용)

[2] HEAD 영역 핵심
- <!DOCTYPE html> : HTML5 렌더링 지시
- <html lang="ko"> : 접근성·SEO 측면의 기본 언어 설정
- <meta charset="UTF-8"> : 한글 깨짐 방지
- <meta name="viewport" content="width=device-width, initial-scale=1.0">
  → 모바일 화면에서 1:1 비율 유지
- <link rel="icon" href="/images/favicon.png"> : 브라우저 탭 아이콘

[3] 스타일(CSS) 핵심 포인트
- 리셋: html, body { margin:0; padding:0; }
- 공통 텍스트 정렬: * { text-align:center; }
- 헤더/푸터 공통: 배경색 + height:100px
- 메인 레이아웃: Grid 사용
  • display:grid
  • grid-template-columns: 100px auto (좌: 고정 100px, 우: 남는 공간)
  • height: calc(100vh - 200px)

[4] BODY 구조(레이아웃)
- <header> : 최상단 영역(로고/전역 네비 등)
- <main>   : 주 콘텐츠 컨테이너
  • <aside>   : 보조 영역(사이드 네비/필터/광고 등)
  • <section> : 본문 콘텐츠
- <footer> : 저작권/연락처/관련 링크 등 하단 정보

[5] 스크립트 영역
- <script> 블록은 비어 있음 → 이후 이벤트 핸들링, 동적 렌더링, API 연동 등 점진적 추가

[6] 오늘의 핵심 포인트 요약
- 의미론적 태그로 문서 뼈대 구성(header/main/aside/section/footer)
- 뷰포트 메타로 모바일 대응 기본기 확보
- calc() + vh로 가변 높이 계산(헤더/푸터 제외 본문 채우기)
- CSS Grid 2열 레이아웃: grid-template-columns: 100px auto

────────────────────────────────────────────────────────────
[추가] Flex vs Grid 차이 한눈에 정리

(1) 한 줄 정의
- Flex(플렉스박스): 한 방향(가로나 세로)으로 ‘줄’을 세우는 1차원 레이아웃
- Grid(그리드): 행(row)·열(column)을 동시에 설계하는 2차원 레이아웃

(2) 언제 무엇을 쓰나
- Flex를 쓰세요:
  • 네비게이션 바, 버튼 줄, 태그 리스트 등 “가로나 세로 한 줄 배치”
  • 요소 내용 길이에 따라 유연한 간격/정렬이 필요할 때
  • 수평/수직 정렬(가운데 정렬 등)이 자주 필요할 때
- Grid를 쓰세요:
  • “좌측 100px 사이드바 + 우측 본문”처럼 행/열을 명확히 설계할 때
  • 대시보드·포토 갤러리처럼 가로·세로 2축에서 배치 제어가 필요할 때
  • 헤더/메인/사이드/푸터 같은 영역 기반 레이아웃과 반응형 기획이 분명할 때

(3) 비교 표

항목                 | Flex(플렉스)                    | Grid(그리드)
---------------------|----------------------------------|------------------------------
차원                 | 1차원(주 축 + 교차 축)           | 2차원(행 + 열)
배치 단위            | 아이템 흐름(‘줄’ 중심)           | 셀/트랙/영역(행·열 동시 설계)
주요 사용처          | 메뉴/버튼 줄/태그 모음            | 페이지 레이아웃/대시보드/갤러리
정렬/간격            | main/cross 축 정렬이 직관적       | gap + area 배치가 강력
자동 배치            | flex-wrap(줄바꿈) 중심            | auto-placement로 격자 채움
소스 순서 독립성     | 제한적(order로 일부 조정)         | grid-area로 큰 폭의 재배치 가능
학습 곡선            | 비교적 쉬움                       | 설계적 사고 필요(처음 다소 난이도↑)

(4) 속성 치트시트
- Flex 컨테이너: display:flex; flex-direction; flex-wrap; justify-content; align-items; gap
- Flex 아이템  : flex; flex-grow; flex-shrink; flex-basis; align-self; order
- Grid 컨테이너: display:grid; grid-template-columns; grid-template-rows; grid-template-areas; gap; justify-items; align-items; justify-content; align-content
- Grid 아이템  : grid-column; grid-row; grid-area; place-self

(5) 미니 예시

• Flex: 좌측 100px + 우측 가변
    .main   { display:flex; min-height:calc(100vh - 200px); }
    .aside  { width:100px; }
    .section{ flex:1; }

    <main class="main">
      <aside class="aside">aside</aside>
      <section class="section">section</section>
    </main>

• Grid: 좌측 100px + 우측 자동(오늘 수업과 동일 개념)
    .main{
      display:grid;
      grid-template-columns:100px auto;
      min-height:calc(100vh - 200px);
      gap:0;
    }

    <main class="main">
      <aside>aside</aside>
      <section>section</section>
    </main>

(6) 반응형 팁
- Grid 카드 그리드:
    .cards{
      display:grid;
      grid-template-columns:repeat(auto-fit, minmax(200px, 1fr));
      gap:16px;
    }
  → 화면 폭에 따라 컬럼 수가 자동 변함

- Flex 버튼 줄 줄바꿈:
    .btn-row{ display:flex; flex-wrap:wrap; gap:8px; }

(7) 한 줄 결론
- “정렬/한 줄/간단” = Flex, “레이아웃/영역/2차원” = Grid
- 두 도구는 경쟁이 아니라 상호보완. 같은 페이지에서도 적재적소로 섞어 쓰면 가장 깔끔함.
