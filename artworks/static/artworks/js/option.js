let artworkId = JSON.parse(document.getElementById('artworkId').textContent);
$(`#id_related_items option[value="${artworkId}"]`).remove();