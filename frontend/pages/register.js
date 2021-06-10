import React from "react";
import Link from "next/link";
import QRCode from "qrcode.react";

export default class Index extends React.Component {
  constructor(props) {
    super(props);
    this.state = { secret: "" };
    this.userRegister = this.userRegister.bind(this);
  }

  async userRegister(event) {
    event.preventDefault();
    const url = "/api/register";
    const response = await fetch(url, {
      body: JSON.stringify({
        username: event.target.username.value,
        email: event.target.email.value,
        password: event.target.password.value,
      }),
      headers: {
        "Content-Type": "application/json",
      },
      method: "POST",
    });
    const data = await response.json();
    console.log(data);

    if (data.status === "success") {
      console.log(data.secret);
      this.setState({ secret: String(data.secret) });
    }
  }

  render() {
    if (this.state.secret !== "") {
      return <QRCode value={this.state.secret} />;
    }

    return (
      <div>
        <h1>Register</h1>
        <form onSubmit={this.userRegister}>
          <input type="text" id="username" name="username" required />
          <br />
          <input type="text" id="email" name="email" required />
          <br />
          <input type="password" id="password" name="password" required />
          <br />
          <button type="submit">Register</button>
        </form>
        <br />
        <Link href="/login">
          <a>login</a>
        </Link>
      </div>
    );
  }
}
