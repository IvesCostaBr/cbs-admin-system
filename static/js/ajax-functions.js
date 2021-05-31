function utilizouHoraExtra(id) {
    console.log(id)
    token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    

    $.ajax({
        type: 'POST',
        url: '/hourdatabase/utilizar_hora/'+id+'/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result) {
            $("#mensagem").text('Hora extra marcada como utilizada');
        },
        failure: function(result){
            $("#mensagem").text('Deu errado :(')
        }
    });
}