// Click event 듣기
const title = document.querySelector("div.hello:first-child h1");
console.dir(title);

function handleTitleClick() {
  console.log("Title was clicked!");
  title.style.color = "blue";
}

function handleMouseEnter() {
  title.innerText = "Mouse is here";
}

function handleMouseLeave() {
  title.innerText = "Mouse is gone";
}

function handleWindowResize() {
  document.body.style.backgroundColor = "tomato";
}

function handleWindowCopy() {
  alert("Copier!");
}

function handleWindowOffline() {
  alert("connection lost!");
}

function handleWindowOnline() {
  alert("connected again!");
}

title.addEventListener("click", handleTitleClick);
title.addEventListener("mouseenter", handleMouseEnter);
title.addEventListener("mouseleave", handleMouseLeave);

window.addEventListener("resize", handleWindowResize);
window.addEventListener("copy", handleWindowCopy);
window.addEventListener("offline", handleWindowOffline);
window.addEventListener("online", handleWindowOnline);
