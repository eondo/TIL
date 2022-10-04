# Database

파일을 이용한 데이터 관리 → 스프레드 시트를 이용한 데이터 관리 → 데이터베이스!
- 프로그래밍 언어를 사용해 작동시킴
- 많은 형태의 데이터베이스 중 RDB(관계형 데이터베이스)가 가장 많이 쓰임
- RDB는 각각의 데이터를 테이블에 기입함
- HOW 입력? 출력? → 데이터베이스의 CRUD를 학습해보자!

## Intro
### Database
검색, 구조화 등 작업을 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템 → 검색, 갱신 효율화
- 데이터베이스를 조작하는 프로그램 : DBMS
- 이때 사용하는 언어가 SQL

## RDB
관계형 데이터베이스
- 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식
- 이 테이블간 관계를 설정해 SQL을 사용하여 데이터를 조회하고 조작 가능

### RBD 기본 구조
### SQLite

## SQL
RDBMS의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어
- RDBMS에서 데이터베이스 스키마를 생성 및 수정할 수 있으며, 테이블에서의 자료 검색 및 관리도 할 수 있음
- 데이터베이스 객체에 대한 처리를 관리하거나 접근 권한을 설정하여 허가된 사용자만 RDBMS를 관리할 수 있도록 할 수 있음
- 데이터베이스와 상호작용하는 방법!

### SQL 명령어
1. DDL : 데이터 정의 (테이블, 스키마를 정의(생성, 수정 및 삭제)) / CREATE, DROP, ALTER
2. DML : 데이터 조작 (데이터를 조작 CRUD) / INSERT, SELECT, UPDATE, DELETE
3. DCL : 데이터 제어

### 문법
```
SELECT column_name from Table_name;
```
[참고] Statement & Clause
- statement
  - 독립적으로 실행될 수 있는 코드 조각
- Clause
  - statment의 하위 단위

## DDL
테이블 or 스키마를 정의한다. 데이터를 다루는 게 아니라 데이터를 조작하기 위한 틀을 정하는 언어.
SQL 데이터 정의 언어를 사용하여 테이블 데이터베이스 개체를 만드는 방법을 학습
CREATE, ALTER, DROP

### 1️. CREATE TABLE
결국 스키마를 정의하는 것
```
CREATE TABLE 테이블이름 (
  컬럼 이름, 어떤 데이터타입, 제약조건
  );
```
#### 🧷 SQLite Data Types
- 동적 타입 시스템을 사용 → 컬럼에 선언된 데이터 타입에 의해서가 아니라 컬럼에 저장된 값에 따라 데이터 타입이 결정됨
- 정적 타입 시스템이 지정된 데이터베이스에서 작동하는 SQL문이 SQLite에서 동일한 방식으로 작동함
- 다른 데이터베이스와의 호환성 문제가 있기 때문에 테이블 생성 시 데이터 타입을 지정하는 것을 권장
- 데이터 타입 지정하면 입력된 데이터의 타입을 지정된 데이터 타입으로 자동으로 변환됨(허용 가능한 타입 변환 존재)

- Type Affinity 타입 선호도가 내부적으로 존재해서 호환성이 좋음

#### 🧷 Constraints
입력하는 자료에 대해 제약을 정함, 제약에 맞지 않으면 입력이 거부됨 → 무결성을 유지하기 위함
- 데이터 무결성 : 데이터에 대한 정확성, 일관성을 보장하기 위한 것
- 종류 : NOT NULL, UNIQUE, PRIMARY KEY, AUTOINCREMENT
1. NOT NULL
   - 컬럼이 NULL 값을 허용하지 않도록 지정
   - 기본적으로 테이블의 모든 컬럼은 NOT NULL
2. UNIQUE
   - 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함(중복된 레코드가 들어올 수 없음)
3. PRIMARY KEY
   - 테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼
   - 각 테이블에는 하나의 기본 키만 있음
   - 암시적으로 NOT NULL 제약 조건이 포함되어 있음
   - [참고] INTEGER 타입에만 사용 가능
4. AUTOINCREMENT
   - 이전에 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
   - Django에서 테이블 생성 시 id컬럼에 기본적으로 사용하는 제약조건
   - INTEGER PRIMARY KEY 다음에 작성하면 해당 rowidi를 다시 재사용하지 못하도록 함

