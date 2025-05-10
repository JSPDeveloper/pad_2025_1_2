from dataweb import DataWeb
import pandas as pd

def main():
    dataweb=DataWeb()
    df = pd.DataFrame()
    df = dataweb.obtener_datos()
    df.to_csv("DataWebPremierLeague.csv",index=False)
if __name__ == "__main__":
    main()
