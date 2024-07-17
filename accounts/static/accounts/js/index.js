$(document).ready(function() {
    // Contador de caracteres para el campo consulta
    $('#inputConsulta').on('input', function() {
        var charCount = $(this).val().length;
        $('#charCount').text(charCount + '/150');
    });

    $("#contactForm").submit(function(event) {
        event.preventDefault(); // Previne el envío del formulario por defecto

        // Quita mensaje de errores anteriores
        $(".invalid-feedback").remove();
        $(".is-invalid").removeClass("is-invalid");

        var name = $("#inputName").val();
        var apellido = $("#inputApellido").val();
        var email = $("#inputEmail").val();
        var phone = $("#inputPhone").val();
        var consulta = $("#inputConsulta").val();
        var valid = true;

        // Valida los campos requeridos
        if(name == "") {
            $("#inputName").addClass("is-invalid");
            $("#inputName").after('<div class="invalid-feedback">Por favor, completa este campo.</div>');
            valid = false;
        }

        if(apellido == "") {
            $("#inputApellido").addClass("is-invalid");
            $("#inputApellido").after('<div class="invalid-feedback">Por favor, completa este campo.</div>');
            valid = false;
        }

        // Valida el formato del email
        var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        if(email == "" || !emailPattern.test(email)) {
            $("#inputEmail").addClass("is-invalid");
            $("#inputEmail").after('<div class="invalid-feedback">Por favor, ingresa un email válido.</div>');
            valid = false;
        }

        // Valida el formato del telefono
        var phonePattern = /^\+569\d{8}$/;
        if(phone == "" || !phonePattern.test(phone)) {
            $("#inputPhone").addClass("is-invalid");
            $("#inputPhone").after('<div class="invalid-feedback">Por favor, ingresa un número de teléfono válido en el formato +569XXXXXXXX.</div>');
            valid = false;
        }

        // Valida el largo de la consulta
        if(consulta.length > 150 || consulta.length ==0 ) {
            $("#inputConsulta").addClass("is-invalid");
            $("#inputConsulta").after('<div class="invalid-feedback">Por favor, ingresa una consulta de hasta 150 caracteres.</div>');
            valid = false;
        }

        //si todos los campos son validos, realiza el envio del formulario por la API de EmailJS

        if(valid) {
            var templateParams = {
                from_name: name + " " + apellido,
                from_email: email,
                message: consulta,
                reply_to: phone
            };

            emailjs.send('service_oucun08', 'template_ys8u0oj', templateParams)
                .then(function(response) {
                   console.log('SUCCESS!', response.status, response.text);
                   $("#contactForm")[0].reset();
                   $("#charCount").text('0/150'); // Deja el contador en 0
                   $("#message").show().delay(5000).fadeOut();
                }, function(error) {
                   console.log('FAILED...', error);
                });
        }
    });
});
