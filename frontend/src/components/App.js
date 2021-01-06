import axios from "axios";
import React, { useState, useEffect } from "react";
import { render } from "react-dom";

import { Provider } from "react-redux";

import store from "../redux/store/";

import NavBar from "./Layout/NavBar";
import Footer from "./Layout/Footer";

import Books from "./Books/Books";

const App = () => {
	return (
		<>
			<Provider store={store}>
				<NavBar />
				<div className="container" style={mainStyles}>
					<h1>Book Entries</h1>

					<Books />
				</div>
				<Footer />
			</Provider>
		</>
	);
};

const mainStyles = {
	textAlign: "center",
	fontFamily: "merriweather",
};

export default App;

render(<App />, document.getElementById("root"));
