$(document).ready(function(){

    function handleMenuOrdering(e){
        var url = new URL(window.location.href);
        var ordering = url.searchParams.get('order_by');
            if(ordering){
                this.href = this.href + '&order_by=' + ordering;
            }
     }

    $('#prev').click(handleMenuOrdering);
    $('#next').click(handleMenuOrdering);

    $('.menu').click(function(e){
        var currentOrdering = window.location.href.split('order_by=')[1];
        var newOrdering = this.href.split('order_by=')[1]

        if(currentOrdering == newOrdering){
            newOrdering = currentOrdering.startsWith('-') ? currentOrdering.substr(1) : '-' + newOrdering;
            var split = this.href.split('order_by=');

            this.href = split[0] + 'order_by=' + newOrdering;
        }
    });


    $('.menu-item').click(function(e){
        var menuId = this.children[0].innerText;
        var endpointUrl = window.location.origin + '/api/menu/' + menuId;

        $.get(endpointUrl, function( data ) {
            $('.menu-name').html(data.name);
            $('.menu-description').html(data.description);

             $.each(data.dishes, function(index, value){
                addTableRow('.dish-row', value);
              });

              $('.menu-details').show();
              $('.menu-list').hide();

              history.pushState(null, null, window.location.origin + '/' + menuId + '/');

        });

    });

    function addTableRow(className, dish){
        var template = '<tr>';

        $.each(dish, function(key, value){

            if(key === 'id'){
                template +='<th scope="row">' + value + '</th>';
            }else if(key === 'is_vegetarian'){
                template += value ? '<td>Tak</td>' : '<td>Nie</td>'
            }
            else{
            template +='<td>' + value + '</td>';
            }
        });

        template +='</tr>';

        $(className).append(template);
    }
});
