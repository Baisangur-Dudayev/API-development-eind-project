# API Project
This is my project for API development. The theme is about books. There are authors, books, pen names. In total there are 11 endpoints: 4 get's, 4 Post's, 2 Delete's and 1 Put. I have done all the minimum requirements (number 1.) and I have done a few front-end requiremnts (numbers 3.1, 3.1.1, 3.1.2). 

## Frontend

The frontend of this project is hosted on Netlify. You can access it [here](https://api-development-eind-frontend.netlify.app/).

## Okteto Development Environment

I utilized Okteto for development. The API documentation is available at [Okteto - API Documentation](https://useritem-api-service-eindproject-baisangur-dudayev.cloud.okteto.net/docs#/).

#DEPLOYMENT
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/92d38986-2e21-4c05-bab3-32817a5e615d)



## Authentication
u must authenticate first to use most endpoints There is already a user with email: "test@hotmail.com" & password: "password"

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

## Endpoints with postman

GET /authors/
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/6dfa8904-b99a-4626-bf78-64096a4a1a14)



POST /authors/ 
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/4f405515-0c2e-4487-b342-bac365037ae8)



GET /authors/{author_id}
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/11d12d76-f520-48e1-9c55-e52a15c6af37)

POST /authors/{author_id}/books/
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/75e2c370-75d2-418f-9f59-067f3d498b90)


POST /authors/{author_id}/pen_names/
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/5537c408-6aa6-45c3-b4dd-7449076326ad)



GET /books/
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/a726b4dd-0ddc-4eae-8dc0-88f0315248b5)


I can connect to the PUT endpoint and the DELETE endpoints, but I didn't know which setting to change in Postman for the PUT
endpoint to send the data. I also didn't know which setting to change in Postman to authenticate myself for DELETE
endpoints. This is not because the endpoints don't work, but because I used to work with /docs in my browser
and that's why I'm not familiar with Postman
PUT /authors/{author_id}
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/3d867c47-0eee-43b1-8105-692da03a06c4)
DELETE /pen_names/{pen_name_id}
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/69904f19-f84a-40db-bdb0-6333d0fd1ee7)
DELETE /books/{book_id}
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/9b6e9fb8-f9dc-4120-99a4-c69174baf691)


## FRONTEND
The frontend has been styled with css and contains all my GET & POST endpoints. It is also hosted on netlify. The blue information is the response data the I show to the user. U can scroll trough the data of each div. This way if there is a lot of information it won't get in the way and it keeps everything organized. 
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/70d51c56-f2ed-456d-8967-f74abad819fb)
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/283b4961-b7b1-47a2-b7ea-384a1099f5f7)
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/3509f3bd-4cce-4bdc-b9bf-fdd6f474f784)

## PYTEST
![image](https://github.com/Baisangur-Dudayev/API-development-eind-project/assets/113896223/007e82f1-fd88-431b-872f-2f2863b79d1f)

