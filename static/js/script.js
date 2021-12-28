 $(document).ready(function () {

     // Toast
     $('.toast').toast('show');

     // Add artwork to wishlist 
     $('button[data-action=add-wishlist]').click(function (e) {
         let csrfToken = $('input[name=csrfmiddlewaretoken]').val();
         let artworkId = $(this).attr('data-item');
         let url = `/my_profile/add_to_wishlist/${artworkId}`;
         let data = {
             'csrfmiddlewaretoken': csrfToken
         };

         $.post(url, data)
             .done(function () {
                 location.reload();
             });
     })

     // Remove artwork to wishlist 
     $('button[data-action=remove-from-wishlist]').click(function (e) {
         let csrfToken = $('input[name=csrfmiddlewaretoken]').val();
         let artworkId = $(this).attr('data-item');
         let url = `/my_profile/remove_from_wishlist/${artworkId}`;
         let data = {
             'csrfmiddlewaretoken': csrfToken
         };

         $.post(url, data)
             .done(function () {
                 location.reload();
             });
     })

 })