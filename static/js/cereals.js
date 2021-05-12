$(document).ready(function() {
    function refreshCereals(event, new_search) {
        event.preventDefault();
        var searchText = $('#search-box').val();
        if (new_search) {
            var order_by = 'name';
            var filter_str = '';
        } else {
            var order_by = $('#order-selection').val();
            var filters = $('#select-filter').val();
            var filter_str = '';
            for (var i = 0; i< filters.length; i++) {
                if (i == filters.length-1) filter_str += filters[i]
                else filter_str += filters[i]+','
            };
        }
        $.ajax( {
            url: '/cereals?search_filter=' + searchText + '&order_by=' + order_by + '&filters=' + filter_str,
            type: 'GET',
            success: function (resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="cereal">
                                <a href="/cereals/${d.id}">
                                    <img class="cereal-img" src="${d.image}" />
                                    <h5 class = "cereal_name">${d.name}</h5>
                                    <div class = 'cereal-attribute'>
                                        <div> Price: ${d.price} ISK
                                            <br>
                                            Sugar: ${d.sugar}/100g
                                        </div>
                           
                                    </div>
                                </a>
                            </div>`
                });
                $('.cereals').html(newHtml.join(''));
                if (new_search) {
                    $('#order-selection').val('name');
                    $('#select-filter').val('');
                };
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    };
    function refreshSearchHistory(event) {
        event.preventDefault();
        $.ajax({
            url: '/cereals?search_history=',
            type: 'GET',
            success: function (resp) {
                let search_query;
                let newLine = '';
                let search;
                let newHtml = '<button class="dropbtn">Search history</button>\n' +
                    '<div class="dropdown-content">';
                for (search in resp.data) {
                    search_query = resp.data[search]['search_query']
                    newLine = '<option class = "search_history_item" value="' +
                        search_query +
                        '">' +
                        search_query+
                        '</option>';
                    newHtml += newLine + '\n'
                };
                newHtml += '</div>';
                $('.search-history-dropdown').html(newHtml);
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    };
    $('#search-btn').on('click', function(event) {
        refreshCereals(event, true);
        refreshSearchHistory(event);
    });
    $("#order-selection").change( function(event) {
        refreshCereals(event, false);
    });
    $("#select-filter").change( function(event) {
        refreshCereals(event, false);
    });
    $('.search_history_item').on('click', function(event) {
        let searchText = $(this).attr('value');
        console.log(searchText);
        $('#search-box').val(searchText);
        refreshCereals(event, true);
    });
});


