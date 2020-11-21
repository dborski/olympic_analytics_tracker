Olympics Analytics Tracker is an API that has several analytical endpoints created from data of the 2016 Summer Olympics. The data is imported by CSV and stored in the APIs database.

This was created by [Derek Borski](https://github.com/dborski)

## API Endpoints

### Olympians

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
