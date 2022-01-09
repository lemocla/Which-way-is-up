// Adapted from Code Institute Boutique Ado project
let countrySelected = $('#id_country').val();
if (!countrySelected) {
    $('#id_country').css('color', '#6c767d');
}
$('#id_country').change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
        $(this).css('color', '#6c767d');
    } else {
        $(this).css('color', '#0D0000');
    }
});