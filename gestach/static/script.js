document.addEventListener('DOMContentLoaded', function () {
    // Ajouter un gestionnaire d'événement aux boutons de bascule
    var toggleButtons = document.querySelectorAll('.toggle-btn');
    toggleButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            // Trouver la ligne parente
            var parentRow = button.closest('.parent-row');
            // Trouver la table fille
            var subTable = parentRow.querySelector('.sub-table');
            // Basculer la visibilité de la table fille
            subTable.style.display = (subTable.style.display === 'none' || subTable.style.display === '') ? 'table' : 'none';
            // Changer le texte du bouton (+/-)
            button.textContent = (subTable.style.display === 'none' || subTable.style.display === '') ? '+' : '-';
        });
    });
});