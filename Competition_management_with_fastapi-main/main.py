#To excute your code, run this main file

import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    uvicorn.run("app.app:app", host= HOST , port= int(PORT) , reload= True)


    
