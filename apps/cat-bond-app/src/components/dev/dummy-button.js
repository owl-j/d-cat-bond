const toBeTriggered = async () => {
  // test codes here
};

export const DummyButton = () => (
  <button
    onClick={toBeTriggered}
    style={{
      color: "#000000",
      backgroundColor: "#ffffff",
      height: "100px",
      width: "300px",
    }}
  >
    DummyButton
  </button>
);
