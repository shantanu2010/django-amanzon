function search(){

   var query=$('#txtbox').val();

    if(query==""){
        $('.searchresults').html("");
    }

    else{
        $.ajax(
            {
                type:"GET",
                dataType:'json',
                url: "/api/search/",
                data:{
                     query:query,
                },
                success: function( data ){

                    var tab=$('<div />');
                    var i = 0
                    for(i=0;i<data.length;i++){

                        tab.append('<p>');
                        var uid=data[i].id;
                        var slug=data[i].slug;
                        $('<a />', {value: data[i].name, text: data[i].name,id:data[i].id,href:"https://shantanuonlinestore.herokuapp.com/"+uid+"/"+slug+"/"}).appendTo(tab);
                        tab.append('</p>');

                    }

                    if(i==0){

                        tab.append('<p>')
                        $('<a/>',{value:"No Item Found"}).appendTo(tab)

                    }

                    $('.searchresults').html(tab);
                },
            error: function(jqXHR, textStatus, errorThrown){
                alert('error');
            }
        })
      }
}
