// Remove current artwork from related item when editing artwork
let artworkId = JSON.parse(document.getElementById('artworkId').textContent);
$(`#id_related_items option[value="${artworkId}"]`).remove();