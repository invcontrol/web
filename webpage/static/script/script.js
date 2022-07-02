function getDog() {
  $.getJSON("https://dog.ceo/api/breeds/image/random", function (data) {
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

  

function checkProv(sel) {
  if (sel.value == "add") {
    $(location).attr("href", "/control/proveedor/new");
  }
}

function agrega_producto(target, codigo) {
  $(document).ready(function () {
    if ($("#txtbusqueda").val() != "") {
      if ($("#tr-" + codigo).length == 0) {
        $.get("/api/items/" + codigo, function (data) {
          $(target).append("<tr id='tr-" + data.sku + "'>" +
            "<td>" + data.nombre + "</td>" +
            "<td class='input-group'><input class='form-control' id='in-" + data.sku + "' value=1 min=1 max="+data.cantidad+" type='number'>" +
            "<span name='tipo-" + data.sku + "' class='input-group-text'></span></td>" +
            "<td><label>" + data.cantidad + "</label><span name='tipo-" + data.sku + "'></span></td>" +
            "<td>" + data.sku + "</td>" +
            "<td><input class='btn-eliminar' type='image' value='Eliminar' onclick='elimina_producto(this)' src='/static/img/delete.png'></td>"
          );
          $.get(data.tipo, function (tipo) {
            var l = document.getElementsByName("tipo-"+codigo);
            l.forEach(function(e) {
              e.classList.add(tipo.cssclass);
            });
          });
          var ver_cant = function(event){
            if(parseInt(this.value)>parseInt(this.max)) {
              alert("No puede colocar mas de la cantidad que existe en bodega");
              this.value = this.max;
            }
          };
          document.getElementById("in-"+codigo).addEventListener("focusout", ver_cant.bind(document.getElementById("in-"+codigo)));
        }).fail(function () {
          alert("El producto no existe, revise el codigo")
        });
      }
      else {
        $("#in-" + codigo).val(parseInt($("#in-" + codigo).val()) + 1)
      }
    }
    else {
      alert("Por favor ingrese un codigo");
    }

  });
}

function agrega_producto_ingreso(target, codigo) {
  $(document).ready(function () {
    if ($("#txtbusqueda").val() != "") {
      if ($("#tr-" + codigo).length == 0) {
        $.get("/api/items/" + codigo, function (data) {
          $(target).append("<tr id='tr-" + data.sku + "'>" +
            "<td>" + data.nombre + "</td>" +
            "<td class='input-group'><input class='form-control' id='in-" + data.sku + "' value=1 min=1 type='number'>" +
            "<span name='tipo-" + data.sku + "' class='input-group-text'></span></td>" +
            "<td><label>" + data.cantidad + "</label><span name='tipo-" + data.sku + "'></span></td>" +
            "<td>" + data.sku + "</td>" +
            "<td><input class='btn-eliminar' type='image' value='Eliminar' onclick='elimina_producto(this)' src='/static/img/delete.png'></td>"
          );
          $.get(data.tipo, function (tipo) {
            var l = document.getElementsByName("tipo-"+codigo);
            l.forEach(function(e) {
              e.classList.add(tipo.cssclass);
            });
          });
        }).fail(function () {
          alert("El producto no existe, revise el codigo")
        });
      }
      else {
        $("#in-" + codigo).val(parseInt($("#in-" + codigo).val()) + 1)
      }
    }
    else {
      alert("Por favor ingrese un codigo");
    }

  });
}

function elimina_producto(target) {
  $(target).parents("tr").remove();
}






