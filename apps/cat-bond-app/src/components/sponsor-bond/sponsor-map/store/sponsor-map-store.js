import { makeAutoObservable, runInAction } from "mobx";

import { MapStyles } from "../../../../config/config";

class SponsorMapStore {
  constructor() {
    makeAutoObservable(this);
  }

  // ---------- store states ----------

  // the map
  mapAppearance = {
    init: {
      center: [-35.28, 149.12], // Canberra location
      zoom: 13,
      scrollWheelZoom: true,
      zoomControl: true,
      editControlPosition: "topright",
    },
    tileLayer: MapStyles.dark,
  };

  // polygons displayed on the map
  polygons = [];

  onEdited = () => {};
  onCreated = (e) => {
    console.log(JSON.stringify(e.layer.editing.latlngs));
  };
  onDeleted = () => {};
  onMounted = () => {};
  onEditStart = () => {};
  onEditStop = () => {};
  onDeleteStart = () => {};
  onDeleteStop = () => {};

  actions = {
    onEdited: this.onEdited,
    onCreated: this.onCreated,
    onDeleted: this.onDeleted,
    onMounted: this.onMounted,
    onEditStart: this.onEditStart,
    onEditStop: this.onEditStop,
    onDeleteStart: this.onDeleteStart,
    onDeleteStop: this.onDeleteStop,
  };
}

const sponsorMapStore = new SponsorMapStore();

export default sponsorMapStore;
