# Social Networking Images
### About
<p>
This API allows users to POST/DOWNLOAD/DELETE images on social networking sites like Twitter, Facebook & Instagram.
</p>

### How to use this?
There are two ways to use this API
1. Direct API Call
2. Client (API is wrapped)

### Working Principle with granular level control
1. API uses `env.yml` to fetch the keys and settings of every social networking
2. You can completely disable a social networking site i.e. block all (POST/DELETE/DOWNLOAD) reqeusts and at the same time allow one or two (POST/DELETE/DOWNLOAD) requests and block other requests for a site.
3. Tokens and secret keys are encrypted and will be decrypted only at the time of connecting with the networking site
4. Has created separate `handlers` folder which is a collection of endpoints to host them separately when moving to cloud
5. Single Objective functions to easily convert them to Step Functions

### Start this API
Navigate to `orchestration` folder and hit

> docker-compose up -d

Above command will start two containers, One container will host the API and the other will have client created.

### Client
1. Open client using below command
> docker container exec -it kon_client bash

2. Run client
> python client.py

3. Choose Operation(POST/DELETE/DOWNLOAD)
- POST - Will have to mention the name of the file to be POSTED
- DELETE - Latest image will be deleted from all the social networking sites
- DOWNLOAD - Latest image will be downloaded from all the social networking sites in **zip** format

### Sample Execution with Response
> root@host_client:/subscribili/fp-client# python client.py <br>
> Would like to Post/Download/Delete Image: post <br>
> Enter filename with path: upload.PNG <br>
```json
[{"facebook":"Disabled"},{"instagram":"[Mocked] Posted Image.","op_mode":"mock","status_code":200},{"op_mode":"original","status_code":200,"twitter":{"info":{"twitter":1455231231063310337},"msg":"Posted Image."}}]
```
