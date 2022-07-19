// For Ticket Status Updates
function closeTicket(ticketId) {
    fetch("/close-ticket", {
        method: "POST",
        body: JSON.stringify({ ticketId: ticketId }),
    }).then((_res) => {
        window.location.href = "/admin-dashboard";
    });
}

function solveTicket(ticketId) {
    fetch("/solve-ticket", {
        method: "POST",
        body: JSON.stringify({ ticketId: ticketId }),
    }).then((_res) => {
        window.location.href = "/admin-dashboard";
    });
}

// For zoom Accessibility
let zoom = 1;
let zoomStep = 0.05;
let zoomCount = 0;
const zoomText = document.getElementsByClassName("zoomtext");

document.getElementById("zoomIn").addEventListener("click", function () {
    console.log(zoomCount);
    if (zoomCount <= 3) {
        zoom += zoomStep;
        for (let i = 0; i < zoomText.length; i++) {
            zoomText[i].style.transform = "scale(" + zoom + ")";
            zoomCount += 1;
        }
    }
});
document.getElementById("zoomOut").addEventListener("click", function () {
    console.log(zoomCount);
    if (zoomCount <= 3) {
        if (zoom > zoomStep) {
            zoom -= zoomStep;
            for (let i = 0; i < zoomText.length; i++) {
                zoomText[i].style.transform = "scale(" + zoom + ")";
                zoomCount += 1;
            }
        }
    }
});
document.getElementById("zoomReset").addEventListener("click", function () {
    zoom = 1;
    for (let i = 0; i < zoomText.length; i++) {
        zoomText[i].style.transform = "scale(" + zoom + ")";
        zoomCount = 0;
    }
})