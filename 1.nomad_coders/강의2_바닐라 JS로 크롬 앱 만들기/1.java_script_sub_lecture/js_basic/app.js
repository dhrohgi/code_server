// 변수 만드는 법. 주로 const 로 만들고 변하지 않아야 되는 경우에만 let 사용할 것
// var 도 있으나 오래된 자바스크립트 문접이라 사용하지 말것.
const a = 5;
const b = "hello";
const c = true;
const d = null;

let e = null;
let f;
let isDennisFat = true;
isDennisFat = false;

// JS Array
const testArray = [1, 2, 3, 4, 5, true, false, null, "hello"];
console.log(testArray[0]);
console.log(testArray);
testArray.push(9);
testArray.push("potato");
console.log(testArray);
testArray[5] = false;
console.log(testArray);

// JS Object
const player = {
  name: "nico",
  points: 10,
  fat: true,
};

console.log(player);
player.lastName = "potato";
player.points = 15;
console.log(player);

// function 만드는 법
function sayHello(myName, age) {
  console.log("Hello my name is " + myName + " and I'm " + age + " years old");
}

sayHello("nico", 10);
sayHello("Daehan", 48);
sayHello("Dohun", 14);

function plus(a, b) {
  console.log(a + b);
}
function divide(a, b) {
  console.log(a / b);
}

plus(43, 35);
divide(34, 67);

//JS Object2
const player2 = {
  name: "nico",
  sayHello: function (otherPersonName) {
    console.log("Hello " + otherPersonName);
  },
};

player2.sayHello("Dennis!");
