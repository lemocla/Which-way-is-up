// Set image name when uploading image
$('#new-image').change(function () {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});
$('#id_portfolio').change(function () {});