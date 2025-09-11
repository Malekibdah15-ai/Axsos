const video = document.getElementById("videos");

video.addEventListener("mouseenter",()=> {
video.play();
})

video.addEventListener("mouseleave",()=> {
video.pause();
})