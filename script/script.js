function getDog(){
    $.getJSON("https://dog.ceo/api/breeds/image/random", function( data ) {
        $(".breeds-image-random pre").html(JSON.stringify(data, null, 4));
        $(".image-content").html("<img src='" + data.message + "'style=\"width: 50px; height: 50px\">");
    });
}

function val() {
    (function () {
        'use strict'

        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.querySelectorAll('.needs-validation')

        // Loop over them and prevent submission
        Array.prototype.slice.call(forms)
          .forEach(function (form) {
            form.addEventListener('submit', function (event) {
              if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
              }

              form.classList.add('was-validated')
            }, false)
          })
      })()
}

function elimina_tabla(target) {
  $(target).hide("slow");
}