$("form[name='register_form']").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/register",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
          console.log(resp);
          $error.text(resp.responseJSON.error).removeClass("error--hidden");  
        }
    })

    e.preventDefault();
});