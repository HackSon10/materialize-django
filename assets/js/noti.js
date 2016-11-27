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