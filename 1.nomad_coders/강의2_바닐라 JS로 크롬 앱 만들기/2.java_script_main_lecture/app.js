const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting");

const HIDDEN_CLASSNAME = "hidden";
// JS 에서 전통적으로 string 만 포함된 변수는 대문자로 표기함

function onLoginSubmit(event) {
  event.preventDefault();
  loginForm.classList.add(HIDDEN_CLASSNAME);
  const username = loginInput.value;
  // greeting.innerText = "Hello! " + username;
  greeting.innerText = `Hello! ${username}`;
  greeting.classList.remove(HIDDEN_CLASSNAME);
}

loginForm.addEventListener("submit", onLoginSubmit);

// submit 이벤트는 호출되면서 벌어진 일들(event object)을 호출되는 함수의 아규먼트로 넣어준다.
// 그래서 호출되는 함수의 아규먼트에 event object 가 들어갈 자리를 미리 만들어 줘야 한다.
// 위에서 들어갈 자리는 event 임.
