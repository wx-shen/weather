function sendpath(){
    path=[['125','49','1000','200','500'],['126','45','900','200','500'],['88','47','800','200','500']];
    data=JSON.stringify(path);
     $.ajax({
                    method:'POST',
                    url:"http://localhost:9000/path",
                    data: data,
                    success:function(data){
                        alert(data);
                    },
                    error: function(XMLHttpRequest, textStatus, errorThrown) {
                        alert(XMLHttpRequest.status);
                        alert(XMLHttpRequest.readyState);
                        alert(textStatus);
                    }
                });
}