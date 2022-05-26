import "./styles.scss";

import { Button, TextField } from "@material-ui/core";
import { observer } from "mobx-react";
import React from "react";

import PlaceholderDiv from "../../../dev/placeholder-div";

const BondForm = observer(({ bondFormStore }) => {
  return (
    <div className={"bond-form-container"}>
      <div className="left-container">
        <div>
          <h2>Bond Information</h2>
        </div>
        <div>
          <TextField
            id="standard-basic"
            label="$ETH Insured"
            variant="standard"
            onChange={bondFormStore.setInsuredSumInput}
          />
        </div>
        <div>
          <TextField
            id="standard-basic"
            label="$ETH Premium"
            variant="standard"
            onChange={bondFormStore.setPremiumInput}
          />
        </div>
        <div>
          <TextField
            id="standard-basic"
            label="Threshold"
            variant="standard"
            onChange={bondFormStore.setThresholdInput}
          />
        </div>
        <div>
          <TextField
            id="standard-basic"
            label="Expiry Time"
            variant="standard"
            onChange={bondFormStore.setExpiryTimeInput}
          />
        </div>
        <div>
          <Button
            variant="outlined"
            onClick={bondFormStore.handleValidateButtonOnClick}
          >
            Validate Bond
          </Button>
        </div>
      </div>

      <div className="right-container">
        <div>
          <PlaceholderDiv txt={bondFormStore.tileStatus} />
        </div>
        <div>
          <Button
            variant="contained"
            onClick={bondFormStore.handleMintButtonOnClick}
          >
            Mint Bond
          </Button>
        </div>
      </div>
    </div>
  );
});

export default BondForm;
