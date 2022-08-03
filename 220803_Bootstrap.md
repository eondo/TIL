### Bootstrp 기본 원리

#### spacing
Margin and Padding
CSS는 부트스트랩 개발자가 이미 만들어와서 우리는 클래스만 지정해주면 됨.

{property}{sides}-{size}
M or P? 옆에 위에 어디에? 얼만큼 줄지?
ex) mt-3
<div class="mt-3 ms-5">bootstrap-spacing</div>

.mt-1 {
  margin-top: 0.25rem !important;
}
-> 1rem = 16px니까 0.25rem = 4px
ex) margin 16px 위아래 -> my-3 (선택자를 쓸 필요 없다는 장점)

.mx-auto : 수평 중앙 정렬, 가로 가운데 정렬
.py-0 : 위아래 padding 0

#### Color
#### Position
position도 bootstrap 통해 설정 가능

absolte 쓰려면 부모가 static이 아님

#### Display
.d-none
.d-inline
.d-flex

breakpoint 언급

#### Bootstrap Component
#### NavBar
많이 쓰임

#### Carousel
페이지 상단에 회전목마 돌듯이 배너들이 바뀌는 UI

#### Modal
팝업창과 다르게 다른 아무 위치를 클릭하면 꺼진다
중첩해서 들어가있으면 안됨 (항상 TOP LEVEL, BODY LEVEL에 두기) -> 다른 요소에게 방해받아서 안 보이는 현상 방지

#### FlexBox

#### card > 
```html
<!--반응형 웹을 의미하는 코드-->
<div class="row row-cols-1 row-cols-md-3 g-4">
```

### Responsive Web Design
이를 만들기 위해 사용하는게 Grid System

### Grid System

- 기본 요소
  - Column
  - Gutter : 칼럼과 칼럼 사이의 공간 (사이 간격)
  - Container

- 원리 (*반드시 기억해야 할 2가지)
  - 12개의 column로 나눠져 있음
  - 6개의 grid breakpoints
    - breakpoint마다 나오길 원하는 디자인에 차이가 있음. 여기까지는 화면에서 4개가 보이고, 이러한 분기점

```html
<div class="container">
  <h2 class="text-center">column</h2>
  <div class="row">
    <div class="col box">1</div>
    <div class="col box">2</div>
    <div class="col box">3</div>
  </div>
</div>
```
.col-{breakpoint}-
```html
<div class="row">
    <div class="box col">1</div>
    <div class="box col">2</div>
    <div class="w-100"></div> <!--텅빈 가로로 한 칸 띄워준다-->
    <div class="box col">3</div>
    <div class="box col">4</div>
    
    ## 1,2가 한 줄, 34가 한 줄, 즉 가로줄 두 줄
  </div>
```
```html
<!--1이 3칸, 2가 6칸, 3이 3칸으로 비율 지정 가능-->
<div class="row">
    <div class="box col-3">1</div>
    <div class="box col-6">2</div>
    <div class="box col-3">3</div>
  </div>
```
12칸을 넘어가면 한 칸 밑으로 추가됨
```html
<div class="row">
    <div class="box col-1">1</div>
    <div class="box col-1">2</div>
    <div class="box col-1">3</div>
    <div class="box col-1">4</div>
    <div class="box col-1">5</div>
    <div class="box col-1">6</div>
    <div class="box col-1">7</div>
    <div class="box col-1">8</div>
    <div class="box col-1">9</div>
    <div class="box col-1">10</div>
    <div class="box col-1">11</div>
    <div class="box col-1">12</div>
    <div class="box col-1">13</div>
  </div>
```
- 합이 12칸이 넘어서 col-9가 쓰이고 나서는 줄바꿈이 일어난 채로 col-4, col-3이 밑으로 내려옴
```html
<div class="row">
    <div class="box col-9">col-9</div>
    <div class="box col-4">col-4</div>
    <div class="box col-3">col-3</div>
  </div>
```
화면 비율 설정 - breakpoint 연습하기
```html
<h2>Grid breakapoint</h2>
  <div class="row">
    <!--lg일땐 5:2:5로 column이 나타난다~-->
    <div class="box col-2 col-sm-8 col-md-4 col-lg-5">1</div>
    <div class="box col-8 col-sm-2 col-md-4 col-lg-2">1</div>
    <div class="box col-2 col-sm-2 col-md-4 col-lg-5">1</div>
  </div>
```

#### nesting, offset
- nesting
  - 원하는 대로 컬럼 스타일 중첩 가능
  ```html
  <h2 class="text-center">nesting</h2>
  <div class="row">
    <div class="box col-6">
      <div class="row">
        <div class="box col-3">1</div>
        <div class="box col-3">2</div>
        <div class="box col-3">3</div>
        <div class="box col-3">4</div>
      </div>
    </div>
    <div class="box col-6">1</div>
    <div class="box col-6">2</div>
    <div class="box col-6">3</div>
  </div>
  ```
- offset
  - 원하는 대로 column 양옆 등을 공백으로 두고 싶을 때 사용