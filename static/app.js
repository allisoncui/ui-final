// JavaScript for modal interactions
document.addEventListener('DOMContentLoaded', function () {
    // Get the modal
    var modal = document.getElementById("openingModal");

    // Get the button that opens the modal
    var btn = document.getElementById("opening");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on the button, open the modal
    btn.onclick = function() {
        modal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    // Add similar handlers for other strategies if needed
});
document.querySelector('.next-arrow').addEventListener('click', function () {
    window.location.href = '/quiz'; // Assuming this is the next tutorial step
});