import axios from "axios";
import React, { useState, useEffect } from "react";
import { render } from "react-dom";

const App = () => {
	const [bookResponses, setBookResponses] = useState([]);

	useEffect(() => {
		axios
			.get("https://glacial-forest-38809.herokuapp.com/api/books/")
			.then((res) => setBookResponses(res.data))
			.catch((err) => console.log(err));
	}, []);

	return (
		<div style={listStyle}>
			<h1>Book Responses</h1>
			{bookResponses.map((response) => (
				<p key={response.Title}>{response.Title}</p>
			))}
		</div>
	);
};

const listStyle = {
	textAlign: "center",
};

export default App;

render(<App />, document.getElementById("root"));
