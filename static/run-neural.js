function run(){
    $('#start').addClass('disabled');
    eta=$("#eta  option:selected").val();
    n=$("#n  option:selected").val();
    $.ajax({
                    method:'GET',
                    url:"http://localhost:9000/run/"+eta+'/'+n,
                    dataType: "text",
                    success:function(result){
                        console.log(result);
                    },
                    error:function(){
                         alert('error start!')
                    }
                });
}

function re_run(){
    location.replace("http://localhost:9000/neural");
}