const clockTitle = document.querySelector(".js-clock");

function getClock() {
  const date = new Date();
  const days = String(date.getDate()).padStart(2, 0);
  const hours = String(date.getHours()).padStart(2, 0);
  const minutes = String(date.getMinutes()).padStart(2, 0);
  const seconds = String(date.getSeconds()).padStart(2, 0);
  clockTitle.innerText = `${days}d ${hours}h ${minutes}m ${seconds}s`;
}

function getChristmasClock() {
  const christmasDate = new Date("2023-12-24");
  const currentDate = new Date();
  const timeLeft = christmasDate - currentDate;
  const timeLeftDays = String(
    Math.floor(timeLeft / (1000 * 60 * 60 * 24))
  ).padStart(2, 0);
  const timeLeftHours = String(
    Math.floor((timeLeft / (1000 * 60 * 60)) % 24)
  ).padStart(2, 0);
  const timeLeftMinutes = String(
    Math.floor((timeLeft / (1000 * 60)) % 60)
  ).padStart(2, 0);
  const timeleftSeconds = String(Math.floor((timeLeft / 1000) % 60)).padStart(
    2,
    0
  );
  clockTitle.innerText = `${timeLeftDays}d ${timeLeftHours}h ${timeLeftMinutes}m ${timeleftSeconds}s`;
}

getChristmasClock();
setInterval(() => {
  getChristmasClock();
}, 1000);
