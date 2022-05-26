import "bootstrap/dist/css/bootstrap.css";

import "./common.scss";

import React from "react";
import { Route, Routes, useLocation } from "react-router-dom";

import { StatefulSponsorBond } from "./sponsor-bond/stateful-sponsor-bond";

function App() {
  const location = useLocation();

  return (
    <Routes location={location}>
      <Route
        path="/"
        element={
          <div>
            <StatefulSponsorBond />
          </div>
        }
      />
    </Routes>
  );
}

export default App;
