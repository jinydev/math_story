# Math Story V3 (수학이야기)

AI 시대의 데이터 사이언스와 함께하는 새로운 수학 학습 연대기 웹사이트 프로젝트입니다.
본 프로젝트는 데스크탑과 모바일 뷰어에 최적화된 정적 웹사이트 생성기 **Jekyll(지킬)** 을 기반으로 제작되었습니다.

## 🚀 시작하기 전에 (Prerequisites)
로컬 환경에서 지킬(Jekyll) 서버를 띄워 실시간 렌더링을 확인하려면 먼저 아래 항목들이 호스트(Mac/Windows/Linux) 시스템에 설치되어 있어야 합니다.

1. **Ruby** (버전 2.5.0 이상)
2. **RubyGems**
3. **GCC 및 Make** (Mac의 경우 터미널에서 `xcode-select --install` 입력하여 Command Line Tools 설치)
4. **Bundler** (터미널에서 `gem install bundler` 입력하여 설치)

## 📦 초기 환경 셋업 (Installation)
저장소를 로컬에 내려받은 후, 최상위 프로젝트 폴더(Gemfile이 있는 위치)에서 다음 명령어를 실행하여 필요한 플러그인과 테마를 한 번에 설치합니다.

```bash
# Gemfile에 정의된 플러그인, 종속성 패키지들 설치
bundle install
```

## 💻 로컬 웹 서버 실행 (Running Local Server)
설치가 완료되면 시스템에서 다음 커맨드로 내장 로컬 웹 서버를 구동할 수 있습니다.

```bash
# 브라우저를 백그라운드 모드로 구동 
bundle exec jekyll serve -B

# (또는 백그라운드가 아닌 실시간 모니터링 모드)
# bundle exec jekyll serve
```
명령어가 정상적으로 돌면 `Server address: http://127.0.0.1:4000/` 와 같은 메시지가 나타납니다. 브라우저 창에서 `http://localhost:4000/` 로 접속 시 수학 웹사이트를 테스트해 볼 수 있습니다. 

*(참고: 서버를 강제로 종료하려면 `pkill -f jekyll` 명령어를 활용하세요.)*

## 🏗 정적 사이트 빌드 및 배포 (Build for Production)
강의 글과 이미지를 다 작성한 뒤, 운영 환경의 서버나 GitHub Pages 구동용으로 정적 HTML 파일들만 깔끔하게 빼내고 싶다면 다음 명령어를 사용합니다.

```bash
bundle exec jekyll build
```
현재 이 프로젝트 기준, `_config.yml` 설정에 의해 소스 코드는 `src/` 에서 인식되며, 빌드가 완료된 결과물은 최상위 디렉토리의 **`docs/`** 폴더 내에 생성됩니다. 

## 📁 주요 디렉토리 구조 (Directory Structure)
- **`src/`** : 실제 작성자가 다루게 될 마크다운(`*.md`) 강의 글과 이미지 (`extracted/img`) 원본 소스 영역.
- **`src/_data/`** : 총 86개의 챕터를 9단계로 그룹화하는 `level_00.yml` ~ `level_08.yml` 및 `menu_mapping.yml` 데이터 베이스
- **`src/_layouts/`** : 사이트 전반의 UI 뼈대를 관장하는 마스터 HTML 템플릿 영역
- **`docs/`** : 최종 빌드된 결과물이 저장되는 퍼블릭 폴더. 실제 상용 도메인 배포용 타겟입니다.
