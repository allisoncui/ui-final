// JavaScript for modal interactions
document.addEventListener('DOMContentLoaded', function () {
    // Get the modal
    var modal = document.getElementById("openingModal");

    // Get the button that opens the modal
    var btn = document.getElementById("opening");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on the button, open the modal
    btn.onclick = function () {
        modal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    // Add similar handlers for other strategies if needed
});
document.addEventListener('DOMContentLoaded', function () {
    const noBtn = document.getElementById('no');
    const yesBtn = document.getElementById('yes');
    const managerBtn = document.getElementById('manager');
    const lookingForBtn = document.getElementById('looking-for');
    const cheaperPriceBtn = document.getElementById('cheaper-price');
    const managerResponse = document.getElementById('manager-response');
    const cheaperPriceResponse = document.getElementById('cheaper-price-response');
    const finalResponse = document.getElementById('final-response');

    noBtn.addEventListener('click', function () {
        document.getElementById('negative-response').classList.remove('hidden');
        document.getElementById('positive-responses').classList.add('hidden');
        managerResponse.classList.add('hidden');
        cheaperPriceResponse.classList.add('hidden');
        finalResponse.classList.add('hidden');
    });

    yesBtn.addEventListener('click', function () {
        document.getElementById('positive-responses').classList.remove('hidden');
        document.getElementById('negative-response').classList.add('hidden');
        managerResponse.classList.add('hidden');
        cheaperPriceResponse.classList.add('hidden');
        finalResponse.classList.add('hidden');
    });

    managerBtn.addEventListener('click', function () {
        managerResponse.classList.remove('hidden');
        cheaperPriceResponse.classList.add('hidden');
        finalResponse.classList.add('hidden');
    });

    lookingForBtn.addEventListener('click', function () {
        finalResponse.classList.remove('hidden');
        managerResponse.classList.add('hidden');
        cheaperPriceResponse.classList.add('hidden');
    });

    cheaperPriceBtn.addEventListener('click', function () {
        cheaperPriceResponse.classList.remove('hidden');
        managerResponse.classList.add('hidden');
        finalResponse.classList.add('hidden');
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const newItemBtn = document.getElementById('new-item');
    const usedItemBtn = document.getElementById('used-item');
    const newItemInfo = document.getElementById('new-item-info');
    const usedItemInfo = document.getElementById('used-item-info');

    newItemBtn.addEventListener('click', function () {
        newItemInfo.classList.remove('hidden');
        usedItemInfo.classList.add('hidden');
    });

    usedItemBtn.addEventListener('click', function () {
        usedItemInfo.classList.remove('hidden');
        newItemInfo.classList.add('hidden');
    });
});
document.addEventListener('DOMContentLoaded', function () {
    var decisionBoxes = document.querySelectorAll('.decision-box');
    decisionBoxes.forEach(function (box) {
        box.addEventListener('click', function () {
            decisionBoxes.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
        });
    });

    var responseBoxes = document.querySelectorAll('.response-box');
    responseBoxes.forEach(function (box) {
        box.addEventListener('click', function () {
            responseBoxes.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
        });
    });

    var infoBoxes = document.querySelectorAll('.item-button');
    infoBoxes.forEach(function (box) {
        box.addEventListener('click', function () {
            infoBoxes.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
        });
    });
});
document.addEventListener("DOMContentLoaded", function () {
    var coll = document.getElementsByClassName("collapsible");
    for (var i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function () {
            this.classList.toggle("active");
            var content = this.nextElementSibling;
            if (content.style.display === "block") {
                content.style.display = "none";
            } else {
                content.style.display = "block";
            }
        });
    }
});
