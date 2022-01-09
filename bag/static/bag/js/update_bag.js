// Update quantity
$('select[data-action=update-bag]').change(function (e) {
    let csrfToken = $('input[name=csrfmiddlewaretoken]').val();
    let artworkId = $(this).attr('data-item');
    let url = `/bag/adjust/${artworkId}/`;
    let data = {
        'csrfmiddlewaretoken': csrfToken,
        'quantity': $(this).val()
    };
    // ajax call to update quantity
    $.post(url, data)
        .done(function () {
            location.reload();
        });
});

// Remove from bag
$('button[data-action=remove-from-bag]').click(function (e) {
    let csrfToken = $('input[name=csrfmiddlewaretoken]').val();
    let artworkId = $(this).attr('data-item');
    let url = `/bag/remove/${artworkId}/`;
    let data = {
        'csrfmiddlewaretoken': csrfToken,
    };
    // ajax call to remove bag
    $.post(url, data)
        .done(function () {
            location.reload();
        });
});