import React from "react";
import Link from "next/link";
import Router from "next/router";

export default class Index extends React.Component {
  async userLogin(event) {
    event.preventDefault();
    const url = "/api/login";
    const response = await fetch(url, {
      body: JSON.stringify({
        username: event.target.username.value,
        password: event.target.password.value,
      }),
      headers: {
        "Content-Type": "application/json",
      },
      method: "POST",
    });
    const data = await response.json();
    console.log(data);

    if (data.status === "success") Router.push(data.redirect);
  }

  render() {
    return (
      <div>
        <h1>Authenticator App</h1>
        <form onSubmit={this.userLogin}>
          <input type="text" id="username" name="username" required />
          <br />
          <input type="password" id="password" name="password" required />
          <br />
          <button type="submit">Login</button>
        </form>
        <br />
        <Link href="/register">
          <a>Register</a>
        </Link>
      </div>
    );
  }
}
