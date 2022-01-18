//bespoke responsive carousel for related items

let screenSize = $(window).width();

// Adjust number of cards in the carousel
let nb = 2;
if (screenSize >= 768) {
    nb = 3;
}
if (screenSize >= 1200) {
    nb = 4;
}

// Variables 
let index_display = 0;
let list_items = $('.card-items');

// disable previous on start  
$('#previous').prop('disabled', true);

// hide buttons if list length is below n
if (list_items.length <= nb) {
    $('#previous').hide();
    $('#next').hide();
}

// reset carousel on screen change
$(window).on('resize', function () {
    // get screen width
    screenSize = $(window).width();
    let new_nb;
    // new number of card in container
    if (screenSize < 768) {
        new_nb = 2;
    }
    if (screenSize >= 768 && screen < 1200) {
        new_nb = 3;
    }
    if (screenSize >= 1200) {
        new_nb = 4;
    }
    nb = new_nb;
    // reset carousel display
    $.each(list_items, function (index, element) {
        if (index >= 0) {
            $(this).removeAttr('style');
        }
    });
    // reset button display
    index_display = 0;
    $('#next').prop('disabled', false);
    $('#previous').prop('disabled', true);
    if (list_items.length <= nb) {
        $('#previous').hide();
        $('#next').hide();
    } else {
        $('#previous').show();
        $('#next').show();
    }
});

// next button actions
$('#next').click(function () {
    // enable previous button
    $('#previous').prop('disabled', false);
    $.each(list_items, function (index, element) {
        // calculate endpoint
        let endpoint = index_display + nb;
        // hide current n items
        if (index >= index_display && index < endpoint) {
            $(this).hide();
        }
        if (index > (index_display + nb)) {
            $(this).removeAttr('style');
        }
    });
    // calculate new start index
    index_display = index_display + nb;
    // disable next buttons if no further n to display
    if ((index_display + nb) >= list_items.length) {
        $('#next').prop('disabled', true);
    }
});

// previous button actions
$('#previous').click(function () {
    $.each(list_items, function (index, element) {
        // calculate endpoint
        let endpoint = index_display - nb;
        if (endpoint < 0) {
            endpoint = 0;
        }
        // show previous n items
        if (index >= endpoint && index < index_display) {
            $(this).removeAttr('style');
        } else {
            $(this).hide();
        }
    });
    // calculate new index start
    index_display = index_display - nb;
    if (index_display < 0) {
        index_display = 0;
    }
    // disable previous button if new index is 0
    if (index_display == 0) {
        $('#previous').prop('disabled', true);
        $('#next').prop('disabled', false);
    }
});