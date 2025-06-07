from src.edu_pad.database import DataBase
import pandas as pd

def main():
    database=DataBase()
    df=pd.read_csv("src/edu_pad/static/csv/DataWebPremierLeague.csv")
    df_db=database.guardar_df(df)
    

if __name__ == "__main__":
    main()