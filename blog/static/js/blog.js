var csrftoken = $("[name=csrfmiddlewaretoken]").val();

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$('#btn_auth').click(function(){
var username = $('#username')[0].value;
var password = $('#password')[0].value;

$.ajax({
beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    },
url: '/login/',
method: 'POST',
//dataType: 'json',
data: { 'username': username,
        'password': password,
      },
success: function(data){
        $('#AuthModal').modal('hide');
        }
//function(){
////    alert(html);
//    auth_modal = $('#AuthModal');
//    auth_modal.modal('hide');
//    },

}
);

});