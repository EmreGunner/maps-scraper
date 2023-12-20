from src.gmaps import Gmaps

star_it = '''Help us reach 850 stars, and we'll break the GMaps 120 limit, giving you 150+ to 250+ potential customers per search.
             Star us to make it happen ⭐! https://github.com/omkarcloud/google-maps-scraper/'''
#"adult shop near California,"

queries = [
   "libraries near Azapkapı, Beyoğlu/İstanbul"
]

fields = [
   Gmaps.Fields.PLACE_ID, 
   Gmaps.Fields.NAME, 
   Gmaps.Fields.MAIN_CATEGORY, 
   Gmaps.Fields.RATING, 
   Gmaps.Fields.REVIEWS, 
   Gmaps.Fields.WEBSITE, 
   Gmaps.Fields.PHONE, 
   Gmaps.Fields.ADDRESS,
   Gmaps.Fields.LINK, 
   Gmaps.Fields.IS_SPENDING_ON_ADS,
   Gmaps.Fields.COMPETITORS,
   Gmaps.Fields.EMAILS,
   Gmaps.Fields.LINKEDIN,
   Gmaps.Fields.TWITTER,
   Gmaps.Fields.FACEBOOK
]
#Gmaps.places(queries, max=5)
Gmaps.places(queries,fields=fields)