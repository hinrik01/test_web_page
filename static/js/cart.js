$(document).ready(function() {
    function refresh_total_price() {
        $.ajax({
            url: '/cart/get_cart',
            type: 'GET',
            success: function (response) {
                newHtml = '<h5>Total price: ' + response.data.total_price + ' kr</h5>';
                $('#cart-total-price').html(newHtml);
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        });
    };
    $('.cart-item-quantity').change(function () {

        var cereal_id;
        var quantity;
        cereal_id = $(this).attr("data-cereal-id");
        quantity = $(this).val();

        $.ajax({
            url: '/cart/update_quantity/' + cereal_id + '/' + quantity,
            type: 'GET',
            success: function (resp) {
                refresh_total_price()
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    });
    $('.cart-item-delete-btn').on('click', function () {
        $(this).parent().parent().hide()

        var cereal_id;
        cereal_id = $(this).attr("data-cereal-id");
        $.ajax({
            url: '/cart/delete_from_cart/' + cereal_id,
            type: 'GET',
            success: function () {
                refresh_total_price()
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        });
    });
    function refresh_cart() {
        $.ajax({
            url: 'get_cart',
            type: 'GET',
            success: function (response) {
                var cart_items = response.data.cart_items

                var newHtml = cart_items.map(cart_item => {
                    return `<div class="cart-item-container" >
                                <h6 class="cart-item-name">${cart_item.cereal_name}</h6>

                                    <div class="cart-item-quantity-container">
                                    <input  class="cart-item-quantity" type="number" name="quantity" data-cereal-id="${cart_item.cereal_id}" value="${cart_item.quantity}" style="width: 40px">
                                    <button class="cart-item-delete-btn" data-cereal-id="${cart_item.cereal_id}" >Delete</button>
                                </div>
                            </div>`
                });
                newHtml = newHtml.join('');
                newHtml += '<h5 id="cart-total-price">Total price: ' + response.data.total_price + ' kr</h5>';
                $('.cart-items-container').html(newHtml);
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        });
    };
});