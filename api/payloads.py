def error_payload(error, code=400):
  return {
      'success': False,
      'error': code,
      'errors': error
  }

def olympians_payload(olympians):
  return {
      'olympians': olympians
  }

def events_payload(events):
  return {
      'events': events
  }

def medalists_payload(event, medalists):
  return {
      'event': event,
      'medalists': medalists
  }

def olympian_stats_payload(stats):
  return {
      'olympian_stats': {
          'total_competing_olympians': stats['total_olympians'],
          'average_weight': {
              'unit': 'kg',
              'male_olympians': round(stats['male_avg'], 1),
              'female_olympians': round(stats['female_avg'], 1)
          },
          'average_age': round(stats['avg_age'], 1)
      }
  }

def olympian_payload(olympian):
  return {
      'name': olympian.name,
      'team': olympian.team,
      'age': olympian.age,
      'sport': olympian.sport,
      'total_medals_won': olympian.medal_count
  }

def event_sports_payload(sport, events):
  return {
      'sport': sport,
      'events': [event.name for event in events]
  }

def event_medalists_payload(olympian):
  return {
      'name': olympian.name,
      'team': olympian.team,
      'age': olympian.age,
      'medal': olympian.medal
  }
