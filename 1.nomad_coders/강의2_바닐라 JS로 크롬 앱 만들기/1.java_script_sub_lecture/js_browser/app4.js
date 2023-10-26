// Click event 듣기
const title = document.querySelector("div.hello:first-child h1");
console.dir(title);

/*
function handleTitleClick() {
  console.log("Title was clicked!");
  if (title.style.color === "blue") {
    title.style.color = "tomato";
  } else {
    title.style.color = "blue";
  }
}
*/

function handleTitleClick() {
  const currentColor = title.style.color;
  let newColor;

  if (currentColor === "blue") {
    newColor = "tomato";
  } else {
    newColor = "blue";
  }

  title.style.color = newColor;
}

title.addEventListener("click", handleTitleClick);
