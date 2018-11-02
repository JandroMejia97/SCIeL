function ajaxBorrar(id_invernadero, nombre_invernadero){
  url = "/ajax/borrar/invernadero/"+id_invernadero+"/";
  return $.ajax({
      url: url,
      type: 'POST',
      contentType: 'application/json',
      data: {
        'id_invernadero': id_invernadero,
      },
      dataType: 'json',
      succes: function(data){
        console.log(data)
      }
    }).done(function(respuesta) {
      alert("El invernadero "+nombre_invernadero+ " fue borrado exitosamente");
      //reloadInvernadero();
    }).fail(function() {
      console.log("error");
      alert("El invernadero "+nombre_invernadero+ " no pudo ser eliminado");
    }).always(function() {
      console.log("complete");
  });
}

function borrar(id_invernadero, nombre_invernadero, id_usuario){
  $('#borrarModal').modal('hide');
  response = ajaxBorrar(id_invernadero, nombre_invernadero);
  response.succes(function(data){
    alert("El invernadero "+nombre_invernadero+ " fue borrado exitosamente");
    //reloadInvernadero(id_usuario)
  })
}

/*function reloadInvernadero(id_usuario){
  response = $('#bodyTable').empty();
  $.ajax({
    url: 'recargar/invernadero/',
    type: 'POST',
    data: {
      'id_usuario': id_usuario,
    }
  });
  response.s
}*/
//  url = "La url como la declara DJANGo";
   // $.ajax({
  //    url: url,
 //     type: 'POST',
 //     data: {'variable': valor },
  //  })
  //  .done(function(respuesta) {

  //      })
  //      .fail(function() {
 //         console.log("error");
 //       })
 //       .always(function() {
 //         console.log("complete");
   //     });

function confirmarBorrado(id_invernadero, nombre_invernadero, id_usuario){
    $('#modalBodyBorrar').empty();
    $('#modalBodyBorrar').append(
      "<p>¿Seguro que desea eliminar el invernadero <strong>"+nombre_invernadero+"</strong>?</p>"+
      "<p>Seleccione 'Continuar' para confirmar la acción</p>"
    );
    $('#modalFooterBorrar').empty();
    $('#modalFooterBorrar').append(
      "<button class='btn btn-primary' type='button' data-dismiss='modal'>Cancelar</button>"+
      "<button id='confirmacion' class='btn btn-danger' href='#'>Continuar</button>"
    )
    $('#borrarModal').modal('show');
    $('#confirmacion').attr('onclick', 'borrar('+id_invernadero+', \''+nombre_invernadero+'\', '+id_usuario+')');
 }
 $(function () {
  $.ajaxSetup({
      headers: { "X-CSRFToken": getCookie("csrftoken") }
  });
});