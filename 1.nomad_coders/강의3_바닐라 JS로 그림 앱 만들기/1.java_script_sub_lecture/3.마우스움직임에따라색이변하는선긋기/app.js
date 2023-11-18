const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d"); //getContext("2d") 함수로 2d brush 를 만들 수 있으며, ctx 가 brush 이다.
canvas.width = 800;
canvas.height = 800;
ctx.lineWidth = 2;

const colors = [
  "#ff3838",
  "#ffb8b8",
  "#c56cf0",
  "#ff9f1a",
  "#fff200",
  "#32ff7e",
  "#7efff5",
];

function onClick(event) {
  ctx.beginPath();
  ctx.moveTo(0, 0);
  const color = colors[Math.floor(Math.random() * colors.length)];
  ctx.strokeStyle = color;
  ctx.lineTo(event.offsetX, event.offsetY);
  ctx.stroke();
}

canvas.addEventListener("mousemove", onClick);
