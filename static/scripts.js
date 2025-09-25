// For Typing Welcome heading
document.addEventListener("DOMContentLoaded", function() {
  const text = "Welcome to AI Learning Hub";
  const typingElement = document.getElementById("typing-text");
  const subtitle = document.getElementById("subtitle");
  let i = 0;

  function typeWriter() {
    if (i < text.length) {
      typingElement.textContent += text.charAt(i);
      i++;
      setTimeout(typeWriter, 80); // typing speed
    } else {
      // Fade-in subtitle after typing finishes
      subtitle.style.transition = "opacity 1s ease";
      subtitle.style.opacity = 1;
    }
  }

  typeWriter();
});


// =========================================