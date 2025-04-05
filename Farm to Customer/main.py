from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

# Create the FastAPI app instance
app = FastAPI()

# Mount static files (CSS, JS, Images)
# This tells FastAPI to serve files from the current directory
# and the 'images' directory when requested with paths like /style.css or /images/logo.png
# Serve files from the root directory under /static path
app.mount("/static", StaticFiles(directory="."), name="static_root")
# Serve files specifically from the images directory under /images path
app.mount("/images", StaticFiles(directory="images"), name="images")


@app.get("/")
async def read_root():
    """
    Serves the main index.html file when the root URL (/) is accessed.
    """
    html_file_path = os.path.join(os.path.dirname(__file__), "index.html")
    if os.path.exists(html_file_path):
        return FileResponse(html_file_path)
    else:
        # Fallback if index.html is missing
        return {"error": "index.html not found"}

@app.get("/login/customer", tags=["Pages"])
async def get_customer_login_page():
    """Serves the customer login HTML page."""
    login_file_path = os.path.join(os.path.dirname(__file__), "login_customer.html")
    if os.path.exists(login_file_path):
        return FileResponse(login_file_path)
    else:
        return {"error": "Customer login page not found"}

@app.get("/login/farmer", tags=["Pages"])
async def get_farmer_login_page():
    """Serves the farmer login HTML page."""
    login_file_path = os.path.join(os.path.dirname(__file__), "login_farmer.html")
    if os.path.exists(login_file_path):
        return FileResponse(login_file_path)
    else:
        return {"error": "Farmer login page not found"}

# --- Static file serving (Explicit routes as fallback, might not be needed with correct StaticFiles mount) ---
@app.get("/static/style.css", include_in_schema=False) # Ensure path matches HTML link
async def get_css():
    css_file_path = os.path.join(os.path.dirname(__file__), "style.css")
    if os.path.exists(css_file_path):
        return FileResponse(css_file_path, media_type="text/css")
    else:
        # Fallback if style.css is missing
        return {"error": "style.css not found"}

@app.get("/static/script.js", include_in_schema=False) # Ensure path matches HTML link
async def get_js():
    js_file_path = os.path.join(os.path.dirname(__file__), "script.js")
    if os.path.exists(js_file_path):
        return FileResponse(js_file_path, media_type="application/javascript")
    else:
        # Fallback if script.js is missing
        return {"error": "script.js not found"}


# --- How to Run ---
# You can run this app from your terminal using Uvicorn:
# uvicorn main:app --reload
#
# --reload makes the server restart automatically when you save changes to the code.
# Open your browser to http://127.0.0.1:8000

if __name__ == "__main__":
    # This block allows running the script directly with `python main.py`
    # Uvicorn is recommended for development and production, but this is useful for simple testing.
    print("Running FastAPI server directly (use 'uvicorn main:app --reload' for development)")
    uvicorn.run(app, host="127.0.0.1", port=8000)
