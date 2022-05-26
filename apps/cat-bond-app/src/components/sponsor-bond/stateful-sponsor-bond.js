import StatefulBondForm from "./bond-form/stateful-bond-form";
import sponsorBondStore from "./sponsor-bond-store";
import { ReactLeafletMap } from "./sponsor-map/UI/sponsor-map";

export const StatefulSponsorBond = () => {
  return (
    <div>
      <ReactLeafletMap sponsorMapStore={sponsorBondStore} />
      <StatefulBondForm bondFormStore={sponsorBondStore} />
    </div>
  );
};
