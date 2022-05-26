import { observer } from "mobx-react";

import BondForm from "./UI/bond-form";

const StatefulBondForm = observer(({ bondFormStore }) => {
  return <BondForm bondFormStore={bondFormStore} />;
});

export default StatefulBondForm;
