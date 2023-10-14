////////////////////////////////////
//live 깔아주기
// 객체

//객체 리터널로 객체 생성
// 플퍼타로 suit, rank 생성
let card = { suit: '하트', rank: 'a'};
console.log(card);

//프로퍼티의 이름은 문자열이 되어도 상관없다.
card = { 'suit' : '하트', 'rank' : 'a'};

//프로퍼티 값의 참조 방법
console.log(card.suit);
console.log(card["rank"]);
console.log(card.test)

//프로퍼티 값 추가
card.value = 14;
console.log(card.value);

//객체의 프로퍼티 삭제
delete card.value;
console.log(card.value)

//객체의 프로퍼티 보유여부 확인
console.log("suit" in card);
console.log("random" in card);
console.log("toString" in card);

////////////////////////////////////
// 메소드

card = {
    suit : "하트",
    rank : "a",
    showCard: function() {
        // this 키워드는 함수의 소유자를 가르킨다
        console.log(`이 카드는 ${this.suit} ${this.rank} 입니다.`);
    }
};
card.showCard();

////////////////////////////////////
// 함수

function square(x) {
    return x * x;
}
console.log(square(9));

//함수는 객체이다.
//객체와 동일한 조작이 가능하다.\
square.test = "testValue"
console.log(square.test);
console.log(square);

////////////////////////////////////
// 객체 생성자

function Card(suit, rank) {
    //new 키워드가 붙은경우
    //this = {}
    this.suit = suit;
    this.rank = rank;

    //new 키워드가 붙는경우
    //return this;
}
card = new Card("하트", "a");
console.log(card);

//전역함수인 this눈 기본적으로
//글로벌 객체인 window를 가르킨다
card = Card("하트", "a");
console.log(window.suit, window.rank);

///////////////////////////////////////
//클래스 (ES6버전 생성자)

class Circle {

    // 파이썬의 __init__ 역할
    constructor(center, radius) {
        this.center = center;
        this.radius = radius;

    }

    //원의 면적 계산 메서드
    area() {
        return Math.PI * (this.radius ** 2);
    }
}

let circle = new Circle({x:0, y: 0}, 2.0);
console.log(`넓이 = ${circle.area()}`);


//삼겹살 가격 구하기
class Product {
    constructor(name, weight, price) {
        this.name = name;
        this.weight = weight;
        this.price = price;

    };


    calculate(weight) {
        return (weight/ this.weight) * this.price;
    };
};
let fork = new Product('삼겹살', 100, 1690);
console.log(`삼겹살 150g의 가격 = ${fork.calculate(150)}원`);

