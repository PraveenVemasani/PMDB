// script.js
document.addEventListener("DOMContentLoaded", function () {
    const voteAverageElement = document.getElementById("voteAverage");
    const voteAverage = parseFloat(voteAverageElement.textContent);
    const votePercentage = Math.ceil(voteAverage * 10);
    voteAverageElement.textContent = votePercentage + "%";
  
    // Like Button
    const heartIcon = document.getElementById("heartIcon");
    let isRegularHeart = true;
  
    heartIcon.addEventListener("click", () => {
      if (isRegularHeart) {
        heartIcon.classList.remove("far", "fa-heart");
        heartIcon.classList.add("fas", "fa-heart");
      } else {
        heartIcon.classList.remove("fas", "fa-heart");
        heartIcon.classList.add("far", "fa-heart");
      }
      isRegularHeart = !isRegularHeart;
    });
  });
  