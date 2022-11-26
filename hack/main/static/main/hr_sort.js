document.addEventListener('click', e =>
get_bd(e));

function get_bd(e){
    var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url:  '/jobs',
        cache: false,
        dataType: "json",
        data: {"classs": e.target.class, "ids": e.target.id, 'csrfmiddlewaretoken': csrftoken},
        succes: function(html){
            var html = JSON.parse(html["data"]);
            var data = "";
            for (var i=0; i < html.length; i++){
                alert((html[i])["fields"])
            }
        }
    })
}