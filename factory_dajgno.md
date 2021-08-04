import factory
from factory.faker import faker
from .models import *


faker = faker.Faker()


print(faker.first_name())
print(faker.last_name())

print(faker.name())

print(faker.email())
print(faker.word())
print(faker.text())
print(faker.sentence())

print(vars(factory.Faker('name')))
print()

print(faker.paragraph(nb_sentences=5))

print(faker.sentence(nb_words=6))


print(faker.sentences(nb=3))

print(faker.text(max_nb_chars=200))

print(faker.words(nb=3, ext_word_list=None, unique=False))


class UserFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Person 
		django_get_or_create = ('name','age')

	name = faker.name()
	age = faker.random_int(min=10, max=40)
 
 
for i in range(10):
	print(UserFactory(name= faker.name(), age= faker.random_int(min=10, max=40)))
	
	
	
class ProductFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Product
		django_get_or_create = ('name', 'price','person')
		
	name = faker.name()
	price = faker.random_int(min=10, max=40)
	person = factory.SubFactory(UserFactory)



		
for i in range(3):
	print(ProductFactory(name= faker.name(), price= faker.random_int(min=40, max=400), person = factory.SubFactory(UserFactory)))
 
 
for i in range(3):
	print(ProductFactory(name= faker.name(), price= faker.random_int(min=40, max=400), person = factory.SubFactory(UserFactory)))
 
for i in range(3):
	print(ProductFactory(name= faker.name(), price= faker.random_int(min=40, max=400), person = per1))
		
		





address()
:example ‘791 Crist Parks, Sashabury, IL 86039-9874’

building_number()
:example ‘791’

city()
:example ‘Sashabury’

city_suffix()
:example ‘town’

country()
country_code(representation='alpha-2')
current_country()
current_country_code()
postcode()
:example 86039-9874

street_address()
:example ‘791 Crist Parks’

street_name()
:example ‘Crist Parks’

street_suffix()
:example ‘Avenue’

faker.providers.person
classfaker.providers.person.en.Provider(generator)
Bases: faker.providers.person.Provider

first_name()
first_name_female()
first_name_male()
first_name_nonbinary()
language_name()
Generate a random i18n language name (e.g. English).

last_name()
last_name_female()
last_name_male()
last_name_nonbinary()
name()
:example ‘John Doe’

name_female()
name_male()
name_nonbinary()
prefix()
prefix_female()
prefix_male()
prefix_nonbinary()
suffix()
suffix_female()
suffix_male()
suffix_nonbinary()
