import React, { useEffect } from "react";
import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import Tooltip from "react-bootstrap/Tooltip";

class Form extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      longURL: "",
      preferedAlias: "",
      generatedURL: "",
      loading: false,
      errors: [],
      errorMessage: {},
      toolTipMessage: "Copy To Clip Board",
    };
  }

  //When the user clicks submit, this will be called
  onSubmit = async (event) => {
    event.preventDefault(); //Prevents the page from reloading when submit is clicked
    this.setState({
      loading: true,
      generatedURL: "",
    });

    // Validate the input the user has sumbitted
    var isFormValid = await this.validateInput();
    if (!isFormValid) {
      return;
    }
  };

  //Checks if feild has an error
  hasError = (key) => {
    return this.state.errors.indexOf(key) !== -1;
  };

  //Save the content of the form as the user is typing!
  handleChange = (e) => {
    const { id, value } = e.target;
    this.setState((prevState) => ({
      ...prevState,
      [id]: value,
    }));
  };

  validateInput = async () => {
    var errors = [];
    var errorMessages = this.state.errorMessage;

    //Validate Long URL
    if (this.state.longURL.length === 0) {
      errors.push("longURL");
      errorMessages["longURL"] = "Please enter your URL!";
    }

    this.setState({
      errors: errors,
      errorMessages: errorMessages,
      loading: false,
    });

    if (errors.length > 0) {
      return false;
    }

    return true;
  };

  copyToClipBoard = () => {
    navigator.clipboard.writeText(this.state.generatedURL);
    this.setState({
      toolTipMessage: "Copied!",
    });
  };

  render() {
    return (
      <div className="container">
        <form autoComplete="off">
          <h3>Vince & Kimberly URLShortner!</h3>

          <div className="form-group">
            <label>Enter Your Long URL</label>
            <input
              id="longURL"
              onChange={this.handleChange}
              value={this.state.longURL}
              type="url"
              required
              className={
                this.hasError("longURL")
                  ? "form-control is-invalid"
                  : "form-control"
              }
              placeholder="https://www.google.com"
            />
          </div>
          <div
            className={
              this.hasError("longURL") ? "text-danger" : "visually-hidden"
            }
          >
            {this.state.errorMessage.longURL}
          </div>

          <div className="form-group">
            <label htmlFor="basic-url">Your Short URL</label>
            <div className="input-group mb-3">
              <div className="input-group-prepend">
                <span className="input-group-text">vincekimdomain.com/</span>
              </div>
              <input
                id="preferedAlias"
                onChange={this.handleChange}
                value={this.state.preferedAlias}
                className={
                  this.hasError("preferedAlias")
                    ? "form-control is-invalid"
                    : "form-control"
                }
                type="text"
                placeholder="AoqXuq"
              />
            </div>
            <div
              className={
                this.hasError("suggestedAlias")
                  ? "text-danger"
                  : "visually-hidden"
              }
            >
              {this.state.errorMessage.suggestedAlias}
            </div>
          </div>

          <button
            className="btn btn-primary"
            ll
            type="button"
            onClick={this.onSubmit}
          >
            {this.state.loading ? (
              <div>
                <span
                  className="spinner-border spinner-border-sm"
                  role="status"
                  aria-hidden="true"
                ></span>
              </div>
            ) : (
              <div>
                <span
                  className="visually-hidden spinner-border spinner-border-sm"
                  role="status"
                  aria-hidden="true"
                ></span>
                <span>Shorten It!</span>
              </div>
            )}
          </button>

          {this.state.generatedURL === "" ? (
            <div></div>
          ) : (
            <div className="generatedurl">
              <span>Your generated URL is: </span>
              <div className="input-group mb-3">
                <input
                  disabled
                  type="text"
                  value={this.state.generatedURL}
                  className="form-control"
                  placeholder="Recipient's username"
                  aria-label="Recipient's username"
                  aria-describedby="basic-addon2"
                />
                <div className="input-group-append">
                  <OverlayTrigger
                    key={"top"}
                    placement={"top"}
                    overlay={
                      <Tooltip id={`tooltip-${"top"}`}>
                        {this.state.toolTipMessage}
                      </Tooltip>
                    }
                  >
                    <button
                      onClick={() => this.copyToClipBoard()}
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
      </div>
    );
  }
}

export default Form;
