# Penn Club Review - Backend Challenge

## Overview
Penn Club Review is a backend system designed for students to explore clubs and student organizations at the University of Pennsylvania. This system provides a structured database to store club details and a REST API to interact with the data. Users can search for clubs, view club details, edit clubs details, add clubs, access club tags, and mark their favorite clubs. The project is built using Flask, SQLAlchemy, a REST API design, and database management.

## Installation and Setup

### Prerequisites
Ensure you have the following installed:
- Python
- `pipx` 
- `poetry` 
- `flask`
- `SQLAlchemy`
- `Postman` (optional, used for testing c:)

### Installation Steps
1. **Clone the Repository**
   ```sh
   git clone <repo-url>
   cd backend-challenge
   ```

2. **Install Dependencies**
   ```sh
   poetry install
   ```

3. **Setup the Database**
   ```sh
   poetry shell
   python3 bootstrap.py
   ```
   This creates the database and loads initial club data from `clubs.json`.

4. **Run the Application**
   ```sh
   flask run
   ```

The server should now be running at `http://127.0.0.1:5000/`.

## API Documentation

#### 1. Get All Clubs
**URL:** `/api/clubs`  
**Method:** `GET`  
**Description:** Returns a list of all clubs stored in the database.  
**Endpoint:** My thought: access api, access clubs, GET method will access information   
**Response:**
```json
[
  {
    "id": 1,
    "code": "pppjo",
    "name": "Penn Pre-Professional Juggling Organization",
    "description": "The PPPJO is looking for intense jugglers seeking to juggle their way to the top.",
    "tags": ["Pre-Professional", "Athletics", "Undergraduate"]
  }
]
```

#### 2. Search for a Club
**URL:** `/api/clubs/search?q=<query>`  
**Method:** `GET`  
**Description:** Searches clubs by name. Use keywords for the field <query> to find clubs.  
**Endpoint:** My thought: access api, access clubs tab, search field to search for the specific club the user is trying to find

#### 3. Create a New Club
**URL:** `/api/clubs`  
**Method:** `POST`  
**Description:** Create a new club to be saved  
**Endpoint:** My thought: access api, access clubs, since its POST method, this URL will "create" a new club compared to accessing information  
**Request Body:**
```json
{
  "code": "new-club",
  "name": "New Club Name",
  "description": "Description of the club",
  "tags": ["example-tag", "example-tag", "etc"]
}
```

#### 4. Mark a Club as Favorite
**URL:** `/api/clubs/<club_code>/favorite`  
**Method:** `POST`  
**Description:** User "favorites" the club. Increments the favorite count for the users selected club.  
**Endpoint:** My thought: access api, clubs section, the specific club, then "favorite" to favorite the club  

#### 5. Modify Club Details
**URL:** `/api/clubs/<club_id>`  
**Method:** `PUT`  
**Description:** Modify a current club (either descriptions, tags, name)  
**Endpoint:** My thought: access api, clubs section, then the club_id to modify the club the user wants to modify  
**Request Body:**
```json
{
  "name": "Updated Club Name",
  "description": "Updated description",
  "tags": ["Updated", "Tags"]
}
```
**Response:**
```json
{
  "id": "same-id",
  "code": "example-code",
  "name": "Updated Club Name",
  "description": "Updated description",
  "tags": ["Updated", "Tags"]
}
```

#### 6. Get All Tags and Their Counts
**URL:** `/api/tags`  
**Method:** `GET`  
**Description:** Returns a JSON object with tag names as keys and their occurrence counts as values.  
**Endpoint:** My thought: access api, then access tag page to get the json object with tag names and their occurences. 

#### 7. Get User Profile
**URL:** `/api/user/<username>`  
**Method:** `GET`  
**Description:** Fetches user profile information based on the provided username.  
**Endpoint:** My thought: access api, then the user page, then the username of the user to access the information of the user  
**Response:**
```json
{
  "username": "josh",
  "email": "josh@gmail.com"
}
```

---

## Design Decisions & Justifications

### 1. Database Models
- **User Model:** 
  - Includes `username`, `email`, and `password_hash`. Password isn't shown when the user information is requested due to security. 
  - Ensures unique constraints on usernames and emails for security.
- **Club Model:** 
  - Includes `code`, `name`, `description`, `tags`, and `favorite_count`.
  - Uses `JSON` type for `tags` to allow flexibility.
  - `favorite_count` is stored in the Club model data for easy, reliable access

### 2. API Design Choices
- I used RESTful principles with proper and clear endpoint names to ensure predictable URLs (e.g., `/api/clubs`, `/api/user/<username>`). Each endpoint applies to standard HTTP methods (`GET`, `POST`, `PUT`) to define actions clearly for the ease of use for users and frontend developers.
- `GET` requests return JSON lists or objects.
- `POST` and `PUT` requests require JSON input with proper validation.
- `search` uses `ilike` for case-insensitive matching.


---

## Next Steps

Next steps is to add more user information, such as the user's favorite clubs, what tags the user is interested in, potentially a bio, what clubs the user is in, etc. Another feature is to enable users to leave comments and reviews for clubs. Also adding more security features for authentication will help promote security, adding admin roles that are only allowed to edit certain parts of information (like modifying and adding clubs). 

---
## Testing the API
Use **Postman** to test the API endpoints.

