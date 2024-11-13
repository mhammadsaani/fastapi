from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from psycopg2 import sql
from config import SCHEMA, TABLE
from utils import create_db_connection, mimic_model


app = FastAPI()

def process_model(file):
    conn = create_db_connection()
    fetch_url_query = sql.SQL("SELECT url FROM {}.{} WHERE id = %s").format(
        sql.Identifier(SCHEMA),
        sql.Identifier(TABLE)
    )
    url = ""
    model_result = mimic_model()
    print("Random Number :", model_result)
    with conn.cursor() as cursor:
        cursor.execute(fetch_url_query, (model_result,))
        result = cursor.fetchone()
        
        if result:
            url = result[0]
            print(f"URL fetched successfully: {url}")
        else:
            print(f"No record found with id = {model_result}.")
        
    return url

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    image_url = process_model(file)
    return JSONResponse(content={"message": f"Image URL: {image_url}"})
