import random
when = ['A few years ago', 'Yesterday', 'Last night', 'long long time ago','On 27th Dec']
who = ['a donkey', 'an alien', 'a lion', 'a turtle','a turtle']
name = ['Tony', 'TChalla','Thor', 'Bucky', 'Thanos']
residence = ['Knowhere','Atlantis', 'Wakanda', 'Rohtak', 'My ex house']
went = ['date', 'asylum','graveyard', 'school', 'washroom']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' whose name is ' + random.choice(name) +' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))