// button 의 클릭 이벤트를 받는 방법인데, 이것보다는 html 의 form 을 이용하는 것이
// 간편하다.

const loginInput = document.querySelector("#login-form input");
const loginButton = document.querySelector("#login-form button");

function onLoginBtnClick() {
  const username = loginInput.value;

  if (username === "") {
    alert("Please write your name");
  } else if (username.length > 15) {
    alert("Your name is too long");
  }
}

loginButton.addEventListener("click", onLoginBtnClick);
