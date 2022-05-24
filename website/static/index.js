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