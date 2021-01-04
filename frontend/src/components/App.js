import axios from "axios";
import React, { useState, useEffect } from "react";
import { render } from "react-dom";

import NavBar from "./Layout/NavBar";
import Footer from "./Layout/Footer";

import Table from "./Home/Table";

const App = () => {
	const [bookResponses, setBookResponses] = useState([]);

	useEffect(() => {
		axios
			.get("https://glacial-forest-38809.herokuapp.com/api/books/")
			.then((res) => setBookResponses(res.data))
			.catch((err) => console.log(err));
	}, []);

	return (
		<>
			<NavBar />
			<div className="container" style={mainStyles}>
				<h1>Book Responses</h1>

				<Table bookResponse={bookResponses} />
			</div>
			<Footer />
		</>
	);
};

const mainStyles = {
    textAlign: "center",
    fontFamily: "merriweather"
};

export default App;

render(<App />, document.getElementById("root"));
