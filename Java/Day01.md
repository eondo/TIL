1. 자바 기본
   1. 변수, 연산자, 제어문
2. 배열, 다차원 배열
3. 객체지향 프로그래밍
4. 변수
5. 메서드
6. 생성자

클래스를 접근하는 3가지 방법
```
// 1. 클래스 이름.class
Class<?> clz = Dog.class;

// 2. Class.forName("패키지 포함 클래스명")
Class<?> clz2 = Class.forName("com.ssafy.reflection.Dog");

// 3. 객체(인스턴스).getClass()
Dog d = new Dog();
Class<?> clz3 = d.getClass(); 
```

## Variable
- 메모리 공간에 값 할당 후 사용
- 타입에 따라 크기가 달라짐
- 기본형 vs 참조형
 - 기본형 : boolean, byte, short, int(* 32bit, 20억 쯤), long, float, double(*), char
   - 부동소수점 double으로 연산하면 부정확한 결과가 나올 수 있음을 유의 -> 유효 자리수를 이용한 반올림 처리, 정수형으로 변환 후 계산
   - 90 / 100 => 0, 90 / 100.0 = 0.9

## 형 변환 
- primitive, reference끼리 형 변환 가능
- 기본 타입과 참조형의 형 변환을 위해 Wrapper 클래스(Integer.~) 사용
- 방법(형 변환 연산자(괄호) 사용)
  - ```java 
    double d = 100.5;
    int result = (int)d; // result = 100
    ```
- 묵시적 형 변환
  - 작은 데이터 타입 -> 큰 데이터 타입 (값 손실 X), 값의 크기, 타입의 크기가 아닌 표현 범위가 커지는 방향으로 할당할 경우는 묵시 적 형변환 발생
  - ```java
      byte b = 10;
      int i2 = b
      ```
- 명시적 형 변환
  - ```java
      int i = 300;
      byte b = (byte)i;
      ```

## 연산자
