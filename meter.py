
import sys,os,argparse
from collections import defaultdict
from datetime import datetime
 
# main  data structures
meters = defaultdict(list)
VALID_METER_READINGS = []
INVALID_METER_READINGS = []
READING_DATES = []

def parse(args):
    """ This function captures the command-line arguements"""
    parser = argparse.ArgumentParser(description="Analyse meter readings.")
    parser.add_argument('sourcefile', help = " Add a valid file with meter readings.")
    return parser.parse_args(args)

def run(filename):
    """ This function reads raw data from file, processes the data
    and stores the data in global variables. If a meter mre than one reading 
    its values are stored in a list"""
    with open(filename, 'r') as fileone:
        data = fileone.readlines()[1:-1]
        clean_data = [line.strip('|\n METER READING') for line in data]

        # map meter with its reading
        mapped_readings = (zip(clean_data[::2],clean_data[1::2]))
        
        for meter , reading in mapped_readings:
            meters[meter].append(reading.split('|')) 

        for meter_id, reading in meters.items():
            for item in reading:
                reading_id = item[0]
                reading_value = float(item[1])
                reading_date = datetime.strptime(item[2],'%Y%m%d').date()
                reading_status = item[3]
                
                # populate global lists
                READING_DATES.append(reading_date)
                if reading_status == 'V':
                    VALID_METER_READINGS.append(reading_value)
                else:
                    INVALID_METER_READINGS.append(reading_value)
 


def main(argv):
    """ Program entry point, above functions are called here. """
    #Input data 
    parser = parse(argv[1:])
    
    inputfile = parser.sourcefile
    
    # Data processing
    try:
      run(inputfile)
    except FileNotFoundError:
        print("File name does not exist, please ensure file is in current directory")

    else:
    # Output data
        print('\n\n', 'METER READINGS'.center(40))
        print(f'Number of meters: {len(meters.keys()):->28} ')
        print(f'Total valid readings: {sum(VALID_METER_READINGS):->30}')
        print(f'Total invalid readings: {sum(INVALID_METER_READINGS):->30}')
        print(f'Highest valid reading: {max(VALID_METER_READINGS):->30}')
        print(f'Lowest valid reading: {min(VALID_METER_READINGS):->30}')
        print('\n')
        print(f'Newest reading:         {max(READING_DATES)}')
        print(f'Oldest  reading:        {min(READING_DATES)}')
        print('\n\n\n')


if __name__ == '__main__':
    sys.exit(main(sys.argv))
         


