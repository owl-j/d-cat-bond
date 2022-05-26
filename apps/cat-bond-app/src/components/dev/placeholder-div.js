import "./placeholder-div.scss";

import React, { Component } from "react";

class PlaceHolderDiv extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div className={"placeholder-div flex-row-centered"}>
        <div className={"placeholder-div__txt flex-column-centered"}>
          {this.props.txt}
        </div>
      </div>
    );
  }
}

export default PlaceHolderDiv;
