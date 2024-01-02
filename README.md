# API Project
This is my project for API development. The theme is about books. There are authors, books, pen names. In total there are 10 endpoints: 4 get's, 4 Post's & 2 Delete's. I have done all the minimum requirements (number 1.) and I have done a few front-end requiremnts (numbers 3.1, 3.1.1, 3.1.2).

## Frontend

The frontend of this project is hosted on GitHub Pages. You can access it [here](https://api-development-eind-frontend.netlify.app/).

## Okteto Development Environment

I utilized Okteto for development. The API documentation is available at [Okteto - API Documentation]([https://api-development-eind-frontend.netlify.app/](https://useritem-api-service-eindproject-baisangur-dudayev.cloud.okteto.net/docs#/)).

#DEPLOYMENT
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/92d38986-2e21-4c05-bab3-32817a5e615d)



##Authentication

I implemented Oath and hashing. U must authenticate before u can interact with the delete endpoints.

![image](https://github.com/Baisangur-Dudayev/API-development-basis-project/assets/113896223/8a5b6a27-75ad-4fe3-a387-d0d0096b3be3)


![image](https://github.com/Baisangur-Dudayev/API-development-basis-project/assets/113896223/954fb833-ebb8-4920-b95e-3abb69159ed5)



## ENDPOINTS with api documentation
my endpoints:
![image](![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/e9075a19-db2a-49b0-a5f3-a3bfc1efd36c)
)


GET /authors/

![image](https://github.com/Baisangur-Dudayev/API-development-basis-project/assets/113896223/4941a18a-8ecc-4306-9fa3-580977dc3b9e)


POST /authors/ 

![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/6cf74835-4f7d-49f7-a31f-f37ffbc98299)

)


GET /authors/{author_id}

![image](https://github.com/Baisangur-Dudayev/API-development-basis-project/assets/113896223/5a7b53a2-19ff-4f4b-b661-a1959bb568ff)


POST /authors/{author_id}/books/
![image](https://github.com/Baisangur-Dudayev/API-development-basis-project/assets/113896223/e6885394-f264-465b-bc0b-b44ee1ca069d)

POST /authors/{author_id}/pen_names/
![image](https://github.com/Baisangur-Dudayev/API-development-basis-project/assets/113896223/8fc25a7d-6445-4f1d-9f49-b49b2bf6ae40)

GET /books/
![image](https://github.com/Baisangur-Dudayev/API-development-basis-project/assets/113896223/7f7d602c-7338-483a-9d71-33246effd8c2)


DELETE
/pen_names/{pen_name_id}
![image](https://github.com/Baisangur-Dudayev/API-development-basis-project/assets/113896223/6f776df7-f158-47bf-8a3f-ab4484bf1cf8)


DELETE /books/{book_id}
![image](https://github.com/Baisangur-Dudayev/API-development-basis-project/assets/113896223/3f529b91-b976-4d26-91fb-3123e2dee482)


##FRONTEND
This is my frontend I have a get point to retrieve all authors. You also need to authenticate yourself and log in before you can use the endpoint.
Unfortunatly I didn't have enough time to add the other endpoints.
![image](https://github.com/Baisangur-Dudayev/API-development-basis-project/assets/113896223/d7ee31f4-ac94-4bb6-bd59-214daa999360)
![image](https://github.com/Baisangur-Dudayev/API-development-basis-project/assets/113896223/fd189840-3030-4d3f-9667-568125fd6d47)
![image](https://github.com/Baisangur-Dudayev/API-development-basis-project/assets/113896223/7a07c0e4-7770-47f1-aca7-3ba8c3a4e545)

