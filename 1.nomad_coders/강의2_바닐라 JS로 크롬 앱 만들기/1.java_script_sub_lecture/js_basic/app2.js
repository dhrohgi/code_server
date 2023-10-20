// object
const calculator = {
  plus: function (a, b) {
    console.log(a + b);
  },
  minus: function (a, b) {
    console.log(a - b);
  },
  times: function (a, b) {
    console.log(a * b);
  },
  divide: function (a, b) {
    console.log(a / b);
  },
  power: function (a, b) {
    console.log(a ** b);
  },
};

calculator.power(2, 4);

// return 에 대한 설명
const age = 96;
function calculateKrAge(ageOfForeigner) {
  return ageOfForeigner + 2;
}

const krAge = calculateKrAge(age);

console.log(krAge);

// return 을 넣어서 수정
const calculator2 = {
  plus: function (a, b) {
    return a + b;
  },
  minus: function (a, b) {
    return a - b;
  },
  times: function (a, b) {
    return a * b;
  },
  divide: function (a, b) {
    return a / b;
  },
  power: function (a, b) {
    return a ** b;
  },
};

calculator2.plus(2, 4); //함수를 호출하여 변수에 넣지 않으면 아무일도 안일어남.
const plusResult = calculator2.plus(2, 4);
const minusResult = calculator2.minus(plusResult, 10);
const timesResult = calculator2.times(10, minusResult);
const divideResult = calculator2.divide(timesResult, plusResult);
const powerResult = calculator2.power(divideResult, minusResult);

console.log(powerResult);
