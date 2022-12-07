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
  - 클래스에서 `implements` 키워드를 사용해서 interface 구현
  - implements한 클래스는 모든 abstract 메서드를 override해서 구현 or 구현하지 않을 경우 abstract 클래스로 표시해야 함
  - 다형성 때문에 조상 인터페이스로 실제 객체 참조 가능
    - ex) Transformable tf = iman;

- 인터페이스의 필요성
  1. 구현의 강제로 표준화 처리 -> 손쉬운 모듈 교체 지원
  2. 서로 상속의 관계가 없는 클래스들에게 인터페이스를 통한 관계 부여로 다형성 확장
   - HandPhone, DigitalCamera 둘 다 charge 메서드가 필요한데, 둘 다 이미 하나를 상속 받고 있을 때(Phone, Camera) 상속 대신 Chargeable 인터페이스를 받아서 사용!
  3. 모듈 간 독립적인 프로그래밍 가능

- default method & static method

# Generics
다양한 타입의 객체를 다루는 메서드, 컬렉션 클래스에서 컴파일 시에 타입 체크
- 미리 사용할 타입을 명시해서 형 변환을 하지 않아도 되게 함
- 라벨링을 통해 해당하는 타입만 담을 수 있는 GenericBox
- 타입에 대한 체크가 컴파일 시에 일어나기 때문에 runtime에 발생할 수 있는 오류의 여지가 줄어듦
- type parameter의 제한
  - Number 이하의 타입으로만 제한하고 싶을 때 -> type parameter 선언 + extends Number(상위 타입 명시)
  - ```java
      public class NumberBox<T extends Number>
    ```
- Generic Type 객체를 할당 받을 때 와일드 카드 `?` 이용
  - Generic type<?> : 타입 제한 X
  - Generic type<? extends T> : T 또는 T를 상속받은 타입
  - Generic type<? super T> : T 또는 T의 조상 타입만 사용

- Generic Method
  - 파라미터와 리턴타입으로 type parameter를 갖는 메서드

