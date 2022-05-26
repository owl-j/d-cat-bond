import { observer } from "mobx-react";

import sponsorMapStore from "./store/sponsor-map-store";
import { ReactLeafletMap } from "./UI/sponsor-map";

const StatefulSponsorMap = observer(({ sponsorMapStore }) => {
  return <ReactLeafletMap sponsorMapStore={sponsorMapStore} />;
});

export default StatefulSponsorMap;
