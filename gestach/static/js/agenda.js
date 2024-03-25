document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    headerToolbar: {
      left: 'prev,next today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay'
    },
    editable: true,
    events: [], // Vous pouvez charger les événements à partir d'une source de données ici
    eventClick: function(info) {
      // Remplir le formulaire avec les données de l'événement
      $('#eventModal #title').val(info.event.title);
      $('#eventModal #start').val(info.event.start.toISOString().slice(0, 16));
      $('#eventModal #end').val(info.event.end ? info.event.end.toISOString().slice(0, 16) : '');
      $('#eventModal #description').val(info.event.extendedProps.description);
      $('#eventModal').modal('show');
    },
    selectable: true,
    select: function(info) {
      // Afficher le formulaire pour créer un nouvel événement
      $('#eventModal #title').val('');
      $('#eventModal #start').val(info.start.toISOString().slice(0, 16));
      $('#eventModal #end').val(info.end.toISOString().slice(0, 16));
      $('#eventModal #description').val('');
      $('#eventModal').modal('show');
    }
  });

  calendar.render();

  $('#saveEvent').click(function() {
    var title = $('#eventModal #title').val();
    var start = $('#eventModal #start').val();
    var end = $('#eventModal #end').val();
    var description = $('#eventModal #description').val();

    // Vous pouvez envoyer les données de l'événement au serveur ici

    // Exemple d'ajout d'un événement au calendrier
    var event = {
      title: title,
      start: start,
      end: end ? end : null,
      description: description
    };
    calendar.addEvent(event);

    $('#eventModal').modal('hide');
  });
});