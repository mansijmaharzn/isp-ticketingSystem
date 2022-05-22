function deleteTicket(ticketId) {
    fetch("/delete-ticket", {
        method: "POST",
        body: JSON.stringify({ ticketId: ticketId }),
    }).then((_res) => {
        window.location.href = "/tickets";
    });
}