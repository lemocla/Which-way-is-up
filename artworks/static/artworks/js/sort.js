//reload page content according to sorting options
$('#sort-selector').change(function () {
    let selector = $(this);
    let currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    if (selectedVal != 'reset') {
        let sort = selectedVal.split('_')[0];
        let direction = selectedVal.split('_')[1];

        currentUrl.searchParams.set('sort', sort);
        currentUrl.searchParams.set('direction', direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete('sort');
        currentUrl.searchParams.delete('direction');

        window.location.replace(currentUrl);
    }
});