const clock = document.querySelector("h2#clock");

function getClock() {
  const date = new Date();
  const hours = String(date.getHours()).padStart(2, "0");
  const minutes = String(date.getMinutes()).padStart(2, "0");
  const seconds = String(date.getSeconds()).padStart(2, "0");
  // clock.innerText = `Current time: ${hours}:${minutes}:${seconds}`;
  if (parseInt(hours) >= 21) {
    clock.innerText = `⏲ Current time: ${hours}:${minutes}:${seconds}, Good night bro! 🌜`;
  } else if (parseInt(hours) >= 18) {
    clock.innerText = `⏲ Current time: ${hours}:${minutes}:${seconds}, Thanks god, it's going home time! 🚗`;
  } else if (parseInt(hours) > 12) {
    clock.innerText = `⏲ Current time: ${hours}:${minutes}:${seconds}, Focus, focus and focus! 🎈`;
  } else if (parseInt(hours) == 12) {
    clock.innerText = `⏲ Current time: ${hours}:${minutes}:${seconds}, Take some lunch! 🍔`;
  } else {
    clock.innerText = `⏲ Current time: ${hours}:${minutes}:${seconds}, Good morning! 😀`;
  }
}

getClock();
setInterval(getClock, 1000);
