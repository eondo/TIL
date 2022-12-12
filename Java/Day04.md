스트림을 통해서 데이터를 어떻게 가져오고 내보내고 하는지!

# IO
## 노드스트림
- I/0란?
  - 데이터의 입력과 출력을 의미한다. 입력과 출력의 끝단을 노드라고 한다
  - 두 노드를 연결하고 데이터를 전송할 수 있는 개념 : 스트림 (단방향 통신)
- Node Stream 종류 및 네이밍
  - 데이터 타입 byte) ~Stream
  - 데이터 타입 char) ~er

### InputStream과 Reader

#### InputStream의 주요 메서드
- read()
  - `public abstract int read() throws IOException` : byte 하나를 읽어서 int로 반환
  - `public int read(byte b[]) throws IOException` : 데이터를 읽어서 b를 채우고 읽은 바이트의 개수를 리턴 (0이 리턴되명 더 이상 읽을 값이 없음을 의미)
  - `public int read(byte b[], int offset, int len) throws IOException` : 최대 len 만큼 데이터를 읽어서 b의 offset부터 b에 저장하고 읽은 바이트 개수를 리턴
- close()
  - `public void close() throws IOException` : 스트림을 종료해서 자원을 반납

#### Reader의 주요 메서드
- byte 대신 char, buffer 사용

### OutputStream과 Writer
#### OutputStream
- write()
- close()
- flush() : 버퍼가 있는 스트림에서 버퍼의 내용을 출력하고 버퍼를 비움

#### Wrtier
- write()
- append()
- close()
- flush()

### File
가장 기본적인 입출력 장치 중 하나로 파일과 디렉터리를 다루는 클래스
- FileInputStream, FileOutputStream 이용해서 현재 위치에서 다른 곳으로 옮길 수 있음


## 보조스트림
### 보조 스트림의 개념과 종류
- 다른 스트림에 부가적인 기능을 제공하는 스트림
- 스트림 체이닝 : 여러 보조 스트림을 연결해서 사용 가능 -> 부가 기능 수행 (문자 set 변환, 버퍼링, 기본 데이터 형의 전송, 객체 입출력)

#### 종류
- byte 스트림을 char 스트림으로 변환 : InputStreamReader, OutputStreamWriter
- 버퍼링을 통한 속도 향상 : Buffered + ~Stream / Reader
- 객체 전송 : Object + ~

- 생성 : 이전 스트림을 생성자의 파라미터에 연결
  - ex. 키보드에서 발생할 수 있는 InputStream을 성능을 더 좋게 하기 위해 Buffered 기능을 더해보자! -> `new BufferedInputStream(System.in);` ...
- 종료 : 보조 스트림의 close() 호출

- 사용할 스트림의 결정 과정 : 노드가 무엇? -> 타입이 문자열? 바이트? -> 방향은 무엇? -> 추가 기능이 필요한가?

#### 보조스트림 활용
1. InputStreamReader & OutputStreamWriter
- byte 기반 스트림을 char 기반으로 변경

2. Buffered 계열
- 스트림의 입/출력 효율을 높이기 위해 데이터를 버퍼에 담아놓고 버퍼에 있는 데이터를 보여주는 방식 사용

3. 객체 직렬화
- 객체는 메모리, 힙에 여기저기 흩어져있기 때문에 이를 모아야 하므로 객체를 파일 등에 저장하거나 네트워크로 전송하기 위해 연속적인 데이터로 변환하는 것 -> 반대) 역 직렬화
- 직렬화 되기 위한 조건
  - 클래스의 모든 멤버가 Serailizable한 인터페이스 구현
  - 주민번호 등 파일로 저장하기 위험한 것은 transient 키워드로 직렬화에서 제외

- serialVersionUID : 클래스 변경 여부 확인 키
  - 멤버 변경으로 인한 컴파일 시마다 serialVersionUID 직접 설정 권장


# 공공데이터와 XML
### 데이터의 형태
- CSV
  - 용량 작지만 구조적이지 않음
- XML
  - 구조적, 정확한 문법이 필요, 큰 용량
- JSON
  - 구조를 가지며 객체로 다른 언어와 호환 가능

#### XML
- 확장 가능한 Markup Language
- 필요에 따라서 태그를 확장해서 사용 가능
- 정확한 문법을 지켜야 동작

- 기본 문법
  - 문서의 시작
  - 반드시 root element가 존재해야 한다.
    - 나머지 태그들은 Tree 형태로 구성
  - 시작 태그와 종료 태그는 일치해야 한다.
  - 시작 태그는 key-value 구조의 속성을 가질 수 있다. 
    - 속성 값은 "", ''로 묶어서 표현
  - 태그는 대소문자를 구별한다.

- 파싱이란?
  - 문서에서 필요한 정보를 얻기 위해 태그를 구별하고 내용을 추출하는 과정

### SAX(Simple API for XML) Parser
- SAX 동작 방식
  - 문서를 읽다가 발생하는 이벤트(사건) 기반으로 문서 처리
  - 이벤트가 발생하면 DefaultHandler의 메서드를 호출
  - 특정 이벤트마다 어떤 동작을 해줄지는 MyHandler 클래스에서 따로 필요한 메서드 재정의

#### [예제] 오늘의 박스오피스 파싱
  - SAXParser를 구성하고 boxoffice.xml을 파싱하기
  ```java
  // 공장 돌리기 - 공장에서 newInstance 가져옴
  SAXParserFactory factory = SAXParserFactory.newInstance();
  // Parser를 만듦
  try {
    SAXParsr parser = factory.newSAXParser();
    // Parser 구성한 것 통해서 파싱하기
    // 넘겨줄 파일 타입과 DefaultHandler 넘겨주기
    parser.parse(xml, this);
  } catch (SAXParseException e) {
    e.printStackTrace();
  } catch(SAXException e) {
    e.printStackTrace();
  } catch(ParserConfigurationException e) {
    e.printStackTrace();
  } catch (IOException e) {
    e.printStackTrace();
  }
  return list;

  // 필요한 메서드를 재정의하여 boxOffice.xml을 파싱 -> startDocument, endDocument, startElement, characters, endElement
  @Override
  public void startDocument() throws SAXException {
    System.out.println("문서 읽기 시작");
  }
  ...

### 문서의 parsing - dom
- 동작 방식
  - 문서를 완전히 메모리에 로딩 후 필요한 내용 찾기
  - Document Builder Factory가 Document Builder를 생성(XML 문서) → Builder를 통ㅇ해 파싱하면 DOM Tree가 생김
- DOM Tree
  - 문서를 구성하는 모든 요소(태그, 속성, 값)를 Node로 구성
  - 태그들은 루트 Node(주소록)을 시작으로 부모-자식의 관계 구성
  - Node를 상속받는 것 : Element

### 문서의 parsing - json
- JSON
  - 다른 기종 간의 데이터 교환에 광범위하게 사용됨
  - 객체를 key-value의 쌍으로 관리
  - [실습] 라이브러리 등록) Java Build Path
  - JSON 문서와 JSON을 처리할 DTO만 있으면 라이브러리를 통해 처리 가능
  - ObjectMapper를 통해서 데이터를 읽어올 때 Map 구조!

### Swing
- Java Application에서 사용되는 GUI를 제공하는 추상적으로 정의된 도구(컴포넌트) 모음

