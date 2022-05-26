import axios from "axios";

import {
  routePostBondFormSponsorMint,
  routePostBondFormSponsorValidate,
} from "./routes";

export const GetUserIpAddress = async () => {
  let ipAddress = "";
  await axios.get("https://jsonip.com/").then(function (response) {
    ipAddress = response.data.ip;
  });
  return ipAddress;
};

export const PostBondFormSponsorValidate = async (
  premium,
  insuredSum,
  expiryTime,
  threshold,
  polygons
) => {
  let errorOccurred = false;

  let route = routePostBondFormSponsorValidate;

  try {
    let response = await axios.post(route, {
      premium: premium,
      insuredSum: insuredSum,
      expiryTime: expiryTime,
      threshold: threshold,
      polygons: polygons,
    });
    if (response.status !== 200) {
      errorOccurred = true;
    } else {
      return response.data;
    }
  } catch (e) {
    errorOccurred = true;
  }
  return errorOccurred;
};

export const PostBondFormSponsorMint = async (
  premium,
  insuredSum,
  expiryTime,
  threshold,
  polygons
) => {
  let errorOccurred = false;

  let route = routePostBondFormSponsorMint;

  try {
    let response = await axios.post(route, {
      premium: premium,
      insuredSum: insuredSum,
      expiryTime: expiryTime,
      threshold: threshold,
      polygons: polygons,
    });
    if (response.status !== 200) {
      errorOccurred = true;
    } else {
      return response.data;
    }
  } catch (e) {
    errorOccurred = true;
  }
  return errorOccurred;
};
