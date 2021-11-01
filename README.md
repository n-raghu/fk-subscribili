# Social Networking Images
### About
<p>
This API allows users to POST/DOWNLOAD/DELETE images on social networking sites like Twitter, Facebook & Instagram.
</p>

### How to use this?
There are two ways to use this API
1. Direct API Call
2. Client (API is wrapped)

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
> POST - Will have to mention the name of the file to be POSTED.
> DELETE - Latest image will be deleted from all the social networking sites
> DOWNLOAD - Latest image will be downloaded from all the social networking sites in **zip** format

