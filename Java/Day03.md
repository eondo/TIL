# OOP - 3

## 추상 클래스
- 우리 프로젝트의 최상위 도메인인 Vehicle을 이용한 배열 사용
- 정의
  - 자손 클래스에서 반드시 재정의해서 사용되어 조상의 구현이 무의미한 메서드 addFuel()
  - 클래스 선언부에 abstract 추가 == abstract 메서드를 가진 클래스는 객체를 생성할 수 없는 클래스!라고 명시
    - 추상 클래스는 객체를 생성할 수 없으므로 Vehicle v = new Vehicle() 불가능
    - 그러나, Vehicle v = new DieselSUV(); 다형성으로 조상으로서 자식을 레퍼런스할 수 있다.

- 이유
  - 메서드 재정의 구현을 강제하여 발생할 수 있는 오류 방지

## Interface
- 인터페이스 작성
  - 일반 메서드는 모두 abstract 형태로 고도로 추상화
  - 형태
    - 클래스와 유사하게 interface 선언
    - 멤버변수 : public static final 생략
    - 메서드 : public abstract 생략

- 인터페이스 상속
  - 다중 상속 가능
- 인터페이스 구현과 객체 참조
  - 클래스에서 `implements` 키워드드르 사용해서 interface 구현
  - implements한 클래스는 모든 abstract 메서드를 override해서 구현 or 구현하지 않을 경우 abstract 클래스로 표시해야 함
  - 다형성 때문에 조상 인터페이스로 실제 객체 참조 가능
    - ex) Transformable tf = iman;

- 인터페이스의 필요성
  1. 구현의 강제로 표준화 처리 -> 손쉬운 모듈 교체 지원
  - 서로 상속의 관계가 없는 클래스들에게