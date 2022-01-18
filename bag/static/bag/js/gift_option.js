// Gift option on load - if in session
if ($('#order-is-gift').attr('data-session') == 'on') {
    $('#order-is-gift').attr("checked", true);
    $('#gift-container').removeClass('gift-display');
}

// Display gift message when gift option is true
$('#order-is-gift').change(function () {
    if ($('#order-is-gift').is(":checked")) {
        // display gift message
        $('#gift-container').removeClass('gift-display');
        // add gift option to session
        let csrfToken = $('input[name=csrfmiddlewaretoken]').val();
        let url = `/bag/gift_option/`;
        let data = {
            'csrfmiddlewaretoken': csrfToken,
            'is_gift': $("#order-is-gift").val(),
            'gift_message': $('#gift-message').val()
        };
        $.post(url, data);
    } else {
        // hide gift message
        $('#gift-container').addClass('gift-display');
        $("#gift-message").val("");
        // add to session
        let csrfToken = $('input[name=csrfmiddlewaretoken]').val();
        let url = `/bag/gift_option/`;
        let data = {
            'csrfmiddlewaretoken': csrfToken,
            'is_gift': false,
        };
        $.post(url, data);
    }

    // Put message and gift option in session when message is entered
    $('#gift-message').focusout(function () {
        // add to session
        let csrfToken = $('input[name=csrfmiddlewaretoken]').val();
        let url = `/bag/gift_option/`;
        let data = {
            'csrfmiddlewaretoken': csrfToken,
            'is_gift': $("#order-is-gift").val(),
            'gift_message': $('#gift-message').val()
        };
        $.post(url, data);
    });
});

// Edit gift message
$('#gift-message').focusout(function () {
    if ($('#order-is-gift').attr('data-session') == 'on') {
        // add to session
        let csrfToken = $('input[name=csrfmiddlewaretoken]').val();
        let url = `/bag/gift_option/`;
        let data = {
            'csrfmiddlewaretoken': csrfToken,
            'is_gift': $("#order-is-gift").val(),
            'gift_message': $('#gift-message').val()
        };
        $.post(url, data);
    }
});