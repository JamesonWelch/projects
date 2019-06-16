gender = str(input('Enter your gender: "m" for male, "f" for female: '))
gender = gender.lower()

player = str(input('Enter your name: '))
plater = player.capitalize()

if gender == 'm':
    queen = str(input('What\'s the name of your queen? '))
    queen = queen.capitalize()

if gender == 'f':
    king = str(input('What\'s the name of your king? '))
    king = king.capitalize()

kingdom = str(input('What\'s the name of your kingdom? '))
kingdom = kingdom.capitalize()

allies = str(input('Do you have allies? Enter "y" for yes or "n" for no. '))
allies = allies.lower()

enemies = str(input('Do you have enemies? Enter "y" for yes or "n" for no. '))
enemies = enemies.lower()

if allies == 'y':

    paladin = str(input('What is your paladin\'s name? '))
    paladin = paladin.capitalize()

    wizard = str(input('What is your wizard\'s name? '))
    wizard = wizard.capitalize()

    warrior = str(input('What is your warrior\'s name? '))
    warrior = warrior.capitalize()

if enemies == 'y':
    print(player, 'got enemies, got a lot of enemies.')

    villain = str(input('What is your villain\'s name? '))
    villain = villain.capitalize()

    thief = str(input('What is your thief\'s name? '))
    thief = thief.capitalize()

    sorcerer = str(input('What is your sorcerer\'s name? '))
    sorcerer = sorcerer.capitalize()

    rogue = str(input('What is your rogue\'s name? '))
    rogue = rogue.capitalize()


    war = str(input('What is the name of your war? '))
    war = war.capitalize()

    years = str(input('How many years did the war last? '))

if gender == 'm':
    prn = 'his'
    prn_short = 'he'
    spouse = 'queen'
    title = 'king'
    name_title = title + ' ' + player
    name_title = name_title.capitalize()
    spouse_title = spouse + ' ' + queen
    spouse_title = spouse_title.capitalize()
elif gender == 'f':
    prn = 'her'
    prn_short = 'she'
    spouse = 'king'
    title = 'queen'
    name_title = title + ' ' + player
    name_title = name_title.capitalize()
    spouse_title = spouse + ' ' + king
    spouse_title = spouse_title.capitalize()

if allies == 'y' and enemies == 'y':
    story = """The great """ + player + """ and """ + prn + """ """ + spouse_title + """ peacefully ruled the
    kingdom of """ + kingdom + """. However, a great war called """ + war + """ erupted.
    """ + player + """'s nemesis """ + villain + """ invaded """ + prn + """ kingdom allying with a thief,
    an evil sorcerer, and a rogue. With the help of
    """ + thief + """, """ + sorcerer + """, and """ + rogue + """, """ + villain + """ pillaged their land, stole
    precious resources, and brutally attacked their villagers.

    But the kingdom of """ + kingdom + """ had a paladin, a wizard and a warrior as allies.
    """ + name_title + """ and """ + spouse_title + """ with the help of """ + paladin + """, """ + wizard + """, and
    """ + warrior + """ valiantly fought back and defeated """ + villain + """ after """ + years + """ years of
    fierce fighting. Order was finally restored and everyone in their kingdom
    lived happily ever after :-)."""

elif allies == 'y' and enemies == 'n':
    story = """The great """ + player + """ and """ + prn + """ """ + spouse_title + """ peacefully ruled the
    kingdom of """ + kingdom + """. The power of that kingdom was so great that any enemy
    fled far away to escape the righteous justice the """ + title + """ used to insure a
    peaceful kingdom.
    The kingdom of """ + kingdom + """ also had strong allies in a paladin, a warrior and a
    wizard who knew no equals in skill. With the help of """ + paladin + """, """ + warrior + """, and """ + wizard + """
    order was constant in """ + name_title + """'s realm of """ + kingdom + """ and everyone in their kingdom
    lived happily ever after."""

elif allies == 'n' and enemies == 'n':
    story = """The great """ + player + """ and """ + prn + """ """ + spouse_title + """ peacefully
     ruled the kingdom of """ + kingdom + """. However, it as a realm bereft of epic tales of war and
    struggle because not only did """ + player + """ not have any enemies, """ + prn_short + """ had no allies
    either.
    But the denizens of """ + kingdom + """ have no need of epic tales because they enjoy a
    peaceful existence and everyone lived happily ever after."""

elif allies == 'n' and enemies == 'y':
    story = """The great """ + player + """ and """ + prn + """ """ + spouse_title + """
    ruled the kingdom of """ + kingdom + """ through constant turmoil. A great war called """ + war + """ erupted.
    """ + player + """'s nemesis """ + villain + """ invaded """ + prn + """ kingdom allying with a thief,
    an evil sorcerer, and a rogue. With the help of
    """ + thief + """, """ + sorcerer + """, and """ + rogue + """, """ + villain + """ pillaged their land, stole
    precious resources, and brutally attacked their villagers.

    There was little resistance """ + name_title + """ and """ + spouse_title + """ could
    send because the paladins, the warriors and the wizards of old aren't around anymore
     who are willing to fight.

    But """ + player + """ received a stroke of luck because """ + prn + """ nemesis """ + villain + """ leading
    the thief, the evil sorcerer and the rogue succumbed to their own depravity.
    Their greed and lust for blood eventually caused them to turn on each other.
    Not one of them survived the mutiny. After an unchecked war of """ + years + """ years, and a long time to heal and
    repair the damage, order was finally restored in """ + kingdom + """, allies were gradually acquired,
    and everyone lived happily ever after."""

print(story)
