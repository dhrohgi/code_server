import "./style.css";

function handleColorChange() {
  if (window.innerWidth >= 1000) {
    document.body.style.backgroundColor = "#eebc12";
  } else if (window.innerWidth <= 500) {
    document.body.style.backgroundColor = "#2e8cd5";
  } else {
    document.body.style.backgroundColor = "#8f4fae";
  }
}

window.addEventListener("resize", handleColorChange);
