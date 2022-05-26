import { WebConfig } from "../../../../config/config";

export const routePostBondFormSponsorValidate = [
  process.env.REACT_APP_SVC_URL,
  WebConfig.bondForm_Sponsor_Validate_POST,
].join("/");

export const routePostBondFormSponsorMint = [
  process.env.REACT_APP_SVC_URL,
  WebConfig.bondForm_Sponsor_Mint_POST,
].join("/");
