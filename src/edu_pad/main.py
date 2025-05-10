from dataweb import DataWeb
import pandas as pd

def main():
    dataweb=DataWeb()
    df=pd.DataFrame() 
    df=dataweb.obtenerdatos()
    df.to_csv("DataWebPremierLeague.csv")

if __name__ == "__main__":
    main()    
    