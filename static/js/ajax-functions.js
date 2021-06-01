var toastHTML = '<span>Alteração:</span><button class="btn-flat toast-action">Success</button>';
      
function utilizouHoraExtra(id) {

    token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    $.ajax({
        type: 'POST',
        url: '/hourdatabase/utilizar_hora/'+id+'/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result) {
            // M.toast({html: toastHTML});
            $("#total").text(result.horas);
        },
        failure: function(result){
            // $("#mensagem").text(result.mensagem);
            
        }
    });
}

function DisponibilizarHoraExtra(id) {
    token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    $.ajax({
        type: 'POST',
        url: "/hourdatabase/disponibilizar_hora/"+id+'/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            // M.toast({html: toastHTML});
            $("#total").text(result.horas);
        }
    });
}

// function RefreshDetailFuncionario(id) {
//     $.ajax({
//         type: "GET",
//         url: "/collaborator/collaborator_detail/"+id+"/",
//         success: function(result){
//             M.toast({html: toastHTML})
//         }
//     })
// }