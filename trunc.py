import sys
import re

MAX_LEN = int(sys.argv[2])
PREFIX_LENGTH = 8

avian = (
'african_starling',
'american_black_duck',
'american_green_winged_teal',
'american_widgeon',
'australian_shelduck',
'bar_headed_goose',
'black_billed_magpie',
'black_crowned_night_heron',
'black_headed_gull',
'black_necked_grebe',
'blue_winged_teal',
'brown_headed_gull',
'domestic_mallard_duck',
'double_crested_cormorant',
'golden_mountain_thrush',
'great_crested_grebe',
'greater_white_fronted_goose',
'green_winged_teal',
'korean_native_chicken',
'mountain_hawk_eagle',
'northern_pintail',
'northern_shoveler',
'open_billed_stork',
'pacific_black_duck',
'peregrine_falcon',
'pink_footed_goose',
'red_crested_pochard',
'red_necked_stint',
'red_winged_tinamou',
'ring_billed_gull',
'ring_necked_duck',
'rosy_billed_pochard',
'rufous_necked_stint',
'scaly_breasted_munia',
'semi_palmated_sandpiper',
'sharp_tailed_sandpiper',
'slaty_backed_gull',
'spot_billed_duck',
'wedge_tailed_shearwater',
'white_backed_munia',
'whitefronted_goose',
'white_front_goose',
'white_winged_scoter',
'yellow_headed_amazon',
'ruddy_turnstone',
)

trans = (('environment', 'env'),
         ('california', 'CA'),
         ('thailand', 'thai'),
         ('guangxi_luochengmulaozuzizhi', 'china'),
         ('north_|south_|east_|west_|interior_|central_|western_', ''),
        ('>a/ft_benning/wrair1669p/2009_h1n1_a/ft.benning/wrair1669p/2009_h1n1__', '>a/ft_benning/wrair1669p/2009_h1n1_'),
        ('>a/aa/huston/1945__|_a_/_h1n1__', '>a/aa/huston/1945_h1n1__'),
)

def smart_truncate(line):
    
    line = line.lower()

    for pattern, replacement in trans:
        line = re.sub(pattern, replacement, line)
    
    pipe_parts = line.split('|')
    if len(pipe_parts) > 1:
        line = pipe_parts[0] + '|A'

    for x in line.split('/'):
        if x in avian:
            line = re.sub(x, 'avian', line)
            
    double_start = line.rfind(line[1:PREFIX_LENGTH], PREFIX_LENGTH)
    if double_start != -1:
        line = line[double_start:] 

    return line.strip().title() + '\r\n' 
                   
def main():        
    with open(sys.argv[1], 'r') as f:
        for line in f:
            if line.startswith('>'):
                line = smart_truncate(line)
            print line,
                   
if __name__ == '__main__':
    sys.exit(main())

