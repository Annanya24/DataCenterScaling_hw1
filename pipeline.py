#import pip

#def import_or_install(package):
    #try:
        #__import__(package)
    #except ImportError:
        #pip.main(['install', package])

#import_or_install('pandas')
#import_or_install('datetime')
#import_or_install('argparse')

import pandas as pd
from argparse import ArgumentParser

from datetime import date
def extract(source):
    return pd.read_csv(source)

def age(data):
    df = data.copy()
    today = date.today()
    age = []

    for i in range(len(df)):
        birth_date = date(df['year'][i], df['month'][i], df['date_of_month'][i])
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age.append(today.year - birth_date.year - 1)
        else:
            age.append(today.year - birth_date.year)
    
    df['age'] = age
    return df

def final_data(data, target):
    data.to_csv(target, index=False)
    
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('source',help='source.csv')
    parser.add_argument('target', help='target.csv')
    args = parser.parse_args()

    source_data = extract(args.source)
    processed_data = age(source_data)
    final_data(processed_data, args.target)

    print(f"Data processed and saved to '{args.target}' successfully.")
