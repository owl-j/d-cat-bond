export const MapStyles = {
  dark: {
    url: "https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}{r}.png",
    attribution:
      '&copy;<a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>&copy; <a href="http://cartodb.com/attributions">CartoDB</a>',
  },
  Esri_WorldTopoMap: {
    url: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}",
    attribution:
      "Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, TomTom, Intermap, iPC, USGS, FAO, NPS, NRCAN, GeoBase, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), and the GIS User Community",
  },
  USGS_USTopo: {
    url: "https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}",
    attribution:
      'Tiles courtesy of the <a href="https://usgs.gov/">U.S. Geological Survey</a>',
  },
  Stamen_Terrain: {
    url: "https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png",
    attribution:
      'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  },
};

export const WebConfig = {
  bondForm_Sponsor_Validate_POST: "cat-bond-server-api/tiles-validation",
  bondForm_Sponsor_Mint_POST: "cat-bond-server-api/tiles-sensors-observation",
};
