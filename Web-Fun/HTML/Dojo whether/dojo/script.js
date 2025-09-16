
function convert() {
    const select = document.getElementById("show-temp");
    const toFahrenheit = select.value === "f";
    const temps = document.querySelectorAll(".temperature");

    temps.forEach(temp => {
        let value = parseInt(temp.dataset.value); 
        if (toFahrenheit) {
            temp.innerText = Math.round((value * 9 / 5) + 32) + "°F";
        } else {
            temp.innerText = value + "°C";
        }
    });
}

function display(el){
    alert ("loading weather for "+ el.innerText);

}

function hide() {
    var element = document.querySelector(".box");
    element.remove();
}