const quotes = [
  {
    quote: "우리는 나이가 들면서 변하는 게 아니다. 보다 자기 다워지는 것이다.",
    author: "린홀",
  },
  {
    quote: "인생에 뜻을 세우는데 적당한 때는 없다.",
    author: "볼드윈",
  },
  {
    quote: "실패는 잊어라. 하지만 그것이 준 교훈은 절대 잊으면 안 된다.",
    author: "하버트 개서",
  },
  {
    quote: "우리는 행복하기 때문에 웃는 게 아니라, 웃기 때문에 행복하다.",
    author: "윌리엄 제임스",
  },
  {
    quote: "인생을 다시 산다면 다음번에는 더 많은 실수를 저지르리라.",
    author: "나딘 스테어",
  },
  {
    quote: "가장 큰 위험은 위험 없는 삶이다.",
    author: "스티븐 코비",
  },
  {
    quote: "모든 사람들로부터 사랑받지 않아도 된다.",
    author: "니체",
  },
  {
    quote:
      "못하는 일에 초점 맞추기를 그만하면 자기가 어떤 일을 할 수 있는지 알고 놀라게 될 것이다.",
    author: "앨릭스 코브",
  },
  {
    quote: "삶이 가치가 있다고 믿어라. 그러면 그 믿음은 현실이 될 것이다.",
    author: "윌리엄 제임스",
  },
  {
    quote: "훌륭한 사람과 어리석은 사람의 차이는 불과 한 걸음 차이다.",
    author: "나폴레옹",
  },
  {
    quote: "당신의 하루하루를 당신의 마지막 날이라고 생각하라.",
    author: "호라티우스",
  },
  {
    quote: "당신의 하루하루를 당신의 마지막 날이라고 생각하라.",
    author: "호라티우스",
  },
  {
    quote: "꿈을 꿀 수 있다면, 그 꿈을 실현할 수 있다.",
    author: "월트 디즈니",
  },
  {
    quote: "오랫동안 꿈을 그리는 사람은 마침내 그 꿈을 닮아간다.",
    author: "앙드레 말로",
  },
  {
    quote: "삶이 소중한 이유는 언젠가 끝나기 때문이다.",
    author: "프란츠 카프카",
  },
];

const quote = document.querySelector("div#quote span:first-child");
const author = document.querySelector("div#quote span:last-child");

const todaysQuote = quotes[Math.floor(Math.random() * quotes.length)];
quote.innerText = `💬 ${todaysQuote.quote}`;
author.innerText = todaysQuote.author;
