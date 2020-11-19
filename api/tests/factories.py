from .. import models
from faker.factory import Factory
import factory.fuzzy
Faker = Factory.create
fake = Faker()
fake.seed(0)


class OlympianFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = models.Olympian

  name = factory.Sequence(lambda n: 'Olympian %d' % n)
  sex = factory.fuzzy.FuzzyChoice(['M', 'F'])
  age = factory.fuzzy.FuzzyInteger(8, 70)
  height = factory.fuzzy.FuzzyInteger(100, 210)
  weight = factory.fuzzy.FuzzyInteger(30, 120)
  team = fake.country()
  sport = fake.sentence(nb_words=3, variable_nb_words=True)


class EventFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = models.Event

  name = factory.Sequence(lambda n: 'Event %d' % n)
  games = '2016 Summer'
  sport = fake.sentence(nb_words=4, variable_nb_words=True)


class EventOlympianFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.EventOlympian

    event = factory.SubFactory(EventFactory)
    olympian = factory.SubFactory(OlympianFactory)
    medal = factory.fuzzy.FuzzyChoice(['Gold', 'Silver', 'Bronze'])

