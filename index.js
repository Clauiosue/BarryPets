

$(document).ready(function() {
    $("#contactForm").submit(function(event) {
        event.preventDefault(); 

        var name = $("#inputName").val();
        var email = $("#inputEmail").val();
        var phone = $("#inputPhone").val();
        var consulta = $("#inputConsulta").val();

        if(name == "" || email == "" || phone == "" || consulta == "") {
            alert("Por favor, completa todos los campos.");
            return;
        }

        var templateParams = {
            from_name: name,
            from_email: email,
            message: consulta,
            reply_to: phone
        };

        emailjs.send('service_oucun08', 'template_ys8u0oj', templateParams)
            .then(function(response) {
               console.log('SUCCESS!', response.status, response.text);
               $("#contactForm")[0].reset();
               $("#message").show().delay(5000).fadeOut();
            }, function(error) {
               console.log('FAILED...', error);
            });
    });
});

