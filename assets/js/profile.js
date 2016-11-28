$('#vent').delay(3000).fadeIn(function(){
  $('#close').click(function () { 
    $('#vent').addClass('animated zoomOut').fadeOut()
  })
})