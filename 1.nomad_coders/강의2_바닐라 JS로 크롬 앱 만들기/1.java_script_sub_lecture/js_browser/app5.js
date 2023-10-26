// Click event 듣기
const h1 = document.querySelector("div.hello:first-child h1");
console.dir(h1);

/*
function handleTitleClick() {
  if (h1.className === "clicked") {
    h1.className = "";
  } else {
    h1.className = "clicked";
  }
}

// 위와 같이 작성할 경우의 문제점은 "clicked" 의 철자가 틀릴 경우 찾아내기 어렵다는 것임.
// 그래서 아래와 같이 하는 것이 이런 에러를 방지할 수 있는 방법임.
// 추가로 아래는 h1 의 class 를 제거하지 않고 추가할 수 있는 방법임. (classList 사용)
function handleTitleClick() {
  const clickedClass = "clicked";
  if (h1.classList.contains(clickedClass)) {
    h1.classList.remove(clickedClass);
  } else {
    h1.classList.add(clickedClass);
  }
}
*/

// 아래는 classList.add() 또는 remove() 대신 classList.toggle() 을 사용
// 또 하나의 tip 은 string 을 반복하는 순간 constant 를 생성해야 하는 순간이다!
function handleTitleClick() {
  const clickedClass = "clicked";
  h1.classList.toggle(clickedClass);
}

h1.addEventListener("click", handleTitleClick);
