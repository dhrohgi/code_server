const rangeInput = document.querySelector("#range-form input");
const playForm = document.querySelector("#play-form");
const playInput = document.querySelector("#play-form input");

function paintResult(rangeNumber, guessNumber) {
  const machineNumber = Math.ceil(Math.random() * parseInt(rangeNumber, 10));
  const compareText = document.querySelector("#result div:first-child");
  const resultText = document.querySelector("#result div:last-child");
  compareText.innerText = `You chose: ${guessNumber}, the machine chose: ${machineNumber}.`;
  if (rangeNumber == "") {
    resultText.innerText = "Please set the range first!";
  } else if (guessNumber == machineNumber) {
    resultText.innerText = `You won!`;
  } else {
    resultText.innerText = `You lost!`;
  }
}

function onPlaySubmit(event) {
  event.preventDefault();
  const rangeNumber = rangeInput.value;
  const guessNumber = playInput.value;
  paintResult(rangeNumber, guessNumber);
}

playForm.addEventListener("submit", onPlaySubmit);
