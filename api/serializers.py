from rest_framework import serializers
from . import views
from api.models import Application, Indice, Satellite, Band
from satsearch import Search
import requests
import pandas as pd

class IndiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indice
        fields = ['name', 'accr', 'description', 'is_NormalizedDifference', 'calc', ]

class SatelliteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Satellite
        fields = ['name', 'accr', 'operator', ]

class BandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Band
        fields = ['band', 'description', 'wavelength', 'resolution', ]

class OsdSerializer(serializers.ModelSerializer):
    bands = BandSerializer(source='indice_to_use.needed_bands', many=True)
    satellite = SatelliteSerializer(source='indice_to_use.satellite_to_use')
    indice = IndiceSerializer(source='indice_to_use')
    files = serializers.SerializerMethodField()

    def get_files(self, instance):
        bands = instance.bands

        # geocoding
        # place = self.context['location']
        # response = requests.get(f"https://nominatim.openstreetmap.org/search?q={place}&format=json&polygon_geojson=1&addressdetails=0&limit=1")
        # json_object = response.json()
        # bb = json_object[0]['boundingbox']
        # bbx = [float(x) for x in bb]

        # aws configuration
        url = 'https://earth-search.aws.element84.com/v0' # URL to Sentinel 2 AWS catalog
        collection = 'sentinel-s2-l2a-cogs'

        # aws search parameter
        startDate = self.context['date_from']
        endDate = self.context['date_to']
        # location = [
        #             11.40020,
        #             53.63612,
        #             11.44569,
        #             53.62385
        #             ]

        bbox_search = Search(
            bbox=self.context['location'],
            datetime=startDate+"/"+endDate,
            query={'eo:cloud_cover': {'lt': 50}, 'sentinel:data_coverage': {'gt': 80}},
            collections=[collection],
            url=url,
            sortby = '+properties.eo:cloud_cover', 
        )

        items = bbox_search.items()

        downloads = {}

        for i, item in enumerate(items):

            data = {}

            data['Product ID']= item.properties["sentinel:product_id"]
            data['Preview']= item.asset("thumbnail")["href"]
            data['Date']= item.properties["datetime"]
            data['Cloud cover']= item.properties["eo:cloud_cover"]
            data['Latitude band']= item.properties["sentinel:latitude_band"]
            data['Grid']= item.properties["sentinel:grid_square"]
            data['UTM Zone']= item.properties["sentinel:utm_zone"]
            data['Sequence']= item.properties["sentinel:sequence"]
            data['Projection']= item.properties["proj:epsg"]
            data['Data coverage']= item.properties["sentinel:data_coverage"]

            for band in bands.split(','):
                data[band] = item.asset(band)["href"]

            downloads[i] = data

        df=pd.DataFrame.from_dict(downloads, orient='index')
        df=df.drop_duplicates('Grid')
        results = df.to_dict(orient='index')
        
        return results

    class Meta:
        model = Application
        fields = ['machine_name', 'name', 'description', 'indice', 'satellite', 'bands', 'files', ]
