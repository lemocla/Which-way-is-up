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

     //togle password

     // login page
     $('#div_id_password').append(
         '<i class="password-visible far fa-eye" data-target="id_password" aria-hidden="true"></i><span class="sr-only">toggle password</span>'
     )
     // register page
     $('#div_id_password1').append(
         '<i class="password-visible far fa-eye" data-target="id_password1" aria-hidden="true"></i><span class="sr-only">toggle password</span>'
     )
     $('#div_id_password2').append(
         '<i class="password-visible far fa-eye" data-target="id_password2" aria-hidden="true"></i><span class="sr-only">toggle password</span>'
     )

     $(".password-visible").click(function () {
         id = $(this).attr("data-target");
         if ($(`#${id}`).attr("type") == "password") {
             $(`#${id}`).attr("type", "text");
             $(this).removeClass("fa-eye").addClass("fa-eye-slash");
         } else if ($(`#${id}`).attr("type") == "text") {
             $(`#${id}`).attr("type", "password");
             $(this).removeClass("fa-eye-slash").addClass("fa-eye");
         }
     });
     //end file
 })