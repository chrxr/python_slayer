import random
from operator import itemgetter, attrgetter, methodcaller

TO_HIT_CHART = [
          [4,4,5,6,6,6,6,6,6,6],
          [3,4,4,4,5,5,6,6,6,6],
          [2,3,4,4,4,4,5,5,5,6],
          [2,3,3,4,4,4,4,4,5,5],
          [2,2,3,3,4,4,4,4,4,4],
          [2,2,3,3,3,4,4,4,4,4],
          [2,2,2,3,3,3,4,4,4,4],
          [2,2,2,2,3,3,3,3,4,4],
          [2,2,2,2,3,3,3,3,3,4],
         ]

TO_WOUND_CHART = [
          [4,5,6,6,9,9,9,9,9,9],
          [3,4,5,6,6,9,9,9,9,9],
          [2,3,4,5,6,6,9,9,9,9],
          [2,2,3,4,5,6,6,9,9,9],
          [2,2,2,3,4,5,6,6,9,9],
          [2,2,2,2,3,4,5,6,6,9],
          [2,2,2,2,2,3,4,5,6,6],
          [2,2,2,2,2,2,3,4,5,6],
          [2,2,2,2,2,2,2,3,4,5],
          [2,2,2,2,2,2,2,2,3,4],
         ]

def battle(fighters):
    # Compare initiative to arrange fighting order. Highest initiatve goes first
    fighters_ordered = sorted(fighters, key=attrgetter('initiative'), reverse=True)
    while fighters_ordered[0].hit_points > 0 and fighters_ordered[1].hit_points > 0:
        fighters_ordered = round(fighters_ordered)
        try:
            if fighters_ordered[0].winner == True:
                announcement = str.format("{0} the {1} is the winner!", fighters_ordered[0].name, fighters_ordered[0].race)
                print(announcement)
        except:
            pass
        fighters_ordered.reverse()

def round(fighters):
    to_hit = TO_HIT_CHART[fighters[0].weapon_skill][fighters[1].weapon_skill]
    roll = random.randrange(1,6)
    f_name = fighters[0].name
    f_race = fighters[0].race
    hit_notice = "{0} the {1} scores a hit!"
    miss_notice = "{0} the {1} misses by a whisker!"
    wound_notice = "{0} the {1} wounds their opponent!"
    wound_fail_notice = "{0} the {1} fails to wound their opponent!"

    if roll >= to_hit:
        print(str.format(hit_notice, f_name, f_race))
        to_wound = TO_WOUND_CHART[fighters[0].strength][fighters[1].toughness]
        roll = random.randrange(1,6)
        if roll >= to_wound:
            print(str.format(wound_notice, f_name, f_race))
            fighters[1].hit_points -= 1
        if fighters[1].hit_points <= 0:
            fighters[0].winner = True
    else:
        print(str.format(miss_notice, f_name, f_race))
    return fighters
