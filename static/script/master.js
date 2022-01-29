
function MovieSearch(event,formid,url)
{
    event.preventDefault();
    var form =  $('#'+formid)[0];
    var formdata =  new FormData(form);
    $.ajax({
        url:url,
        data:formdata,
        async:true,
        type:'POST',
        success:function(response,st,xml){
            if(st == 'success' && xml.status == 200)
            {
                $('div.searchresult').html(response);  
                $('div.searchresult').css({'display':'block'});
            }            
        },
        processData: false,
        contentType: false,
});
}