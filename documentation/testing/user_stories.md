 # TESTING USER STORIES
  
  [Return to main ReadMe](/README.md)
  
  - ## **Navigation and website experience**
  
    - ### **As a site user, I want a responsive website so that I can access it on different devices.**
      - When I visit the website using my device, the content is optimized for that device
      - On a mobile and tablet the navigation bar is collapsed
      - When the navigation is collapsed, a toggle button is displayed to right of the header, and
      - When I click on the toggle button, a vertical menu is displayed,
      - When I click again on the toggle button, the vertical menu collapses back.
      - **Result**: Pass ✅
      
      **Example responsive screen**
      ![example responsive screen](screenshots/responsive_screen.png)

      **Mobile navbar**
      ![mobile nabar](screenshots/mobile_navbar.png)

      **Ipad navbar**
      ![tablet navbar](screenshots/tablet_navbar.png)

    - ### **As a site user, I want to easily navigate across the site so that I can find the information I need.**
      - When I hover on a menu item in the top navigation bar, its appearance changes.
      - When I click on a menu item in the navigation bar, the relevant page is displayed without errors.
      - When I click on any link in the footer, the relevant page is displayed without errors.
      - **Result**: Pass ✅

      **Desktop navbar**
      ![desktop navbar](screenshots/navbar.png)

    - ### **As a site user, I want to read about the artist so that I can learn about artist background and exhibitions**
      - When I click on the "about" menu item in the top navigation bar, the "about me" page is displayed with
      - an image of the artist,
      - biography about the artis and,
      - a list of exhibitions and events
      - **Result**: Pass ✅

      **Artist biography**
      ![artist biography](screenshots/artist_bio.png)

      **Events section**
      ![about page events](screenshots/about_events.png)
      
    - ### **As a site user, I want to view the artist work so that can understand the artist work**
        - When I click on the menu item "work", a secondary drop down menu is displayed with the name of the artist work (collection) and,
        - When I cick on a collection, I am redirected to the relevant page where information and an image library are displayed,
        - When I hover an image in the library, an overlay features a series of three buttons as follows:
        - When I click on button with the magnifying glass icon, a modal window opens with a zoom image of the artwork
        - When I click on the button with the information icon, I am redirected to the product page
        - When I click on the button with heart icon and if I am authenticated the artwork is added to my wishlist and the appearance of the icon changes to red.
        - When I click on the button with the heart icon and I am not authenticated I am redirected to the login page.
        - **Result**: Pass ✅

      **Portfolio page with image library**
      ![example of collection page](screenshots/collection.png)

      **Overlay over artwork image with buttons**
      ![overlay with buttons](screenshots/image_overlay.png)

      **Zoom modal**
      ![zoom image](screenshots/image_zoom.png)

      **Item added to wishlist**
      ![item added to wishlist](screenshots/image_overlay_favourite.png)

    - ### **As a site user, I want to see the details for an artwork so that I can get a better appreciation and decide if I would want to buy it**
        - **Path 1**
            - When browsing a collection and when I click on image of an artwork,
            - I am redirected to page where the details for this artwork is displayed, including an image, a title, as well as the size for this artwork, related artworks and reviews (if they're are any)
            - If the artwork is available for sale, its price will be displayed as well as a button to add to cart,
            - If the artwork is not available for sale, a button inviting to contact the artist is displayed.
            - **Result**: Pass  ✅

        - **Path 2**
            - When I browse the shop and when I click on an image of an artwork, 
            - I am redirected to page where the details for this artwork is displayed, including an image, a title, the size for this artwork, its price as well as related artworks and reviews (if they're are any) and,
            - A button to add to cart is also displayed
            - **Result**: Pass  ✅

        **Example of product page with add to cart button**
        ![product page with add to cart button](screenshots/artwork_page_cart.png)

        **Example of product page with contact us button**
        ![product page with contact us button](screenshots/artwork_page_contact.png)

    - ### **As site user, I want to engage with the artist work so that I can be part of the artist community**
        - When I browse down the homepage, a section with downloadable colouring page is displayed as well as a hashtag encouraging me to share my colouring work with the artist on social media,
        - When I click on the image, the content is downloaded on my device where I should be able to open the colouring sheet in pdf format and print it
        - **Result**: Pass ✅

        **Homepage colouring section**
        ![colour-me section](screenshots/home_colourme.png)

 - ## **Shopping experience** 
 
    - ### **As a shopper, I want to view all the artwork available so that I can quickly have an overview of what is on offer**
      - When I select "all", from the shop in the top navigation bar, I can see all the artwork available with an image, a title and a price being displayed, as well as items out of stock and items for sales
      - When I hover the artwork name, the text is underlined and when I click on the link I am redirected the artwork detailed page
      - When I click on the "shopping bag" button, the artwork is added to my shopping bag and a toast message is displayed with a summary of my shopping bag
      - When I click on the button with a heart icon and I am logged in, the artwork will be added to my wishlist but,
      - If i click on the button with heart icon and I am not authenticated, a toast message will invite me to either login or register.
      - **Result**: Pass ✅

      **Shop all page**
      ![Shop all](screenshots/Shop.png)

      **Info message when user tries to add item to wishlist and not authenticated**
      ![info message not auth users](screenshots/shop_wishlist_info.png)

    - ### **As a shopper, I want to view available artwork by specific category so that I can quickly find products I’m interested in.**
        - When in the navigation bar, I can select a category of artwork, 
        - When I select a category, the artwork related to that category is displayed
        - **Result**: Pass ✅

      **Shop navigation bar**
      ![Shop navigation](screenshots/shop_category.png)

      **Shop page example**
      ![Shop page example](screenshots/shop_page.png)

    - ### **As a shopper, I want to sort the list of artwork available by price so that I can find a piece in my price range**
      - When I am browsing the shop, either by category, collection - I can a "sort by" select field, where I can sort items by price or alphabetical order,
      - When I click on sort by price low to high, the page refresh with all the artwork arranged in pricing order from the lowest to the highest,
      - When I click on sort price high to low, the page refreshes will all the artwork arranged in pricing order from the highest to lowest
      - **Result**: Pass ✅

      **Sort filter options**
      ![sort filter options](screenshots/shop_sort.png)

      **Sort result display**
      ![sort display](screenshots/shop_sort.png)

    - ### **As a shopper, I want to view the artwork price and details so that I can make an informed decision**
      - When I browse the shop - either viewing all items or specific category of items and,
      - I can see, in addition of the image, the artwork title and price and,
      - When I hover the artwork, its appearance changes and,
      - When I click on the artwork, I am redirected the artwork detail page where all the details for the artwork is displayed including its price.
      - **Result**: Pass  ✅

    - ### **As a shopper, I want to read reviews so that I can have a better understanding of the quality of the artist work**
      - **Path 1**:
        - When I browse down the homepage, I can see a section with some reviews and button to see more reviews,
        - When I click on the button "more reviews, I am redirected to a page with all the reviews
        - **Result**: Pass ✅

        ![homepage review section](screenshots/reviews-home.png)

        ![reviews page](screenshots/reviews.png)

      - **Path 2**:
        - When I browse an artwork details, I can see a section at the bottom of the page with product reviews.
        - **Result**: Pass ✅
        
        **Product page review section**
        ![product page review section](screenshots/product_page_reviews.png)

    - ### **As a shopper, I want to view related items so that I can purchase several artwork**
        - When I browse an artwork detail page from the shop, a section named "You may also like" is displayed with image of related artwork, 
        - When I click on a related artwork, I am redirected to the relevant detail page for this artwork.
        - **Result**: Pass ✅

        **Related items**
        ![related items](screenshots/related_items.png)
  
    - ### **As a shopper, I want to select quantity of an item if applicable so I can order what I need**
        - When I browse an artwork detail page and / or my wishlist and, 
        - If the artwork is available to purchase in multiple quantity, 
        - A select tag with a label "quantity" is displayed and, 
        - When I click on the select field, the list of available quantities is displayed
        - When I select a quantity in the select field and click on add to bag, the right quantity for the relevant artwork is added to the shopping bag and a notification message is displayed.
        - **Result**: Pass ✅

        **Quantity available is one**
        ![select quantity 1](screenshots/quantity_1.png)

        **Quantity availabel is more than one**
        ![related items](screenshots/quantity.png)

        **Add to bag success message and bag summary**
        ![add to bag success message](screenshots/bag-toast.png)

- ## **Shopping bag and checkout**

    - ### **As a shopper, I want to review items in my shopping bag so that I can adjust quantities ordered**
      - When I browse my shopping bag, I can see a list of items in my bag with thumbnail, title, quantity and subtotals,
      - When I click in the select field under the quantity column and changes the quantity, the subtotals and totals adjust accordingly
      - When I click on the "bin" icon, the item is removed from my shopping bag and the subtotals as well as totals are adjusted accordingly
      - When I click on the button "move to wishlist" and if I am authenticated, the artwork will be added to my wishlist and a success message will display
      - When I click on wishlist and I am not authenticated, a message will display inviting me to either login or register
      - When I click on on the button "Continue Shopping", I am redirected to the previous shopping page
      - When I click on checkout, I am redirected to the checkout page
      - **Result**: Pass  ✅

      **Update quantity**
      ![update quantity](screenshots/bag_update.png)

      **Remove items**
      ![remove item from bag](screenshots/bag_remove.png)

      **Add item to wishlist from shopping bag and user is not registered**
      ![add to wishlist not registered users](screenshots/bag_info_wishlist.png)

      **Defensive design: Attempting to remove item not in the list**
      ![remove item not in the list](screenshots/bag_remove_error.png)

    - ### **As a shopper, I want to have a gift option so I can buy a print / piece of art for a special occasion for a friend**
      - When on the shopping bag and /or checkout page,
      - I can see a checkbox entitled "gift option",
      - When I check "gift option", additional fields are displayed such as the name of the recipient and a message to be sent alongside the item
      - **Result**: Pass  ✅
  
    - ### **As a shopper, I want to enter payment information in a safe and secure way so that I can checkout quickly with confidence**
      - When on the checkout page, I can see a paiement details section at the bottom of the page with field asking me for my debit/credit card details, expiry date and CVC
      - When I complete these details correctly and click "checkout" I am redirected to an order confirmation page and I also can see a notification informing me of my successful order.
      - When I complete these details incorrectly and click "checkout", an error message will display prompting me to enter the correct information.
      - **Result**: Pass  ✅


    - ### **As a shopper, I want to receive confirmation of my order so that I can have a proof of purchase**
      - When I click on the checkout and all the details on the checkout page, I am redirected to an order confirmation page with the details for my order, my details as well as delivery information. 
      - I should also receive an email with my order details with the same information as on the order confirmation page.
      - **Result**: Pass  ✅

      
 
- ## **Registration and account management** 

    - ### **As a site user, I want to register for an account so that I can view my orders and my favourite items** 

        - **Navigation**
            - When I click on the "user" icon, a dropdown menu is displayed with the options to login and to register,
            - When I click on the secondary menu item "Register", a form is displayed prompting me to complete my email, a username and a password.
            - **Result**: Pass
        - **Form valid path**
            - when I enter my email in the "email” field and
            - When I enter my username in the “username” field and,
            - When I enter a valid password of a minimum of 8 characters including a mix of letters, numbers and symbols including a capital letter,
            - A message informing me to verify my email address is displayed.
            - **Result**: Pass
        - **Form invalid path**
            - When I enter invalid email in the “email” field and or leave the field empty, and/or
            - when I enter an invalid username address in the “username” field or leave the field empty and if
            - When I enter an invalid password or leave the password field empty,
            - Errors messages will display and I will be prompted to input valid information
            - **Result**: Pass
        - **Invalid path: existing user**
            - When I enter credentials for a user that already exists, 
            - An error message will display to inform me that a user already exists with these credentials and inviting me to log in instead. 
            - **Result**: Pass

    - ### **As a site user, I want to login and logout so that I can access my profile safely**
        - **Navigation**
            - When I click on the "user" icon, a dropdown menu is displayed with the options to login and to register,
            - When I click on the secondary menu item "Login", a form is displayed prompting me to complete my email and a passwork.
            - **Result**: Pass

        - **Form valid path**
            - When I enter my email in the “email” field and
            - When I enter my password in the “password” field and,
            - If the information match my account, a success message is displayed informing me that I have successfully logged in.
            - **Result**:  Pass

        - **Form invalid path: Incorrect credentials**
            - If I enter the wrong password/email, a message will display to inform me that my credentials are incorrect, 
            - **Result**: Pass

        - **Form invalid path: invalid input**
            - If I enter invalid email in the “email” field or leave the field empty, and/or
            - If I leave the passwword field empty,
            - A message will display and I will be prompted to fill valid information and
            - **Result**: Pass

    - ### **As a site user, I want to edit my profile so that I can update my personal information**
        - **Navigation**
            - When I have successfully logged in and,
            - When I click on the user icon, a dropdown menu is displayed,
            - When I click on my profile, I am redirected to my profile page with the details I've already entered displayed in a a form
            - **Result**: Pass
       - **Edit profile - valid path**
            - When I edit a field in my personal information in the valid format and click on "update my profile", 
            - My profile is updated and a message informing me that my profile has been successfully updated is displayed.
            - Results: Pass
        - **Edit profile invalid path**
            - If I enter information in an invalid format or
            - A message error under the relevant field will display prompting me to enter the right information
            - **Result**: Pass

    - ### **As a site user, I want to reset my password if I forgot it so that I can access my account**
        - **Navigation**
           - When I am the login page, I can see a link "reset your password" and,
           - When I click on the link "reset my password", I am redirected to a page asking me for an email address and a button to reset my password
           - **Result**: Pass      
        - **Valid path**
            - When I enter a valid address and I click the button "reset my password", I should receive an email with a link redirecting me to a form to edit my password. 
            - When I enter a new password, my credentials are updated. 
            - **Result**: Pass          
        - **Invalid path**
            - When I leave the email field empty / input an invalid email address, I am prompted to enter valid data
            - When I enter an incorrect email address, a message is displayed informing me that the e-mail address is not assigned to any user account.
            - **Result**: Pass

- ## **Wishlist items and product review**

    - ### **As a site user, I want to save artworks in my wishlist so that I can buy it later or buy it again**
      - When I hover over the "heart" icon in the navigation, its appearance changes and, 
      - When I click on the icon and if I am logged-in, I am redirected to "My wishlist" page and,
      - A list of artwork added as my favourite is displayed with buttons to either add the artwork to cart or remove the the artwork from my saved items.
      - When I click on the button "Remove", the artwork is removed from my saved items and a message informing me that the item has been successfully removed is displayed. 
      - When I click on the button "Add to cart", the artwork is added to my shopping bag and a message informing me that the item has been successfully added to my shopping bag is displayed.
      - **Result**: Pass

    - ### **As a site user, I want to leave a review so that I can let others know about my shopping experience**
      - **Path 1 - artwork page**
        - When I browse an artwork page I have purchasd and commissioned and I haven't yet left a review, I can see a button "leave a review"
        - When I click on "leave a review", a page open with a form where I can enter a review in the "review" field, 
        - When I submit the review, I am redirected to artwork page and my review is displayed, 
        - Additional links will display under my review, so that I can edit / delete my reivew,
        - When I select edit, the review page with the form prefilled is displayed and I can edit my review, 
        - When I click submit, my review is updated and a notification informing me that my review has been successfully edited is displayed.
        - **Result**: Pass
      - **Path 2 - profile page**
        - When I am logged in and under my profile page, I can see my order details with a button "Review", 
        - When I click on "Review" a page open with a form to enter a review in the "review" field, 
        - When I click "Submit", the review is displayed under the artwork I purchased / commissioned and notification informing me that I have successfully left a review is displayed
        - **Result**: Pass
      - **Path 3 - edit reviews**
        - When I am on my profile page, I can see the tab reviews 
        - When I click on the tab revies, all the reviews I have created are displayed, 
        - When I click on edit, a page opens with my reviews details and I am able to edit my reviews,
        - When I click submit, my review is edited and a notification of my review has been successfully edited is displayed
        - **Result**: Pass

- ## **Contact and connect**

    - ### **As a site user, I want to contact the site owner so that I can make queries about his work / request for a commission**
    
      - #### **Navigation**
        - When I scroll down to the footer, I can see a the white button "contact",
        - When I hover over the contact button, its appearance changes and,
        - When I click on the contact button, I am redirected to a contact page which features a contact form.
        - **Result**: Pass ✅

        ![contact button changing appearance](screenshots/contact_button_change.png)

        ![contact page](screenshots/contact_page.png)

      - #### **Authenticated user**
        - When I am logged in, I can see that the contact form is prefilled with my details
        - **Result**: Pass ✅
      
      ![contact form prefilled](screenshots/contact_prefilled.png)

      - #### **Valid path**
        - When I enter all the valid information, including my full name, my email address and a query message, and
        - I click on submit,
        - The page refresh with a message informing me that my message has been sent successfully.
        - Once I have contacted the owner, I should receive an acknowlegment email.
        - **Result**: Pass ✅

        ![contact success](screenshots/contact_success.png)

      - #### **Invalid path**
        - If I leave or enter an invalid information in any of the fields, I will be prompted to fill or to enter valid information.
        - **Result**: Pass ✅

        ![contact page missing field](screenshots/contact_missing_field.png)

        ![contact page invalid field](screenshots/contact_invalid_format.png)
   
    - ### **As a site user, I want to follow the artist on social media so that I can keep up to date with his work**
      - When I scroll down to the footer, I can see three social media icons for Instagram, Facebook and Twitter,
      - When I hover over any of these icons, their appearance changes
      - When I click on any of these icons, I am redirected to the relevant social media platform in a new tab.
      - **Result**: Pass ✅

      ![footer with icon changing appearance](screenshots/footer_social_media.png)

- ## **Admin and site management** 
    - ### **As the site owner, I want to add, edit and delete a collection so that I can keep my portfolio and work up-to-date**
      - When I successfully log-in as the site owner, I can see a menu item entitled "Add Collection" in the top navigation bar under the user icon
      - When I click on the menu item "Add Collection", a page opens with a form to add collection details 
      - When I fill all the information correctly, the collection is successfully created and a notification informing of the successful creation of a collection is displayed.
      - Wen I fill information incorrectly / do not complete all the compulsory fields in the form, an error message will display prompting me to correct my entries before submitting the form again
      - **Result**: Pass
    - ### **As the site owner, I want to add, edit and delete individual artwork and items to that I can link them to collection and keep my shop up-to-date**
      - When I successfully log-in as the site owner, I can see a menu item entitled "Add Artwork" in the top navigation bar under the user icon
      - When I click on the menu item "Add Artwork", a page opens with a form to add artwork details 
      - When I fill all the information correctly, the collection is successfully created and a notification informing me that the artwork has been successfully created is displayed.
      - Wen I fill information incorrectly / do not complete all the compulsory fields in the form, an error message will display prompting me to correct my entries before submitting the form again
      - **Result**: Pass      
    - ### **As a site owner I want to add related product so that I can encourage multi-buy**
      - When I complete the form in "Add an Artwork" page, I can see an option to select related artwork from existing entries on the database.
      - When I select related artwork and submit the form, I can see under the artwork detail page related artwork displayed with a thumbnail, a title and price. 
      - **Result**: Pass