#### 🧷 rowid의 특징
테이블을 생성할 때마다 rowid라는 암시적 자동 증가 컬럼이 자동으로 생성됨
- 테이블에 새 행을 삽입할 때마다 정수 값을 자동으로 할당(1에서 시작)
- rowid 안 쓸 거면 INTEGER PRIMARY KEY를 써야 이를 대체함


### 2. ALTER TABLE
기존 테이블의 구조를 수정(변경)
1. 테이블 이름 변경
2. 컬럼의 이름 변경
3. 기존 테이블에 새로운 컬럼을 추가 -> 기존 데이터가 있을 때 문제가 생길 수 있음, 기존 데이터가 있으면 새롭게 추가되는 컬럼에 값이 없기 때문에! DEFAULT 제약 조건을 사용하여 해결 가능
4. 컬럼 삭제 ALTER TABLE '테이블 이름' DROP COLUMN '컬럼 이름'
   - 삭제하지 못 하는 경우
     - 컬럼이 다른 부분에서 참조되는 경우
     - PRIMARY KEY인 경우
     - UNIQUE 제약 조건이 있는 경우

### 3. DROP TABLE
데이터베이스에서 테이블을 제거
- 특징
  - 한 번에 하나의 테이블만 삭제 가능
  - DROP TABLE 문은 실행 취소하거나 복구할 수 없음


## DML
#### INDEX
- Simple query
- Sorting
- Filtering
- Grouping
- Changing

- 키워드 : INSERT(C), SELECT(R), UPDATE(U), DELETE(D)

### SELECT문
### Sorting rows
__ORDER BY__
- FROM 절 뒤에, 하나 이상 컬럼을 기준으로 결과를 오름차순, 내림차순으로 정렬할 수 있음
- 여러 기준으로 정렬 할 땐, 우선으로 맞출 기준을 먼저 적고 그 뒤를 콤마로 구분해서 넣음
- [참고] NULL값 있는 경우

### Filtering data
__SELECT DISTINCT__
- 조희 결과에서 중복된 행을 제거
- 두 개 이상의 컬럼에 대해서 쓰면 그 둘이 따로 보는 게 아니라 하나로 묶어서 중복 제거함
- [참고] NULL값을 중복으로 간주하여 NULL값의 한 행만 남김

__WHERE__
- 조회 시 특정 검색 조건을 지정
- 수정이나 삭제할 때에도 WHERE 절을 사용할 수 있음
- FROM절 뒤에 작성
- 작성 형식 : COMPARISON_OPERATOR 다양함

__SQLite logical operators(논리연산자)__
ALL, AND, ANY, __BETWEEN, IN, LIKE__, NOT, OR

- LIKE operator : 패턴 일치를 기반으로 데이터 조회
  - 두 개의 와일드카드
    - % : 0개 이상의 문자가 올 수 있음을 의미
    - _ (underscore) : 뒤에 단일(1개) 문자가 있음을 의미
```
WHERE '02-%'

WHERE age LIKE '2_'

WHERE phone LIKE '%-51__-%';
```
- IN operator : 값이 값 목록 결과에 있는 값과 일치하는 지 확인
```
SELECT first_name, country FROM users
WHERE country NOT IN ('경기도', '강원도');
```
- BETWEEN operator : 어떤 값 이하 ~ 이상을 확인

__LIMIT 절__
결과에서 행 수를 제한할 수 있음
- [응용] OFFSET 키워드 : 함께 사용하면 특정 지정된 위치에서부터 데이터를 조회
```
SELECT rowid, first_name FROM
users LIMIMT 10 OFFSET 10; 
# rowid 11부터 20까지 조회
```

### Grouping data
__GROUP BY__
```
# 지역을 기반으로 지역마다 몇 명 있는지 카운트
SELECT country, COUNT(*) FROM users
GROUP BY country;
```
- Aggregate function(집계 함수) - 함께 많이 쓰임
  - 값 집합의 최대값, 최소값, 평균, 합계 및 개수를 계산

이제까지 R, 이제 CUD!
### Changing data
INSERT, UPDATE, DELETE

__INSERT문__
```
INSERT INTO '테이블이름' ('테이블 컬럼 목록')
VALUES ('컬럼에 해당 하는 밸류 목록')
```
__UPDATE문__
```
UPDATE '테이블 이름'
SET '컬럼 = 새로운 값'
WHERE '수정할 대상' (WHERE절 없으면 전체 데이터가 다 SET 뒤 값으로 바뀜)
```
__DELETE문__
```
DELETE FROM '테이블 이름'
WHERE '검색 조건' -> 제거할 행을 식별
```

