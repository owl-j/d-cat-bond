import { polygon } from "leaflet/dist/leaflet-src.esm";
import { makeAutoObservable } from "mobx";

import { MapStyles } from "../../config/config";
import {
  PostBondFormSponsorMint,
  PostBondFormSponsorValidate,
} from "./bond-form/backend-support/api";

class SponsorBondStore {
  // ---------- SPONSOR-FORM ----------
  constructor() {
    makeAutoObservable(this);
  }

  // inputs
  premiumInput = ""; // Amount of premium in Ether
  insuredSumInput = ""; // Amount to insure in Ether (for the entire area)
  expiryTimeInput = ""; //Expiry time
  offerTimeInput = "";
  thresholdInput = ""; // Integer Threshold value

  // output
  tileStatus = "noTileStatus";
  tileAddresses = "";
  // --------- reducers ---------

  setPremiumInput = (event) => {
    this.premiumInput = event.target.value;
    console.log(this.premiumInput);
  };
  setInsuredSumInput = (event) => {
    this.insuredSumInput = event.target.value;
    console.log(this.insuredSumInput);
  };
  setExpiryTimeInput = (event) => {
    this.expiryTimeInput = event.target.value;
    console.log(this.expiryTimeInput);
  };
  setThresholdInput = (event) => {
    this.thresholdInput = event.target.value;
    console.log(this.thresholdInput);
  };

  handleValidateButtonOnClick = async () => {
    let errorOnSubmitOccurred = await PostBondFormSponsorValidate(
      this.premiumInput,
      this.insuredSumInput,
      this.expiryTimeInput,
      this.thresholdInput,
      this.polygons
    );
    this.tileStatus = errorOnSubmitOccurred.toString();
  };
  handleMintButtonOnClick = async () => {
    let errorOnSubmitOccurred = await PostBondFormSponsorMint(
      this.premiumInput,
      this.insuredSumInput,
      this.expiryTimeInput,
      this.thresholdInput,
      this.polygons
    );
    this.tileStatus = this.polygons.toString();
    console.log(this.polygons);
  };

  // ---------- SPONSOR-MAP ----------

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
const sponsorBondStore = new SponsorBondStore();

export default sponsorBondStore;
