# Screened-Movie-Blog

This a blog for movie reviews.

## URLS

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

```

## CODE SNIPPET FOR DROP ANIMATION

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
```
