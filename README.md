# **Which Way is Up**

## **INTRODUCTION** 

[include screenshots of project on responsive devices]

Which Way Is Up -  an online gallery and ecommerce website for artist Peter Charalambides - was created for educational purposes only as part of the Code Institute’s full stack development course.

Using the principles of UX design, this fully responsive and interactive website was developed using HTML, CSS, JavaScript and Python as well as Django as a framework.

View live project here [link to deployed link]

## **TABLE OF CONTENT** 

  - [UX Design](#ux-design)
    - [Strategy](#Strategy)
    - [User stories](#User-stories)
    - [Scope](#Scope)
    - [Structure](#Structure)
    - [Skeleton](#Skeleton)
    - [Design](#Design)
  - [Features](#features)
    - [Existing features](#existing-features)
    - [Features left to implement](#features-left-to-implement)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Databases platform and cloud storage](#database-platform-and-cloud-storage)
    - [Libraries and frameworks](#libraries-and-frameworks)
    - [Other technologies](#other-technologies)  
  - [Testing](#testing)
    - [Introduction](#introduction)
    - [Code validation](#code-validation)
    - [Testing User stories](#testing-User-stories)
    - [Automated testing](#automated-testing)
    - [Responsiveness and compatibility](#responsiveness-and-compatibility)
    - [Testing performance](#testing-performance)
    - [Testing accessibility](#testing-accessibility)
    - [Interesting issues and known bugs](#interesting-issues-and-known-bugs)
  - [Deployment](#deployment)
    - [Deployment of the page](#deployment-of-the-page)
    - [How to run the code locally](#how-to-run-the-code-locally)
   - [Credits](#credits)
     - [Code](#code)
     - [Content](#content)
     - [Media](#media)
     - [Acknowledgment](#acknowledgments)

## **UX DESIGN**

 - ### **Strategy**  

   Peter Charalambides is a London based artist operating under the umbrella Which Way Is Up and whose style sits within the urban art movement.
   
   Whilst Peter Charalambides’ breadth of work is versatile, he specialises in doodle art illustration on a wide range of mediums including furniture.  
   
   With over 1300 followers on instagram, Peter would like to revamp his website to showcase his portfolio and include an ecommerce shop where he can sell his art directly to the public.  
   
   Peter Charalambides offers original artwork as well as prints of his illustration, with a wide range of pricing, making his art accessible and affordable to all.
   
   - #### **Site owner goal**
     - To increase online presence 
     - To drive and connect with audience through the website
     - To tell artist story and profile by showcasing portfolio
     - Convert interest into sales 
   - #### **User goals** 
     - To access a user-friendly website across multiple devices 
     - To discover artist work and collections 
     - To buy prints and unique piece of arts
     - To contact and connect with the artist

 - ### **User stories** 

    1. **Navigation and website experience**
        - As a site user, I want a responsive website so that I can access it on different devices.
        - As a site user, I want to easily navigate across the site so that I can find the information I need.
        - As a site user, I want to read about the artist so that I can learn about artist background and exhibitions
        - As a site user, I want to view the artist work so that can understand the artist work
        - As a site user, I want to see the details for an artwork so that I can get a better appreciation and decide if I would want to buy it.
        - As site user, I want to engage with the artist work so that I can be part of the artist community

    2. **Shopping experience** 
        - As a shopper, I want to view all the artwork available so that I can quickly have an overview of what is on offer
        - As a shopper, I want to view available artwork by specific collection and category so that I can quickly find products I’m interested in.
        - As a shopper, I want to sort the list of artwork available so that I can find a piece in my price range
        - As a shopper, I want to view the artwork price and details so that I can make an informed decision
        - As a shopper, I want to read reviews so that I can have a better understanding of the quality of the artist work
        - As a shopper, I want to view related items so that I can purchase several artwork
        - As a shopper, I want to select quantity of an item if applicable so I can order what I need

    3. **Shopping bag and checkout**
        - As a shopper, I want to review items in my shopping bag so that I can adjust quantities ordered.
        - As a shopper, I want to have a gift option so I can buy a print / piece of art for a special occasion for a friend
        - As a shopper, I want to enter payment information in a safe and secure way so that I can checkout quickly with confidence
        - As a shopper, I want to receive confirmation of my order so that I can have a proof of purchase

    4. **Registration and account management** 
        - As a site user, I want to register for an account so that I can view my orders and my favourite items
        - As a site user, I want to login and logout so that I can access my profile safely 
        - As a site user, I want to edit my profile so that I can update my personal information
        - As a site user, I want to reset my password if I forgot it so that I can access my account
        - As a site user, I want to delete my profile so that my personal information are removed from the website

    5. **Favourite items and product review**
        - As a site user, I want to save artwork as my favourites so that I can buy it later or buy it again
        - As a site user, I want to leave a review so that I can let others know about my shopping experience

    6. **Contact and connect**
        - As a site user, I want to contact the site owner so that I can make queries about his work / request for a commission
        - As a site user, I want to follow the artist on social media so that I can keep up to date with his work

    7. **Admin and site management** 

        - As the site owner, I want to add, edit and delete a collection so that I can keep my portfolio and work up-to-date
        - As the site owner, I want to add, edit and delete individual artwork and items to that I can link them to collection and keep my shop up-to-date
        - As a site owner I want to add related product so that I can encourage multi-buy
        - As a site owner, I want to be able to edit most of the content of the website, so that I can keep my website up to date and engaging.
        - As a site owner, I want to manage orders from the console so I can know I have dispatched the order.

  - ### **Scope**
  
     - #### **Feature trade-off**

        ![Attachments_feature trade off](documentation/scope/Feature_trade_off.png)

        A pdf version of the feature trade-off can been see [here](documentation/scope/Feature_trade_off.pdf)

        This website will be developed as a minimal viable product with room for future improvements and releases incorporating additional features.

     - #### **Functional requirements**
        - To be able to sign-up using email address and secure password
        - To be able to login and logout
        - To be able to add/view/edit/delete profile information
        - To be able to reset password 
        - To be able to add/view/edit/delete an collection
        - To be able to add/view/edit/delete a artwork
        - To be able to add/view/edit/delete reviews
        - To be able to create/view/edit/delete shopping bag
        - To be able to process orders
        - To be able to process paiement
        - To be able to sort shop items according to a set of criteria 
        - To be able to email notification to users
        - To be able to store and retrieve images 
        - To be able to contact the site owner 
        - To receive feedback for important actions: create - update - delete
        - To handle errors: page 404 not found, page 500 Internal Server Error page and page 403/403 

	 - #### **Non functional requirements**
	
       - Display artwork images and information in engaging way
       - Intuitive navigation and structure

     - #### **Content requirements**
       - Artist biography and key events/exhibitions
       - Information about the artist work 
       - Image library of artwork
       - Details for the artwork - size, price
       - Forms where user input is required
       - Engaging text and headings throughout to introduce main sections of the website
       - Icons for interactive and visual elements 

     - #### **Constraints**
	
       - Technical skills: The site owner is still learning Python and is new to Django Framework which may impact on the successful implementation of the planned features. 
       - Time: Implementing features using new technical skills will require time and careful planning, especially since the developer is now working full-time.

 - ### **Structure**

     - #### **Organisation of functionality and content**

        - Header: Logo and a collapsible menu with navigational links
        - Homepage: Give an overview of the artist universe including Hero image, featured collection, downloadable colouring page and reviews
        - About: Information about the artist
        - Work: Display artist portfolio and image library
        - Shop: Display artwork, prints and other items for sale
        - Product page: Display artwork details
        - Shopping bag: Display items added in the bag
        - Footer: Contact form, links to social media and policies

     - #### **Interaction design**

        - Collapsible menu
        - Artwork image with hovering effect
        - Buttons and icons with hovering effect

     - #### **Database structure**

        The diagram below illustrates the database structure used in this project, first managed using SQLite during the development process, then Postgres in production with Heroku. A pdf version can be seen [here](documentation/structure/db_structure.pdf).

        ![Attach db structure](documentation/structure/db_structure.png)

 - ### **Skeleton**
    
    - ### **Wireframes**

       ![homepage wireframes](documentation/wireframes/homepage.png)

       Please find all the wireframes in pdf format [here](documentation/wireframes/wireframes.pdf). 
    
       Please find below links to a selection of wireframe for this project (png format)
         - [Homepage menu](documentation/wireframes/homepage_menu.png)
         - [Work](documentation/wireframes/work.png) 
         - [Collection details](documentation/wireframes/collection_details.png)
         - [About page](documentation/wireframes/about.png)
         - [Shop](documentation/wireframes/shop.png)
         - [Artwork details](documentation/wireframes/artwork_details.png)
         - [Shopping bag](documentation/wireframes/shopping_bag.png)
         - [Checkout page](documentation/wireframes/checkout_page.png)
         - [Order successful](documentation/wireframes/order_successful.png)
         - [Saved items](documentation/wireframes/saved_items.png)
         - [Sign up page](documentation/wireframes/signup.png)
         - [Login page](documentation/wireframes/login.png)
         - [Profile page](documentation/wireframes/profile.png)
         - [Add artwork](documentation/wireframes/add_artwork.png)
         - [Add collection](documentation/wireframes/add_collection.png)
         - [Contact us page](documentation/wireframes/contact.png)
         - [Error page](documentation/wireframes/error_pages.png)
         - [Policy page](documentation/wireframes/policy_pages.png)

    - #### **Difference to design**

    - #### **Limitations** 

 - ### **Surface / Design** 

     The website will feature a simple, modern and engaging design, with a minimum of colours to keep the emphasis on the artist's work.

    - #### **Imagery**

       The website will solely feature images from the artist's artwork. 

    - #### **Colour scheme**
 
       Since the artwork is either black and white or very color full, the website will use mostly black and white with an additional colour for interactive purposes (such as hovering effect) and feedback to site visitors / shoppers. 

       The website will use the following colour palette, which was custom-made and checked for accessibility using Adobe Color

     - #### **Typography**
        The website will use the following fonts from Google:

     - #### **Icons**
       Icons by font-awesome will be used in the navigation bar to allow users to quickly access functionalities offered by the website such as the shopping cart / 

     - #### **Styling**
        - Horizontal lines to structure and make the content of the website easy to read.
        - Slightly rounded edge borders and buttons for a more user friendly and inviting interface.

     - #### **Difference to design** 

## **FEATURES**

  - ### **Existing features**
  - ### **Features left to implement**

## **TECHNOLOGIES USED**

  - ### **Languages**
  - ### **Databases platform and cloud storage**
  - ### **Libraries and frameworks**
  - ### **Other technologies**

## **TESTING**

  - ### **Introduction**
  - ### **Code validation**
  - ### **Testing User stories**
  - ### **Automated testing**
  - ### **Responsiveness and compatibility**
  - ### **Testing performance**
  - ###  **Testing accessibility**
  - ### **Interesting issues and known bugs**
    - #### **Known bugs**
 
## **DEPLOYMENT**

## **CREDITS**

  - ### **Code**
  - ### **Media and content**
  - ### **Additional Content**
  - ### **Acknowledgments**


