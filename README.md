# Guess Human Age API

Guess Human Age API is a Django-based API that estimates the age of a person based on their name. It utilizes the Agify API for age estimation.

## Overview

The API provides an endpoint `/api/human-age` that accepts a POST request with a JSON payload containing the name, and it returns the estimated age along with the computed date of birth.

## Installation

### Using Docker Compose

1. Clone the repository:

    ```bash
    git clone https://github.com/Adeakim/guess_human_age.git
    cd guess_human_age
    ```

2. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

3. Access the API at [http://127.0.0.1:8000/api/human-age](http://127.0.0.1:8000/api/human-age) in your browser or using a tool like [curl](https://curl.se/) or [Postman](https://www.postman.com/).

## Usage

### Endpoint: `/api/human-age`

- **Method**: POST
- **Request Payload**:
  ```json
  {
    "name": "michael"
  }

- **Response**:
{
  "name": "michael",
  "age": 63,
  "date_of_birth": 1961

}
- **To run tests**:
  ```docker-compose run web python manage.py test```
  

