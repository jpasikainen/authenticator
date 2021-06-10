import React from "react";
import Router from "next/router";

export default class Authenticate extends React.Component {
  state = {
    loggedIn: false,
  };

  async componentDidMount() {
    try {
      const url = "api/user";
      const response = await fetch(url);

      if (!response.ok) {
        throw Error(response.statusText);
      }

      const data = await response.json();
      if (data.username !== "") this.setState({ loggedIn: true });
      Router.push("/");
    } catch (error) {
      console.log(error);
    }
  }

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
    if (this.state.loggedIn)
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
    return <h1>You are already authenticated.</h1>;
  }
}
