function validaUsuario() {
    var user = false;
    var pass = false;
    var usuario = $(document).getElementById("#txtemail").value;
    user = !usuario.includes("@") & !usuario.includes(".");
    var clave = $("#txtclave").val();
    pass = clave.length < 1;
    if (user | pass) alert("Revise " + (user ? "Usuario" : "") + (user & pass ? " y " : "") + (pass ? "Clave" : ""));
}