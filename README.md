# API Project
This is my project for API development. The theme is about books. There are authors, books, pen names. In total there are 11 endpoints: 4 get's, 4 Post's, 2 Delete's and 1 Put. I have done all the minimum requirements (number 1.) and I have done a few front-end requiremnts (numbers 3.1, 3.1.1, 3.1.2). 

## Frontend

The frontend of this project is hosted on GitHub Pages. You can access it [here](https://api-development-eind-frontend.netlify.app/).

## Okteto Development Environment

I utilized Okteto for development. The API documentation is available at [Okteto - API Documentation](https://useritem-api-service-eindproject-baisangur-dudayev.cloud.okteto.net/docs#/).

#DEPLOYMENT
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/92d38986-2e21-4c05-bab3-32817a5e615d)



## Authentication

I implemented Oath and hashing. U must authenticate before u can interact with the delete endpoints. In the endpoint section of the readme u can also see that i can only interact with a delete endpoint if im logged in. 
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/896e5dcd-a09f-47cf-8c7f-e95c075bbb57)

![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/1aa05dd0-4212-4e49-9d4a-1244343bfa8e)




## ENDPOINTS with api documentation
my endpoints:
(![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/e9075a19-db2a-49b0-a5f3-a3bfc1efd36c)
)


GET /authors/
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/1d2270ba-5a25-40aa-b78c-eff944a10c3a)




POST /authors/ 

![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/b932f7ab-f827-4471-869c-98367f2f1ac2)


)


GET /authors/{author_id}
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/d0b153a4-ffba-4d48-afe7-da763125040f)


PUT /authors/{author_id}
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/0f3e33ba-3e2b-44be-a1e3-fc8d3537bd54)

POST /authors/{author_id}/books/
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/272b11c1-29f2-4f11-963e-7030f5c0f8e7)


POST /authors/{author_id}/pen_names/
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/08ce0437-921f-44ac-b828-e55a264c0d6e)


GET /books/
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/66e5cef9-69bf-46b4-9a77-964c41340a3c)



DELETE
/pen_names/{pen_name_id}
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/fb41294a-a618-48f8-97df-e1c99d0fac33)


DELETE /books/{book_id}
before logging in
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/c579efb4-1d32-4509-8c66-72f1c007c8f0)
after logging in
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/2afb6ab5-b189-47c4-9b08-118aa00c827e)

## FRONTEND
The frontend has been styled with css and contains all my GET & POST endpoints. It is also hosted on netlify. The blue information is the response data the I show to the user. U can scroll trough the data of each div. This way if there is a lot of information it won't get in the way and it keeps everything organized. 
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/70d51c56-f2ed-456d-8967-f74abad819fb)
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/283b4961-b7b1-47a2-b7ea-384a1099f5f7)
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/3509f3bd-4cce-4bdc-b9bf-fdd6f474f784)


