function sendinfo(){
    lon=$("#lon").val();
    lai=$("#lai").val();
    height=$("#height").val();
    drct=$("#drct").val();
    weight=$("#weight").val();
    $.ajax({
                    method:'GET',
                    url:"http://localhost:9000/judge_data/"+lon+'/'+lai+"/"+height+'/'+drct+'/'+weight,
                    dataType: "text",
                    success:function(result){
                        //console.log(result);
                        var re=JSON.parse(result);
                        $("#1").html(re[0]);
                        $("#2").html(re[1]);
                        $("#3").html(re[2]);
                        $("#4").html(re[3]);
                        $("#5").html(re[4]);

                    },
                    error:function(){
                         alert('error judge!')
                    }
                });

}