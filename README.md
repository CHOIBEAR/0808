# 0808

📘 오늘 학습 요약 – FastAPI(Form + 파일 업로드 + 미리보기)  
────────────────────────────────────────────────────

# 1) 오늘 변경사항 한눈에 보기

- **index.html**
  - 폼 전송을 `POST /s2/`로 지정하고, 파일 업로드를 위해 `enctype="multipart/form-data"` 추가. 텍스트(`txt`)와 파일(`file`)을 함께 전송함. :contentReference[oaicite:0]{index=0}
  - 업로드된 이미지를 바로 확인할 수 있도록 **두 가지 확인 방식** 제공:
    1) a 링크: `/s2/read?fileName=test.png` (새 탭) :contentReference[oaicite:1]{index=1}  
    2) GET 폼: `/s2/read`로 파일명을 입력해 확인 :contentReference[oaicite:2]{index=2}

- **app02.py**
  - `POST /s2/`: `txt`는 `Form(...)`로, `file`은 `UploadFile`로 받아 **서버에 저장**하고 저장 결과(파일명·경로)를 JSON으로 반환. 저장 디렉터리는 `uploaded_images/`(없으면 생성)이며, 파일명은 **UUID.확장자** 형식으로 생성함. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5} :contentReference[oaicite:6]{index=6}
  - `GET /s2/read`: 쿼리로 받은 `fileName`을 경로에 조합하여 파일을 찾고, `mimetypes.guess_type()`으로 **미디어 타입**을 추정해 `FileResponse`를 **inline**으로 반환함. 응답 헤더에 `Content-Disposition`을 설정함. :contentReference[oaicite:7]{index=7}
  - 라우팅 테이블: `/s2/`에 `GET/POST` 등록, `/s2/read`에 파일 읽기용 `GET` 등록. :contentReference[oaicite:8]{index=8} :contentReference[oaicite:9]{index=9}


# 2) 요청 흐름(엔드 투 엔드)

1) **클라이언트(브라우저)**  
   - `index.html`에서 텍스트와 파일을 선택 후 **POST /s2/** 로 전송 (`multipart/form-data`). :contentReference[oaicite:10]{index=10}

2) **서버(app02.py – POST /s2/)**  
   - `txt`(Form), `file`(UploadFile)을 수신 → 저장 디렉터리(초기화 보장)로 파일 **저장** → `{"result": txt, "filename": <UUID.ext>, "path": <저장경로>}` 반환. :contentReference[oaicite:11]{index=11} :contentReference[oaicite:12]{index=12} :contentReference[oaicite:13]{index=13}

3) **클라이언트 확인(미리보기)**  
   - 반환된 파일명을 가지고 `/s2/read?fileName=<반환값>`으로 접속하면 브라우저에서 파일이 **inline**으로 렌더링됨(이미지면 이미지로 표시). :contentReference[oaicite:14]{index=14}


# 3) 오늘 포인트 핵심 정리

- **Form 전송과 파일 업로드**  
  - HTML 폼으로 텍스트+파일을 함께 보내려면 반드시 `enctype="multipart/form-data"`가 필요. :contentReference[oaicite:15]{index=15}
  - FastAPI에서는 텍스트는 `Form(...)`, 파일은 `UploadFile`로 수신. (POST 바디 기반 처리) :contentReference[oaicite:16]{index=16} :contentReference[oaicite:17]{index=17}

- **서버 저장 전략**  
  - 업로드 파일 저장 루트 생성 보장: `os.makedirs("uploaded_images", exist_ok=True)` :contentReference[oaicite:18]{index=18}  
  - 저장 파일명 충돌 방지: `uuid4().hex`로 파일명 생성 후 원본 확장자 결합. :contentReference[oaicite:19]{index=19}

- **미리보기 응답**  
  - `mimetypes.guess_type()`으로 동적 `media_type` 추정 → `FileResponse(..., media_type=...)`로 브라우저 렌더링 제어. :contentReference[oaicite:20]{index=20}
  - `Content-Disposition: inline` 설정으로 다운로드 대신 브라우저 내 표시 유도. :contentReference[oaicite:21]{index=21}

- **라우팅 구성 방식**  
  - `study02["urls"]`에 `GET/POST/READ` 엔드포인트들을 선언적으로 나열하고, 라우터에 일괄 등록하는 패턴을 유지. (오늘은 `/s2/`와 `/s2/read` 중심) :contentReference[oaicite:22]{index=22} :contentReference[oaicite:23]{index=23}


# 4) 테스트 시나리오(요약)

- `index.html` 열기 → 텍스트+이미지 선택 → **요청** 클릭 → 응답 JSON에서 `filename` 확인. :contentReference[oaicite:24]{index=24}
- 브라우저에서 `/s2/read?fileName=<filename>` 접속 → 이미지가 브라우저에 **즉시 표시**되는지 확인. :contentReference[oaicite:25]{index=25}

────────────────────────────────────────────────────
