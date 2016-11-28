var comment = $('#comment');
var formComment = $('form#formComment');
var text = $('input#id_comment');

formComment.on('submit' ,function(e){
  e.preventDefault();

  var comment = text.val()

  $.ajax({
		url: "/comment/100/",
		type: "POST",
		data: {'comment':comment},
	})

  .done(function(res){
    console.log(res)
    $('.collection')
      .append('<li class="collection-item animated bounceInUp"> <strong>'+res.comment+'</strong> '+res.user+'</li>')
  })
  .fail(function(err){
    console.log(err)
  })

})

function reload(){
  setTimeout(function() {

    var confirmation = confirm('Puede ser que tus amigos hallan hecho algo, dale aceptar');

    if (confirmation){
      location.reload(true);
    }else{
      alert('gracias');
    }
    
  }, 120000);
}

reload();

function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
	beforeSend: function(xhr, settings) {
		if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	}
});