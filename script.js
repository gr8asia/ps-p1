const welcomeLink = document.getElementById("welcome-link");
const message = document.getElementById("message");

welcomeLink.addEventListener("click", (event) => {
  event.preventDefault();
  message.textContent = "welcome to p1.";
});
