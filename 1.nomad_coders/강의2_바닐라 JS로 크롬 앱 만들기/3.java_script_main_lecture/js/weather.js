const API_KEY = "50d20d0c95fefe643c6fe21030dd2e76";

function onGeoOk(position) {
  const lat = position.coords.latitude;
  const lon = position.coords.longitude;
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`;
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      const weather = document.querySelector("#weather span:first-child");
      const city = document.querySelector("#weather span:last-child");

      weather.innerText = `🌡 ${data.weather[0].main} and ${data.main.temp}℃`;
      city.innerText = `in ${data.name}`;
    });
}

function onGeoError() {
  console.log("error");
}

const geo = navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError);
console.log(geo);
