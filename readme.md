# api.openspacedata.org

![Travic CI result](https://travis-ci.com/OpenSpaceData/api.openspacedata.org.svg?branch=master)

This API will handle the user requests and translate them to the technical parameters of the ESA's API, and it will provide all information for the [user interface](https://github.com/OpenSpaceData/get.openspacedata.org) of get.openspacedata.org.

More information about the idea of OpenSpaceData you can read here:  *[Interview: OpenSpaceData Wants to Democratise Access to Satellite Data](https://en.reset.org/blog/interview-openspacedata-wants-democratise-access-satellite-data-05252021)*
## Run Locally

Clone the project:

```bash
  git clone https://github.com/OpenSpaceData/api.openspacedata.org.git
```

Go to the project directory:

```bash
  cd api.openspacedata.org
```

Start the server with [Docker Compose](https://github.com/docker/compose):\

```bash
  docker-compose up
```
*Note: You have to install Docker and Docker Compose first.*
## API Reference

#### Send a request

```http
  http://0.0.0.0:8000/v1/{use_case}/?from={date_from}&to={date_to}&location={location}
```

or

```http
GET /v1/{use_case}/?from={date_from}&to={date_to}&location={location}
```

| Parameter | Type     | Description                | Format                |
| :-------- | :------- | :------------------------- | :------------------------- |
| `use_case` | string | Required. | `vegetation-health` |
| `date_from` | date | Required. |  `2021-03-01` |
| `date_to` | date | Required. |  `2021-03-30` |
| `location` | string | Required. |  `Berlin` |

#### Use Cases
There are multiple defined use cases which can requested:

| Name | String |
| :-------- | :------- |
| Visualize Urban Development | `urban-development` |
| Visualizing Barren Soil | `barren-soil` |
| Detect Burned Areas | `burned-areas` |
| True Color Image | `true-color` |
| Detect Snow Cover | `snow-cover` |
| Water bodies | `water` |
| Green Vegetation Health | `vegetation-health` |

#### Responce

```json
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "Everything you need to analyzing Vegetation Health": {
        "machine_name": "vegetation-health",
        "name": "Vegetation Health",
        "description": "",
        "indice": {
            "name": "Normalized Difference Vegetation Index",
            "accr": "NDVI",
            "description": "The well known and widely used NDVI is a simple, but effective index for quantifying green vegetation. It normalizes green leaf scattering in Near Infra-red wavelengths with chlorophyll absorption in red wavelengths.\r\n\r\nThe value range of the NDVI is -1 to 1. Negative values of NDVI (values approaching -1) correspond to water. Values close to zero (-0.1 to 0.1) generally correspond to barren areas of rock, sand, or snow. Low, positive values represent shrub and grassland (approximately 0.2 to 0.4), while high values indicate temperate and tropical rainforests (values approaching 1). It is a good proxy for live green vegetation.",
            "is_NormalizedDifference": true,
            "calc": "(B08-B04)/(B08+B04)"
        },
        "satellite": {
            "name": "Sentinel-2",
            "accr": "S2",
            "operator": "European Space Agency"
        },
        "bands": [
            {
                "band": "B04",
                "description": "Red",
                "wavelength": "665",
                "resolution": "10"
            },
            {
                "band": "B08",
                "description": "Visible and Near Infrared (VNIR)",
                "wavelength": "842",
                "resolution": "10"
            }
        ],
        "files": {
            "0": {
                "Product ID": "S2A_MSIL2A_20210410T100021_N0300_R122_T33TVJ_20210410T115211",
                "Preview": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/T/VJ/2021/4/10/0/preview.jpg",
                "Date": "2021-04-10T10:08:30Z",
                "Cloud cover": 43.1,
                "B02": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/T/VJ/2021/4/S2A_33TVJ_20210410_0_L2A/B02.tif",
                "B03": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/T/VJ/2021/4/S2A_33TVJ_20210410_0_L2A/B03.tif",
                "B04": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/T/VJ/2021/4/S2A_33TVJ_20210410_0_L2A/B04.tif"
            },
            "1": {
                "Product ID": "S2A_MSIL2A_20210410T100021_N0300_R122_T33TWJ_20210410T115211",
                "Preview": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/T/WJ/2021/4/10/0/preview.jpg",
                "Date": "2021-04-10T10:08:26Z",
                "Cloud cover": 20.61,
                "B02": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/T/WJ/2021/4/S2A_33TWJ_20210410_0_L2A/B02.tif",
                "B03": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/T/WJ/2021/4/S2A_33TWJ_20210410_0_L2A/B03.tif",
                "B04": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/T/WJ/2021/4/S2A_33TWJ_20210410_0_L2A/B04.tif"
            },
            "2": {
                "Product ID": "S2A_MSIL2A_20210410T100021_N0300_R122_T33TUK_20210410T115211",
                "Preview": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/T/UK/2021/4/10/0/preview.jpg",
                "Date": "2021-04-10T10:08:20Z",
                "Cloud cover": 26.51,
                "B02": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/T/UK/2021/4/S2A_33TUK_20210410_0_L2A/B02.tif",
                "B03": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/T/UK/2021/4/S2A_33TUK_20210410_0_L2A/B03.tif",
                "B04": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/T/UK/2021/4/S2A_33TUK_20210410_0_L2A/B04.tif"
            },
            "3": {
                "Product ID": "S2A_MSIL2A_20210410T100021_N0300_R122_T33TUL_20210410T115211",
                "Preview": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/T/UL/2021/4/10/0/preview.jpg",
                "Date": "2021-04-10T10:08:05Z",
                "Cloud cover": 8.27,
                "B02": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/T/UL/2021/4/S2A_33TUL_20210410_0_L2A/B02.tif",
                "B03": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/T/UL/2021/4/S2A_33TUL_20210410_0_L2A/B03.tif",
                "B04": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/T/UL/2021/4/S2A_33TUL_20210410_0_L2A/B04.tif"
            }
        }
    }
}
```

## Funding

This project is funded by the [German Federal Ministry of Education and Research](http://bmbf.de)
and is part of the 9th round of the [Prototype Fund](http://prototypefund.de).

![Logo of Prototype Fund, Open Knowledge Foundation and the German Federal Ministry of Education and Research](/assets/funding-logos.png)
