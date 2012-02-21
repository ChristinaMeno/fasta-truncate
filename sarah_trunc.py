import sys
import re
import pycountry

MAX_LEN = int(sys.argv[2])
PREFIX_LENGTH = 8
subdivision_codes = dict([(x.name.lower(),x.code) for x in pycountry.subdivisions])

translation_table = dict(avian=('american_black_duck',
                                'american_coot',
                                'american_green_winged_teal',
                                'american_wigeon',
                                'bar_headed_goose',
                                'blue_winged_teal',
                                'brown_headed_gull',
                                'african_starling',
'northern_pintail',
'african_starling',
'american_widgeon',
'greater_white_fronted_goose',
'whistling_swan',
'whistlingswan',
'white_backed_munia',
'whitefronted_goose',
'white_front_goose',
'white_winged_scoter',
'whooper_swan',
'wild_bird',
'wild_duck',
'yellow_headed_amazon',
'aquatic_bird',
'australian_shelduck',
'bald_eagle',
'bar_headed_goose',
'barnacle_goose',
'black_billed_magpie',
'black_crowned_night_heron',
'black_duck',
'black_headed_gull',
'blackhead_gull',
'black_necked_grebe',
'blue_winged_teal',
'bewick_s_swan',
'bewicks_swan',
'brown_headed_gull',
'california_gull',
'canada_goose',
'cinnamon_teal',
'common_buzzard',
'domestic_duck',
'domestic_mallard_duck',
'double_crested_cormorant',
'eurasian_coot',
'eurasian_wigeon',
'glaucous_gull',
'golden_mountain_thrush',
'golden_pheasant',
'gray_teal',
'great_crested_grebe',
'great_egret',
'greater_scaup',
'greater_white_fronted_goose',
'green_winged_teal',
'grey_heron',
'greylag_goose',
'gsc_chicken',
'gsc_chicken_b',
'guinea_fowl',
'herring_gull',
'hooded_vulture',
'house_crow',
'japanese_quail',
'korean_native_chicken',
'laughing_gull',
'least_sandpiper',
'lesser_kestrel',
'lesser_scaup',
'little_grebe',
'longtail_duck',
'magpie_robin',
'mallard',
'mallard_duck',
'migratory_duck',
'mongolian_gull',
'mountain_hawk_eagle',
'muscovy_duck',
'open_billed_stork',
'open_bill_stork',
'openbill_stork',
'ostrich',
'pacific_black_duck',
'pekin_duck',
'peking_duck',
'peregrine_falcon',
'pheasant',
'pink_footed_goose',
'pintail_duck',
'red_crested_pochard',
'redhead_duck',
'red_headed_duck',
'red_necked_stint',
'red_winged_tinamou',
'ring_billed_gull',
'ring_necked_duck',
'rock_dove',
'rosy_billed_pochard',
'rubby_shelduck',
'ruddy_shelduck',
'ruddy_turnstone',
'rufous_necked_stint',
'scaly_breasted_munia',
'semi_palmated_sandpiper',
'sharp_tailed_sandpiper',
'shorebird',
'silky_chicken',
'silver_pheasant',
'slaty_backed_gull',
'snow_goose',
'softbill',
'sooty_tern',
'spot_billed_duck',
'tree_sparrow',
'tundra_swan',
'wedge_tailed_shearwater',
'western_grebe',
'northern_shoveler',
                                ))


def smart_truncate(line):
    
    line = line.lower()
    if len(line.split('|')) > 1:
        line = line[0]

    for x in line.split('/'):
        '''
        if x in translation_table['avian']:
            line = re.sub(x, 'avian', line)
            
        if x.lower() in subdivision_codes:
            line = re.sub(x, subdivision_codes[x.lower()], line)
    
        try:
            abbr = pycountry.countries.get(name=x.title().replace('_', ' ')).alpha2
        except KeyError:
            pass
        else:
            #line = re.sub(x, abbr, line)
            pass
        '''
        
    double_start = line.rfind(line[1:PREFIX_LENGTH], PREFIX_LENGTH)
    if double_start != -1:
        line = line[double_start:] 
        
        
    line = re.sub('environment', 'env', line)

    line = re.sub('north_|south_|east_|west_|interior_|central_|western_', '', line)


    if len(line)  > MAX_LEN:
        print line,
        '''
        try:
            print "'{0}',\n".format(line.split('/')[1]),
        except:
            pass
        '''
    return line    
                   
def main():        
    with open(sys.argv[1], 'r') as f:
        for line in f:
            if line.startswith('>'):
                line = smart_truncate(line)
            #print line,
                   
if __name__ == '__main__':
    sys.exit(main())

