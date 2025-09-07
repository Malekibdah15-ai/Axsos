console.log("page loaded...");

function changename() {
    let name = document.querySelector("#jane-name")
    name.innerText = "Malek Ibdah"
}
function wipe(el) {
    let parent = el.closest(".card-list-item")
    parent.remove()
    let connectionNumber = document.querySelectorAll(".badge")
    connectionNumber[0].innerText = Number(connectionNumber[0].innerText) - 1
    if (el.alt === "accept") {
        connectionNumber[1].innerText = Number(connectionNumber[1].innerText) + 1
    }
}