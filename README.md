# sachirva-interview
Sachirva - Python Developer assignment

## Installing dependencies
- Install dependencies with `pip install -r requirements.txt`

## Usage
- Open terminal in the `src` folder.
- Run `python stair_climber.py` to view results of the stair climber problem.
- Run `python flask_application.py` to view and explore the available endpoints on your browser.

## Endpoints available
| Endpoint | Description | Example | isIdempotent |
|--|--|--|--|
| `/records` | Gets all records | Self explanatory | True |
| `/records/filter` | Gets records based on some filter parameters | `/records/filter?name=Tony&min_age=18&max_age=51&fav_sport=MMA` | True |
| `/record?id=SomeId` | Gets one record by ID  | `/record?id=U0E4CXQSWC4S` | True |
| `/record/add` | Adds record to database | `/record/add?name=Tony&age=37&fav_sport=MMA` | False |
| `/record/update` | Updates record in database. Gets record based on ID, and updates it's other parameters (not all parameters need to be updated) | `/record/update?id=VN8BB69EU1BV&name=Harrison&age=29&fav_sport=Swimming` | False |
| `/quote/delete?id=SomeId` | Deletes record from the database, based on ID (if the ID exists) | `/quote/delete?id=KEICNG84DMS7` | True |

## Notes
- I've used a CSV file as a database, instead of creating a sqlite (or any other) database, as the objective was just exposing certain endpoints.
- The IDs of all the records in the database are automatically randomly generated when new records are created.
- While searching/filtering records, note that the query params are case sensitive.