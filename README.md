## Basic Vue/FastAPI/Postgres template app
This is intended as a small, easy to work with template for use as a jumping off point.


## Usage

#### database
Run the docker-compose to create a local dev db
`cd backend`
`docker-compose up -d`
You can login to the container
`docker exec -it backend_db_1 bash`
`psql -U test -d vue-app-db`
view tables:
`\dt`

#### Backend
Run the backend
`cd backend`
`pip install -r requirements.txt`
`uvicorn src.main:app --reload`

#### Frontend
`cd frontend`
`npm run dev`
