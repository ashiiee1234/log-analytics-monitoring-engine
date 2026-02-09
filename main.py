# from config.dask_config import start_dask
# from ingestion.loader import load_logs
# from ingestion.parser import parse_log_line
# from processing.pipeline import build_pipeline
# import time
# import dask.dataframe as df
# from anomaly.detecter import detect_anomaly
# from config.email_config import send_mail
from fastapi import FastAPI
from backend.router import service
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins=[     #Need to add origin so that frontend can send method to backend.
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, ## Allow connection to database.
    allow_methods=["*"], ##allow all methods like POST,GET,PUT,DELETD,etc.
    allow_headers=["*"],
)


]

app.include_router(service.router)
# if __name__ == "__main__":
#     main()


