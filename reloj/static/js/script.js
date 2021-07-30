function mueveReloj(){
    momentoActual = new Date()
    hora = momentoActual.getHours()
    minuto = momentoActual.getMinutes()
    segundo = momentoActual.getSeconds()
    dia = momentoActual.getDate()
    mes = momentoActual.getMonth()
    año = momentoActual.getFullYear()

    horaImprimible = dia + " - " + mes + " - " + año + " / " + hora + " : " + minuto + " : " + segundo

    document.form_reloj.reloj.value = horaImprimible

    setTimeout("mueveReloj()",1000)
}

hora = new Date()