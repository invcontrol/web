function getDog() {
  $.getJSON("https://dog.ceo/api/breeds/image/random", function (data) {
    $(".breeds-image-random pre").html(JSON.stringify(data, null, 4));
    $(".image-content").html("<img src='" + data.message + "'style=\"width: 250px; height: 250px\">");
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

function checkUn(sel) {
  if (sel.value == "add") {
    $(location).attr("href", "/control/unidades/new");
  }
}

function agrega_producto(target, codigo) {
  $(document).ready(function () {
    if ($("#txtbusqueda").val() != "") {
      if ($("#tr-" + codigo).length == 0) {
        $.get("/api/items/" + codigo, function (data) {
          $(target).append("<tr id='tr-" + data.sku + "'>" +
            "<td>" + data.nombre + "</td>" +
            "<td class='input-group'><input class='form-control' id='in-" + data.sku + "' name='in-" + data.sku + "' value=1 min=1 max=" + data.cantidad + " type='number'>" +
            "<span name='tipo-" + data.sku + "' class='input-group-text'></span></td>" +
            "<td><label>" + data.cantidad + "</label><span name='tipo-" + data.sku + "'></span></td>" +
            "<td>" + data.sku + "</td>" +
            "<td><input class='btn-eliminar' type='image' value='Eliminar' onclick='elimina_producto(this)' src='/static/img/delete.png'></td>"
          );
          $.get(data.tipo, function (tipo) {
            var l = document.getElementsByName("tipo-" + codigo);
            l.forEach(function (e) {
              e.classList.add(tipo.cssclass);
            });
          });
          var ver_cant = function (event) {
            if (parseInt(this.value) > parseInt(this.max)) {
              alert("No puede colocar mas de la cantidad que existe en bodega");
              this.value = this.max;
            }
          };
          document.getElementById("in-" + codigo).addEventListener("focusout", ver_cant.bind(document.getElementById("in-" + codigo)));
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

function agrega_producto_venta(target, codigo) {
  $(document).ready(function () {
    if ($("#txtbusqueda").val() != "") {
      if ($("#tr-" + codigo).length == 0) {
        $.get("/api/items/" + codigo, function (data) {
          $(target).append("<tr id='tr-" + data.sku + "'>" +
            "<td>" + data.nombre + "</td>" +
            "<td class='input-group'><input class='form-control' id='in-" + data.sku + "' name='in-" + data.sku + "' value=1 min=1 max=" + data.cantidad + " type='number' readonly>" +
            "<span name='tipo-" + data.sku + "' class='input-group-text'></span></td>" +
            "<td><label>" + data.cantidad + "</label><span name='tipo-" + data.sku + "'></span></td>" +
            "<td>" + data.sku + "</td>" +
            "<td><span class='precios'>" + data.precio.toLocaleString() + "</span><input type='hidden' id='precio-" + data.sku + "' value='" + data.precio + "' ></td>" +
            "<td><input class='btn-eliminar' type='image' value='Eliminar' onclick='elimina_producto(this)' src='/static/img/delete.png'></td>"
          );
          $.get(data.tipo, function (tipo) {
            var l = document.getElementsByName("tipo-" + codigo);
            l.forEach(function (e) {
              e.classList.add(tipo.cssclass);
            });
          });
          var ver_cant = function (event) {
            if (parseInt(this.value) > parseInt(this.max)) {
              alert("No puede colocar mas de la cantidad que existe en bodega");
              this.value = this.max;
            }
          };
          document.getElementById("in-" + codigo).addEventListener("focusout", ver_cant.bind(document.getElementById("in-" + codigo)));
          document.getElementById("in-" + codigo).addEventListener("keyup", ({ key }) => {
            if (key === "Enter") {
              document.getElementById("txtbusqueda").focus();
              return;
            }
          });
          let precio = Number(document.getElementById("precio-" + codigo).value);
          let total = Number(document.getElementById("total-h").value);
          let cant = Number(document.getElementById("in-" + codigo).value);
          total = total + precio * cant;
          document.getElementById("total").innerHTML = total.toLocaleString();
          document.getElementById("total-h").value = total;
        }).fail(function () {
          alert("El producto no existe, revise el codigo")
        });
      }
      else {
        let precio = Number(document.getElementById("precio-" + codigo).value);
        let cant = Number(document.getElementById("in-" + codigo).value);
        let previo = precio * cant;
        let totalh = Number(document.getElementById("total-h").value);
        let total = totalh - previo;
        total = total + (precio * (cant + 1));
        document.getElementById("total").innerHTML = total.toLocaleString();
        document.getElementById("total-h").value = total;
        $("#in-" + codigo).val(parseInt($("#in-" + codigo).val()) + 1)
      }

      document.getElementById("txtbusqueda").value = "";
    }
    else {
      alert("Por favor ingrese un codigo");
    }

  });
}
function buscarVenta(target, codigo) {
  $(document).ready(function () {
    if ($("#txtvta").val() != "") {
      if ($("#tr-" + codigo).length == 0) {
        $.get("/api/venta/" + codigo, function (data) {
          $.get("/api/detalle/"+data.id, function (detalle) {

          });
          $(target).append("<tr id='tr-" + data.sku + "'>" +
            "<td>" + data.nombre + "</td>" +
            "<td class='input-group'><input class='form-control' id='in-" + data.sku + "' name='in-" + data.sku + "' value=1 min=1 max=" + data.cantidad + " type='number' readonly>" +
            "<span name='tipo-" + data.sku + "' class='input-group-text'></span></td>" +
            "<td><label>" + data.cantidad + "</label><span name='tipo-" + data.sku + "'></span></td>" +
            "<td>" + data.sku + "</td>" +
            "<td><span class='precios'>" + data.precio.toLocaleString() + "</span><input type='hidden' id='precio-" + data.sku + "' value='" + data.precio + "' ></td>" +
            "<td></td>"
          );
          $.get(data.tipo, function (tipo) {
            var l = document.getElementsByName("tipo-" + codigo);
            l.forEach(function (e) {
              e.classList.add(tipo.cssclass);
            });
          });
          var ver_cant = function (event) {
            if (parseInt(this.value) > parseInt(this.max)) {
              alert("No puede colocar mas de la cantidad que existe en bodega");
              this.value = this.max;
            }
          };
          document.getElementById("in-" + codigo).addEventListener("focusout", ver_cant.bind(document.getElementById("in-" + codigo)));
          document.getElementById("in-" + codigo).addEventListener("keyup", ({ key }) => {
            if (key === "Enter") {
              document.getElementById("txtbusqueda").focus();
              return;
            }
          });
          let precio = Number(document.getElementById("precio-" + codigo).value);
          let total = Number(document.getElementById("total-h").value);
          let cant = Number(document.getElementById("in-" + codigo).value);
          total = total + precio * cant;
          document.getElementById("total").innerHTML = total.toLocaleString();
          document.getElementById("total-h").value = total;
        }).fail(function () {
          alert("El producto no existe, revise el codigo")
        });
      }
      else {
        let precio = Number(document.getElementById("precio-" + codigo).value);
        let cant = Number(document.getElementById("in-" + codigo).value);
        let previo = precio * cant;
        let totalh = Number(document.getElementById("total-h").value);
        let total = totalh - previo;
        total = total + (precio * (cant + 1));
        document.getElementById("total").innerHTML = total.toLocaleString();
        document.getElementById("total-h").value = total;
        $("#in-" + codigo).val(parseInt($("#in-" + codigo).val()) + 1)
      }

      document.getElementById("txtbusqueda").value = "";
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
            "<td class='input-group'><input class='form-control' id='in-" + data.sku + "'  name='in-" + data.sku + "' value=1 min=1 type='number'>" +
            "<span name='tipo-" + data.sku + "' class='input-group-text'></span></td>" +
            "<td><label>" + data.cantidad + "</label><span name='tipo-" + data.sku + "'></span></td>" +
            "<td>" + data.sku + "</td>" +
            "<td><input class='btn-eliminar' type='image' value='Eliminar' onclick='elimina_producto(this)' src='/static/img/delete.png'></td>"
          );
          $.get(data.tipo, function (tipo) {
            var l = document.getElementsByName("tipo-" + codigo);
            l.forEach(function (e) {
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


async function checkAlerts() {
  const delay = ms => new Promise(res => setTimeout(res, ms));
  let bajos = "";
  let sobres = "";
  let cero = "";
  $.get("/api/alertas/", function (dataAlert) {
    console.log(dataAlert.results);
    $.each(dataAlert.results, function (i, value) {
      $.get("/api/items/" + value.sku, function (dataProd) {
        console.log("Alerta:");
        console.log(value);
        console.log("Item:");
        console.log(dataProd);
        console.log(dataProd.cantidad);
        console.log(value.nivel_bajo);
        console.log(value.nivel_sobre);
        console.log(dataProd.alerta_bajo);
        console.log(dataProd.alerta_sobre);
        if (Number(dataProd.cantidad) == 0) {
          console.log("Cero DET");
          cero = cero + dataProd.nombre + ", ";
        }
        else if (Number(dataProd.cantidad) <= Number(value.nivel_bajo) & dataProd.alerta_bajo) {
          console.log("BAJO DET");
          bajos = bajos + dataProd.nombre + ", ";
        }
        else if (Number(dataProd.cantidad) >= Number(value.nivel_sobre) & dataProd.alerta_sobre) {
          console.log("SOBRE DET");
          sobres = sobres + dataProd.nombre + ", ";
        }
        console.log(bajos + "|" + sobres + "|" + cero);
      })

    });
  });
  await delay(1000);
  console.log(bajos + "|" + sobres + "|" + cero);
  if (bajos != "") {
    document.getElementById("bajoTxt").innerHTML = "Los siguientes Items tienen menos del stock registrado para este aviso: " + bajos;
    const toastbajos = new bootstrap.Toast(bajoToast);
    toastbajos.show();
  }
  if (sobres != "") {
    document.getElementById("sobreTxt").innerHTML = "Los siguientes Items tienen mas del stock registrado para este aviso: " + sobres;
    const toastsobres = new bootstrap.Toast(sobreToast);
    toastsobres.show();
  }
  if (cero != "") {
    document.getElementById("ceroTxt").innerHTML = "Los siguientes Items ya no tienen stock: " + cero;
    const toastcero = new bootstrap.Toast(ceroToast);
    toastcero.show();
  }

}





