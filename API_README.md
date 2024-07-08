# API Documentation

This file contains detailed information about the API endpoints.

## Endpoints

### GET /

Fetches all characters stored in `characters.csv`.

**URL**: `/`

**Method**: `GET`

**Response**: Returns a list of dictionaries, where each dictionary contains information about a character.

**Example**:
```json
[
    {
        "name": "Rick Sanchez",
        "location": "Earth (Replacement Dimension)",
        "image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg"
    },
    {
        "name": "Morty Smith",
        "location": "Earth (Replacement Dimension)",
        "image": "https://rickandmortyapi.com/api/character/avatar/2.jpeg"
    }
]
