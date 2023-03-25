import React, { useState } from "react";
import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import Tooltip from "react-bootstrap/Tooltip";
export const URLForm = () => {
  const [longURL, setLongURL] = useState("");
  const [shortURL, setShortURL] = useState("");

  const getShortURL = () => {
    fetch("/create_short_url/" + longURL)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setShortURL(data.response);
      });
    console.log(shortURL);
  };
  const copyToClipBoard = () => {
    navigator.clipboard.writeText("localhost:5000/" + shortURL);
  };

  return (
    <form autoComplete="off">
      <h3>Vinberly's URLShortner!</h3>
      <div className="input-group-append">
        <label>Enter Your Long URL:</label>
        <input
          onChange={(e) => setLongURL(e.target.value)}
          value={longURL}
          placeholder="https://www.google.com"
        />
        <button
          type="button"
          onClick={getShortURL}
          className="btn btn-outline-secondary"
        >
          Submit
        </button>
      </div>

      {shortURL === "" ? (
        <div></div>
      ) : (
        <div className="generatedurl">
          <span>Your Short URL is: </span>
          <div className="input-group mb-3">
            <input
              disabled
              type="text"
              value={"localhost:5000/" + shortURL}
              className="form-control"
              placeholder="Recipient's username"
              aria-label="Recipient's username"
              aria-describedby="basic-addon2"
            />
            <div className="input-group-append">
              <OverlayTrigger
                key={"top"}
                placement={"top"}
                overlay={<Tooltip>Copied</Tooltip>}
              >
                <button
                  onClick={() => copyToClipBoard()}
                  data-toggle="tooltip"
                  data-placement="top"
                  title="Tooltip on top"
                  className="btn btn-outline-secondary"
                  type="button"
                >
                  Copy
                </button>
              </OverlayTrigger>
            </div>
          </div>
        </div>
      )}
    </form>
  );
};
// fetch("/data").then((res) =>
//   res.json().then((data) => {
//     console.log(data);
//   })
// );
export default URLForm;
