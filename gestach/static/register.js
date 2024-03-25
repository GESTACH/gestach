// register.js

var validationInput = document.getElementById("validmail");
var resetButton = document.getElementById("resetButton");

validationInput.addEventListener("input", function(event) {
    var inputElement = event.target;
    if (inputElement.checkValidity()) {
        inputElement.classList.remove("is-invalid");
        inputElement.classList.add("is-valid");
        // Afficher le bouton de réinitialisation lorsque le champ n'est plus vide
        resetButton.style.display = inputElement.value.trim() !== "" ? "block" : "none";
    } else {
        inputElement.classList.remove("is-valid");
        inputElement.classList.add("is-invalid");
        resetButton.style.display = "none"; // Masquer le bouton de réinitialisation en cas de saisie invalide
    }
});

resetButton.addEventListener("click", function() {
    validationInput.value = ""; // Réinitialiser la valeur
    validationInput.classList.remove("is-valid", "is-invalid"); // Réinitialiser les classes
    resetButton.style.display = "none"; // Masquer le bouton après la réinitialisation
});
