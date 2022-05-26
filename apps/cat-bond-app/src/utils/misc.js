export const ExtractPolygonCoordinatesBoundsFromFeatures = (feature) => {
  let coords = feature.geometry.coordinates[0];
  let res = [];
  for (let i = 0; i < coords.length; i++) {
    res.push({ lat: coords[i][1], lng: coords[i][0] });
  }
  return res;
};
