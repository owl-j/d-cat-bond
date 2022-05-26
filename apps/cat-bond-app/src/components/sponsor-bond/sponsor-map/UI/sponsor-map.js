import "leaflet/dist/leaflet.css";

import L from "leaflet";
import { observer } from "mobx-react";
import React from "react";
import {
  FeatureGroup,
  LayersControl,
  MapContainer,
  Polygon,
  TileLayer,
} from "react-leaflet";
import { EditControl } from "react-leaflet-draw";

import { ExtractPolygonCoordinatesBoundsFromFeatures } from "../../../../utils/misc";

delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.0.0/images/marker-icon.png",
  iconUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.0.0/images/marker-icon.png",
  shadowUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.0.0/images/marker-shadow.png",
});

const { BaseLayer } = LayersControl;

export const ReactLeafletMap = observer(({ sponsorMapStore }) => {
  let _editableFG = null;
  let _onFeatureGroupReady = (reactFeatureGroupRef) => {
    _editableFG = reactFeatureGroupRef;
  };

  return (
    <MapContainer
      key={JSON.stringify(sponsorMapStore.mapAppearance.init.center)}
      center={sponsorMapStore.mapAppearance.init.center}
      zoom={sponsorMapStore.mapAppearance.init.zoom}
      scrollWheelZoom={sponsorMapStore.mapAppearance.init.scrollWheelZoom}
      zoomControl={sponsorMapStore.mapAppearance.init.zoomControl}
      style={{ height: "80vh", width: "100%" }}
    >
      <LayersControl>
        <BaseLayer checked name={"Esri_WorldImagery"}>
          <TileLayer
            url={
              "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
            }
            attribution={
              "Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community"
            }
          />
        </BaseLayer>
        <BaseLayer name={"Dark"}>
          <TileLayer
            url={sponsorMapStore.mapAppearance.tileLayer.url}
            attribution={sponsorMapStore.mapAppearance.tileLayer.attribution}
          />
        </BaseLayer>
        <BaseLayer name={"Stamen_Terrain"}>
          <TileLayer
            url={
              "https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png"
            }
            attribution={
              'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }
            subdomains={"abcd"}
            minZoom={0}
            maxZoom={18}
          />
        </BaseLayer>
      </LayersControl>
      <FeatureGroup
        ref={(reactFeatureGroupRef) => {
          _onFeatureGroupReady(reactFeatureGroupRef);
        }}
      >
        <EditControl
          position="topright"
          onEdited={sponsorMapStore.actions.onEdited}
          onCreated={sponsorMapStore.actions.onCreated}
          onDeleted={sponsorMapStore.actions.onDeleted}
          onMounted={sponsorMapStore.actions.onMounted}
          onEditStart={sponsorMapStore.actions.onEditStart}
          onEditStop={sponsorMapStore.actions.onEditStop}
          onDeleteStart={sponsorMapStore.actions.onDeleteStart}
          onDeleteStop={sponsorMapStore.actions.onDeleteStop}
          draw={{
            rectangle: false,
          }}
        />
      </FeatureGroup>
      {sponsorMapStore.polygons.map((feature, i) => {
        return (
          <Polygon
            key={i}
            positions={ExtractPolygonCoordinatesBoundsFromFeatures(feature)}
            pathOptions={{
              color: feature.color,
              fillColor: feature.color,
            }}
            eventHandlers={{
              click: () => {
                console.log("polygon clicked");
              },
            }}
          />
        );
      })}
    </MapContainer>
  );
});
