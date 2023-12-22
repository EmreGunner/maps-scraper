from src.gmaps import Gmaps
import pandas as pd


#example = ["https://www.google.com/maps/place/?q=place_id:ChIJH97tACXHyhQRo_gS1J_i0YY"]
def get_comps_fromCsv(inputfile):
    df = pd.read_csv(inputfile)
    comps_list = df['Detailed URL'].to_list()
    return comps_list

inputfile = "/home/titan/Desktop/Python/ForMarketing/google-maps-scraper/competitor_placeIds_links.csv"
comp_list = get_comps_fromCsv(inputfile)    
#print(comp_list)
print(comp_list[:10])
Gmaps.links(links=comp_list,output_folder="/test4")