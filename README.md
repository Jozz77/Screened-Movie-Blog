# Screened - A Multi-Author Movie Blog

Screened is a community for creative and interesting minds. It’s home to several thought-provoking pieces and intriging conversations about movies on our screens.


## Table of Content

- [General Information](#General-Information)

- [Live Site](#Live-Site)

- [Technologies Used](#Technologies-Used)

- [Architecture](#Architecture)

- [Prerequisites](#Prerequisites)

- [Features](#Features)

- [How to Use Screened](#How-to-Use-PriceZilla)

- [Contributors](#Contributors)

- [Acknowledgements](#Acknowledgements)

- [Author](#Author)



## General Information

Screened is the premiere online destination for movie enthusiasts, providing the latest news and information on casting and development, release dates, interviews and all movies rated gist. Screened keeps users connected to all their favorites, past, present and future movies/tv series. Our sole aim is to become one of the best review websites on the internet where you discover, watch and discuss the movies you love.


## Live Site

[Screened Blog Website](http://screened.herokuapp.com/)


## Technologies Used

- ### Product Designers

Tool: 

Figma for UI designs. FigJam for UX designs.


- ### Frontend Developers

Languages: 
HTML, CSS, JAVASCRIPT. 

These languages were used to structure, style, and let users interact with the UI of the platform.


- ### Backend Developers

Language: Python

Framework: Django



## Architecture

The entire project is built on Django, a high-level python web framework for rapid development and clean design. 


## Prerequisites

- You will need the following technologies installed to get the service running:

- A compatible broswer

- An IDE

- Python app

- GIT

## Installation Guide
- Clone the repo
- Open command prompt and type git clone https://github.com/zuri-training/Price-Compare-Team-22.git

- Open the folder you just cloned using your IDE and open the terminal window.
 
## Running locally for the first time

1. install python
   download from the official python [download](https://www.python.org/downloads/) page

- install virtualenv `pip install virtualenv`
- install django `pip install django`

2. clone the repository and move into the repository

   ```bash

   git clone https://github.com/Jozz77/Screened-Movie-Blog.git

   ```

3. create the virtual environment if you haven't created it

   ```bash

    python -m venv env

   ```

4. activating the virtual environment

   windows:
   `.\env\Scripts\activate`

   macOs:
   `source env/bin/activate`

5. install the requirements

   ```bash

   pip install -r requirements.txt

   ```

6. run

   ```bash

    python manage.py runserver

   ```

## Running after the first time

1. activate the environment

windows:
`.\env\Scripts\activate`

macOs:
`source env/bin/activate`

2.  run the server

```bash

python manage.py runserver

```
 You're all set!



## Features

#### Unauthenticated Users

- Home Page
    Users can view basic information about the platform and watch a Youtube video trailer one on the categories.
    
 - Navigation Bar
    Users can navigate the site and move from one page accessible to them to another. Pages includes: About Page, 
    
 - Search
     Users can search for products by typing the ‌keyword in the search bar. However, they are limited to viewing products in a category.
    
  - Categories
      Users can view blog post across 5 categories which are Hollywood, Bollywood, Nollywood, K-drama and Tv-Series.
      
  - Call To Action (CTA)
       Users will be receive prompts to take certain initiative and become a registered member. These features include: A prompt to register and become authenticated.
       
   - Footer: Pages include: Contact Page, Write for Us, Terms and Conditions, Privacy and Credits Page which is the Team's page.


## How to Use PriceZilla

- Use the search area to find your desired products.

- Click on the categories dropdown and choose which category posts you want to see.

- Click on the posts you want to view.

- Click on Comment on the blog post to add your comments.

### How to create a Blog Post on the website

- Visit the platform using the live link

- Browse through various Categories and posts.

- Go to the Write For Us page and click on Start Here to sign up and log in.

- Go the Write new blog and fill in your details and click on Submit Button.

- You are done!!!




#### Authenticated Users

- Navigation Bar
  Users who did not save login information will have to sign in using the email and password method.
  
  - Blog Posts
     Users can post contents, edit posts, delete add images to their posts across 5 categories
     

## Acknowledgements

Many thanks to the [Just-Projects ](https://twitter.com/thejustprojects) for the training and inspiring this project.


## Author

Jonathan Mmadu

- GitHub - [Jozz77](https://github.com/Jozz77)





<!-- ## URLS

- login page: localhost/user/login
- signup page: localhost/user/signup
- reset password page: localhost/user/password_reset/
- password reset confirmation page i.e. The reset link has been sent to your email: localhost/user/password_reset_confirm/
- password reset complete: localhost/user/password_reset_complete/

## Table of Contents

- [Running](#running-locally)

## Running locally for the first time

1. install python
   download from the official python [download](https://www.python.org/downloads/) page

- install virtualenv `pip install virtualenv`
- install django `pip install django`

2. clone the repository and move into the repository

   ```bash

   git clone https://github.com/Jozz77/Screened-Movie-Blog.git

   ```

3. create the virtual environment if you haven't created it

   ```bash

    python -m venv env

   ```

4. activating the virtual environment

   windows:
   `.\env\Scripts\activate`

   macOs:
   `source env/bin/activate`

5. install the requirements

   ```bash

   pip install -r requirements.txt

   ```

6. run

   ```bash

    python manage.py runserver

   ```

## Running after the first time

1. activate the environment

windows:
`.\env\Scripts\activate`

macOs:
`source env/bin/activate`

2.  run the server

```bash

python manage.py runserver

``` -->

<!-- ## CODE SNIPPET FOR DROP ANIMATION

1. html code(note that you can change the name of the classes if need be)
   (note that the img src will have to be altered to fit the actual path of the image)

```html
<div class="container">
  <div class="line">
    <img src="./Line 3.png" alt="" />
  </div>
  <div class="title">
    <h2>About</h2>
  </div>
</div>

<div class="container-2">
  <div class="line">
    <img src="./Line 3.png" alt="" />
  </div>
  <div class="title">
    <h2>Us</h2>
  </div>
</div>
```

2. css code (Make sure that whatever is housing the containers is positioned relatively i.e the header)
   (style the h2 elements as deemed fit)

```css
.container {
  position: absolute;
  top: 0;
  left: 40%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  animation: moveDown 2s ease-in;
  margin-right: 200px;
}
.container-2 {
  position: absolute;
  top: -100px;
  left: 60%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  animation: moveDown 2s ease-in;
  animation-delay: 0.5s;
  animation-fill-mode: backwards;
}

@keyframes moveDown {
  0% {
    opacity: 0;
    transform: translateY(-1000px);
  }

  40% {
    transform: translateY(50px);
  }
  60% {
    transform: translateY(-20px);
  }

  100% {
    opacity: 1;
    transform: translateY(0px);
  }
}
``` -->
