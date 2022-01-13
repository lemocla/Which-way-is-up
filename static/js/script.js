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
         // post to add to wishlist
         $.post(url, data)
             .done(function () {
                 location.reload();
             });
     });

     // Remove artwork to wishlist 
     $('button[data-action=remove-from-wishlist]').click(function (e) {
         let csrfToken = $('input[name=csrfmiddlewaretoken]').val();
         let artworkId = $(this).attr('data-item');
         let url = `/my_profile/remove_from_wishlist/${artworkId}`;
         let data = {
             'csrfmiddlewaretoken': csrfToken
         };
         // post to remove from wishlist
         $.post(url, data)
             .done(function () {
                 location.reload();
             });
     });

     //togle password

     let style; //Additional styles for change password page
     if ($('h1').text()=="Change Password"){
     style='style="right: 42rem;"';
     }

     // login page
     $('#div_id_password').append(
         '<i class="password-visible far fa-eye" data-target="id_password" aria-hidden="true"></i><span class="sr-only">toggle password</span>'
     );
     // register page
     $('#div_id_password1').append(
         `<i class="password-visible far fa-eye" data-target="id_password1" aria-hidden="true" ${style}></i><span class="sr-only">toggle password</span>`
     );
     $('#div_id_password2').append(
         `<i class="password-visible far fa-eye" data-target="id_password2" aria-hidden="true" ${style}></i><span class="sr-only">toggle password</span>`
     );
     // toggle function
     $(".password-visible").click(function () {
         let id = $(this).attr("data-target");
         if ($(`#${id}`).attr("type") == "password") {
             $(`#${id}`).attr("type", "text");
             $(this).removeClass("fa-eye").addClass("fa-eye-slash");
         } else if ($(`#${id}`).attr("type") == "text") {
             $(`#${id}`).attr("type", "password");
             $(this).removeClass("fa-eye-slash").addClass("fa-eye");
         }
     });

     // Check for invalid fields and display error message
     $('button[type="submit"]').click(function () {
         $('form').addClass('submitted');
         $('*:not(form):invalid').each(function () {
             let id = $(this).attr('id');
             let label = $(`label[for="${id}"]`).text().replace('*', '');
             if ($(`p[data-error="${id}"]`).length == 0) {
                 $(this).parent().append(
                     `<p class="red-text pt-1 my-0 small" data-error="${id}">Enter a valid ${label}</p>`
                 );
             }
         });
     });

     // Remove error message when input is valid
     $('*:not(form):invalid').change(function () {
         if ($(this).is(":valid")) {
             let id = $(this).attr('id');
             $(`p[data-error="${id}"]`).remove();
         }
     });

 });