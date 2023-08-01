# Challenge Connect

## About

ChallengeConnect is a versatile solution that serves as a consumable API to streamline building a hackathon hosting  application. With ChallengeConnect, organizers can effortlessly create and manage hackathons, specifying details like title, dates, and rewards. Participants can easily enroll in hackathons, submit their innovative solutions, and view a feed of available hackathons. The API ensures secure user registration and authentication, allowing only authorized individuals to create hackathons. It offers a seamless experience for both organizers and participants, fostering a thriving community of tech enthusiasts and problem solvers.

## Local Setup               

1. Install Python (3.6 or higher)
2. Create a virtual environment using your choice of tool.
E.g. `python -m venv your_venv_name`
3. Clone this repository: `https://github.com/sourav-nanda/challenge-connect.git`.
4. Navigate to the project directory:
`cd challenge-connect-master`.
5. Install the required dependencies: `pip install -r requirements.txt`.


## Usage

1. Run the development server: `python manage.py runserver` or `source run.sh`.
2. Access the API at `http://localhost:8000/`.
3. Check examples to know how to access the endpoints.

```Note cloud endpoints will be added after deployment.```



  ## Consuming as a REST API

Use tools like `curl`, `Postman`, or programming libraries (e.g., `requests` in Python) to make HTTP requests to the API endpoints.


## API Overview

The API allows users to create, enroll in, and submit entries for hackathons. It is built using Django and Django Rest Framework.

### Models

- **Hackathon**: Represents a hackathon and has fields like title, description, background image, hackathon image, type of submission, start datetime, end datetime, and reward prize.
- **Submission**: Represents a user's submission for a hackathon and includes fields like name, summary, submission file, user, and hackathon.


### API Structure

The API follows the RESTful architecture and includes endpoints for creating and viewing hackathons, submitting entries, and enrolling users in hackathons.

### URL Mappings

- `/hackathons/`: GET - View list of all hackathons (hackathon_feed).
- `/hackathons/create/`: POST - Create a new hackathon (hackathon_create).
- `/hackathons/enroll/<int:hackathon_id>/`: POST - Enroll in a hackathon (hackathon_enroll).
- `/hackathons/enrolled/`: GET - View list of enrolled hackathons (hackathon_enrolled).
- `/submissions/create/<int:hackathon_id>/`: POST - Submit an entry for a hackathon (submission_create).
- `/submissions/user/<int:user_id>/`: GET - View list of user submissions (submission_user).
- `/unauthorized/`: GET - Display unauthorized access message (unauthorized).

