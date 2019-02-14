
function search(){
   $.ajax({
       type:"GET",
       datatype:"json",
       url:"/search",
       data:$("#searchkey").serialize(),
       success: function(result){
           console.log(result);
       },
       error:function(){
           console.log("failed");
       }
   }); 
}


function ginSubmitEmail() {
    //console.log($("#form_email").serialize())
    $.ajax({
        type: "POST",
        datatype:"text",
        url: "/form/email",
        data: $('#form_email').serialize(),
        success: function (result) {
            console.log(result["email"]);
            console.log(result["status"]);
            console.log(result["name"]);

            document.getElementById("result").innerHTML = result["email"] + " " + result["name"];

        },
        error: function () {
            console.log("error")
        }
    });
}

function ginSubSingleFile(){
    var files = document.getElementById("siglefile").files;
    var form_data = new FormData();
    form_data.append('upload', files[0]);
    $.ajax({
        type:"POST",
        datatype:"json",
        url:"form/file",
        data:form_data,
        contentType:false,
        processData:false,
        cache:false,
        success:function(result){
            console.log(result);
        }
    });
}

function ginSubMultiFiles(){
    var files = document.getElementById("multifile").files;
    var form_data = new FormData();
    for(var i = 0; i < files.length; i++){
        form_data.append("upload", files[i])
    }

    $.ajax({
        type:"POST",
        datatype:"json",
        url:"/form/files",
        data:form_data,
        contentType:false,
        processData:false,
        cache:false,
        success: function(result){
         console.log(result);   
        },
        error:function(){
            console.log("error");
        }
    });
}
