const title1 = document.querySelector(".hello h1"); // css 스타일을 검색하는 방법 hello class 밑의 h1 찾기
const title2 = document.querySelector("div.hello:first-child h1");
// class hello 를 가진 div 태그 내부의 first child 인 h1 을 찾기

const title3 = document.querySelector("#hello"); // hello id 로 검색하는 것과 동일한 결과
const title4 = document.querySelector("#hello:first-child");

console.dir(title2);

title2.style.color = "red";
