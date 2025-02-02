# Open-Ended Questions

## 1. 

For the signup feature, I would create a /api/register route that accepts a POST request with user details (username, email, password). Passwords need to be hashed using a secure hashing algorithm, like bcrypt, before storing them in the database to prevent security issues. This ensures that even if a hacker gains access to the database, they cannot easily get passwords. Then, I would validate user input to prevent SQL injection and other vulnerabilities. For Python Packages, looking at through resources/internet, I found Flask-JWT-Extended for token-based authentication and werkzeug.security for password hashing.

For the login feature, I would create a /api/login route that accepts a POST request with the user's credentials (username/email and password). To handle potential security risks, I would use JSON Web Tokens to handle authentication. This is because JSON Web Tokens are stateless and can include user roles and permissions, making them ideal for scalable systems, meaning it will be able to handle a large database for the large number of Penn students. For Python Packages, I would use Flask-JWT-Extended to handle token creation and validation.

For the logout feature, I would create a /api/logout route that invalidates the user's JWT token. To handle logout, I would create and maintain a blacklist of revoked tokens in a database. This ensures that even if a token is stolen, it can be invalidated, and thus, secure. I would also use HTTPS to encrypt all communication between the client and server, preventing token interception.

For existing protocols, I would follow OAuth 2.0 and OpenID Connect standards for a strong authentication system to prevent security breaches. These are widely used, secure protocols that provide standardized ways to handle authentication and authorization.

## 2.

To allow users to reply to other users in a nested comment structure, I can implement a self-referential Comment model. This enables comment chains, allowing users to have structured discussions under club posts. (like a linked list, keeping track of the beginning comment, the next comment, and the end comment)

Database Structure:
- Each comment is stored in a database table.
- Every comment has a user (who wrote it) and a club (under which the discussion is happening).
- To support replies, each comment can have an optional parent comment.
- If a comment has no parent, it's a top-level comment.
- If a comment has a parent, it’s a reply.
  
If a user comments on a club, the comment is stored without a parent reference. If a user replies** to a comment, the comment is linked to its parent using an identifier. This allows each reply to be connected to the comment it belongs to. When a user submits a comment, the system checks: if the comment is a new top-level comment, then it is stored normally, or ff the comment is a reply, then it is stored with a reference to the comment it is replying to. This ensures that replies are correctly linked to their parent comments. When fetching comments for a club, the system retrieves all top-level comments (comments without a parent), looks for replies linked to those comments, then structures the results so that each comment includes its replies. The way replies are handled are that replies are stored in the same table as normal comments, where each reply points to its parent comment. The system then retrieves all parent comments first, then finds and groups replies under them. In order to support long comment chains, since comments are linked to each other like a chain, users can reply multiple times to the same thread. The system then keeps track of all replies, making long conversations possible. If a discussion thread gets too long, I would use pagination, meaning only a certain number of replies are first loaded, and if the user scrolls, then more replies are fetched as the user scrolls. 



## 3.

Some routes in my API that I think are worth caching are the fetching all clubs, retrieving details for a single club, and searching for clubs routes. The "get clubs" endpoint is frequently accessed, and since club data does not change often, caching reduces repeated database queries, improving response time. Similarly, fetching "details and searching for a single club" is a common operation, and storing recent responses in the cache would help to prevent multiple identical queries. 

To handle cache invalidation, time-based expiration  is one approach, where cached data automatically expires after a defined period (e.g., every 5-10 minutes), ensuring that stale data does not persist indefinitely (an example is the favorites information for a club, data is update every few minutes to keep data up to date if the data is cached). Event-driven invalidation is another technique that could handle cache invalidation. Cache would be cleared whenever relevant data is updated (when a new club is added, modified, or deleted). This ensures that the most recent data is available without unnecessary database queries. 

To implement caching efficiently, Redis can be used for applying caching to API responses and provides in-memory storage, enabling extremely fast retrieval, automatic expiration, and distributed caching, making it ideal for high-traffic APIs, especially if Penn Club Review has high traffic (such as during club recruiting season). 


