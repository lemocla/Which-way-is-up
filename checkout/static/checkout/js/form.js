$(document).ready(function () {

    // function to display error message if delivery country is not UK
    function countryCheck() {
        if ($('#id_delivery_country').val()) {
            if ($('#id_delivery_country').val() != 'GB') {
                $('#country-error').removeClass('hide');
            } else {
                $('#country-error').addClass('hide');
            }
        }
    }

    // Select GB address by default
    $('#id_delivery_country').val('GB');

    // Style placeholders for delivery & billing countries
    // Adapted from Code Institute Boutique Ado project
    $('.lazyselect ').each(function () {
        let countrySelected = $(this).val();
        if (!countrySelected) {
            $(this).css('color', '#6c767d');
        }
        $(this).change(function () {
            countrySelected = $(this).val();
            if (!countrySelected) {
                $(this).css('color', '#6c767d');
            } else {
                $(this).css('color', '#0D0000');
            }
        });
    });

    // on load - display gift option if option is checked
    if ($('#is_auth').val() == 'true') {
        $('#id_email').prop('readonly', 'readonly');
    }

    if ($('#is_gift').val() == 'on') {
        $('#id_gift_option').attr('checked', true);
        $('#gift-option-container').removeClass("hide");
        if ($('#gift-message').val() != "None") {
            let msg = $('#gift-message').val();
            $('#id_gift_message').val(msg);
        }
    }

    // check default country
    countryCheck();

    // default display for billing address block
    if ($('#id_billing_same_as_delivery').is(":checked")) {
        $('#billing-details-container').addClass('hide');
    } else {
        $('#billing-details-container').removeClass('hide');
    }

    // remove default required attribute
    $('#id_billing_street_address1').prop('required', false);
    $('#id_billing_town_or_city').prop('required', false);
    $('#id_billing_postcode').prop('required', false);
    $('#id_billing_country').prop('required', false);

    // display error message if country selected is not UK
    $('#id_delivery_country').change(function () {
        countryCheck();
    });

    // toggle billing container if delivery details are different than billing details 
    $('#id_billing_same_as_delivery').change(function () {
        if ($('#id_billing_same_as_delivery').is(":checked")) {
            $('#billing-details-container').addClass('hide');
            $('#id_billing_street_address1').val($('#id_delivery_street_address1').val()).prop('required', false);
            $('#id_billing_street_address2').val($('#id_delivery_street_address2').val());
            $('#id_billing_town_or_city').val($('#id_delivery_town_or_city').val()).prop('required', false);
            $('#id_billing_postcode').val($('#id_delivery_postcode').val()).prop('required', false);
            $('#id_billing_county').val($('#id_delivery_county').val());
            $('#id_billing_country').val($('#id_delivery_country').val()).prop('required', false);
        } else {
            $('#billing-details-container').removeClass('hide');
            $('#id_billing_street_address1').val("").prop('required', true);
            $('#id_billing_street_address2').val("");
            $('#id_billing_town_or_city').val("").prop('required', true);
            $('#id_billing_postcode').val("").prop('required', true);
            $('#id_billing_county').val("");
            $('#id_billing_country').val("").prop('required', true);
        }
    });

    // display gift message container
    $('#gift-checkbox').change(function () {
        if ($('#gift-checkbox').is(":checked")) {
            $('#form-message-container').removeClass('hide');
        } else {
            $('#form-message-container').addClass('hide');
        }
    });

    // add gift option
    $('#id_gift_option').change(function () {
        if ($('#id_gift_option').is(":checked")) {
            // display gift option container
            $('#gift-option-container').removeClass("hide");
            // set is gift to true
            $('#is_gift').prop('checked', true);
        } else {
            $('#gift-option-container').addClass("hide");
            $('#form-message-container').addClass('hide');
            // remove values of field 
            $('#is_gift').prop('checked', false);
            $('#gift-checkbox').prop('checked', false);
            $('#id_gift_recipient').val("");
            $('#id_gift_message').val("");
        }
    });
});