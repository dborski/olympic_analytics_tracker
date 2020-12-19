# Olympic Analytics Tracker
[![Build Status](https://travis-ci.com/dborski/olympic_analytics_tracker.svg?branch=main)](https://travis-ci.com/dborski/olympic_analytics_tracker)

Olympics Analytics Tracker is an API that exposes several analytical endpoints using data from the 2016 Summer Olympics. The data is imported by CSV and stored in the API's database.


This site is deployed in production to Heroku [here](https://olympic-analytics-tracker-db.herokuapp.com/)

## Contributors
* [Derek Borski](https://github.com/dborski)

## Tech Stack
* Django
* PostgreSQL
* Travis CI
* Heroku

## API Endpoints

### All Olympians

```
GET /api/v1/olympians
```
Description:
- Displays name, team, age, sport, and total medals won for each olympian
- Returns a 200 status code on success

Response Body:
```
{
  "olympians":
    [
      {
        "name": "Maha Abdalsalam",
        "team": "Egypt",
        "age": 18,
        "sport": "Diving"
        "total_medals_won": 0
      },
      {
        "name": "Ahmad Abughaush",
        "team": "Jordan",
        "age": 20,
        "sport": "Taekwondo"
        "total_medals_won": 1
      },
      {...}
    ]
}
```

### Youngest Olympian

```
GET /api/v1/olympians?age=youngest
```
Description:
- Displays name, team, age, sport, and total medals won for the youngest olympian
- Returns a 200 status code on success

Response Body:
```
{
  "olympians":
    [
      {
        "name": "Ana Iulia Dascl",
        "team": "Romania",
        "age": 13,
        "sport": "Swimming"
        "total_medals_won": 0
      }
    ]
}
```

### Oldest Olympian

```
GET /api/v1/olympians?age=oldest
```
Description:
- Displays name, team, age, sport, and total medals won for the oldest olympian
- Returns a 200 status code on success

Response Body:
```
{
  "olympians":
    [
      {
        "name": "Julie Brougham",
        "team": "New Zealand",
        "age": 62,
        "sport": "Equestrianism"
        "total_medals_won": 0
      }
    ]
}
```

### Olympian Stats

```
GET /api/v1/olympian_stats
```
Description:
- Displays total count of olympians, average weight for males and females, and average age of all olympians
- Returns a 200 status code on success

Response Body:
```
{
  "olympian_stats": {
    "total_competing_olympians": 3120
    "average_weight:" {
      "unit": "kg",
      "male_olympians": 75.4,
      "female_olympians": 70.2
    }
    "average_age:" 26.2
  }
}
```

### All Events by Sport

```
GET /api/v1/events
```
Description:
- Displays a list of all event names sorted by their respective sports
- Returns a 200 status code on success

Response Body:
```
{
  "events":
    [
      {
        "sport": "Archery",
        "events": [
          "Archery Men's Individual",
          "Archery Men's Team",
          "Archery Women's Individual",
          "Archery Women's Team"
        ]
      },
      {
        "sport": "Badminton",
        "events": [
          "Badminton Men's Doubles",
          "Badminton Men's Singles",
          "Badminton Women's Doubles",
          "Badminton Women's Singles",
          "Badminton Mixed Doubles"
        ]
      },
      {...}
    ]
}
```

### Event Medalists

```
GET /api/v1/events/:event_id/medalists
```
Description:	
- Displays a list of all medalists for a specific event	
- Returns a 200 status code on success	
- *Note: Not all medalists for each event are included in the sample data*

Response Body:
```
{
  "event": "Badminton Mixed Doubles",
  "medalists": [
      {
        "name": "Tontowi Ahmad",
        "team": "Indonesia-1",
        "age": 29,
        "medal": "Gold"
      },
      {
        "name": "Chan Peng Soon",
        "team": "Malaysia",
        "age": 28,
        "medal": "Silver"
      }
    ]
}
```
