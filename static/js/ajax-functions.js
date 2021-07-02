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
            $("#id_status").text(result.mensagem);
        }
    });
}

// function process_response(funcionarios){
//     func_select = document.getElementById("funcionarios");
//     func_select.innerHTML = "";

//     funcionarios.forEach(function(funcionario){
//         var option = document.createElement("option");
//         option.text = funcionario.field.first_name;
//         func_select.add(option);
//     });

//}

// function filtrarFuncionario(){
//     depart_id = document.getElementsByName("departaments").value;
//     $.ajax({
//         type: 'GET',
//         url: '/collaborator/list_collaborator/',
//         data : {
//             other_params : depart_id
//         },
//         success: function(result){
//             process_response(result);
//             $("#mensagem").text('Funcionario Cadastrado')
//         }
//     });
// }


function alterarTask(id) {
   
    $.ajax({
            type: "GET",
            url: "/task/task-complete/"+id+"/",
            data : {
                id : id
            },
            success: function(result){
                M.toast({html: toastHTML});
        }
    })
}



function removeCollaborator(id, name){
    var elemnt = document.getElementById(name);  
    elemnt.parentElement.removeChild(elemnt);
    $.ajax({
        type:"GET",
        url:"/collaborator/remove-collaborator/"+id+"/",
        data: {
            id_collaborator: id
      
        },
        success: function(result){
            alert(`Ação Execeutada!:${result}`); 
        },failure: function(result){
            alert('Erro ao executar a tarefa!')
        }
    })
}

