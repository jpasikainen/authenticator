import React from "react";

export default class Authenticate extends React.Component {
  async authenticateUser(event) {
    event.preventDefault();
    const url = "/api/authenticate";
    const response = await fetch(url, {
      body: JSON.stringify({
        otp: event.target.otp.value,
      }),
      headers: {
        "Content-Type": "application/json",
      },
      method: "POST",
    });
    const data = await response.json();
    console.log(data);
  }

  render() {
    return (
      <div>
        <h1>Authentication</h1>
        <form onSubmit={this.authenticateUser}>
          <input
            type="number"
            id="otp"
            name="otp"
            min="111111"
            max="999999"
            required
          />
          <br />
          <button type="submit">Authenticate</button>
        </form>
      </div>
    );
  }
}
