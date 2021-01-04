import React from "react";

const NavBar = () => {
	return (
		<>
			<nav className="navbar navbar-expand-lg navbar-dark bg-dark">
				<a className="navbar-brand" href="/">
					Book Database Home
				</a>
				<button
					aria-controls="navbarNav"
					aria-expanded="false"
					aria-label="Toggle navigation"
					className="navbar-toggler"
					data-target="#navbarNav"
					data-toggle="collapse"
					type="button"
				>
					<span className="navbar-toggler-icon"></span>
				</button>
				<div className="collapse navbar-collapse" id="navbarNav">
					<ul className="navbar-nav">
						<li className="nav-item active">
							<a className="nav-link" href="add-book/">
								Create Book
								<span className="sr-only">(current)</span>
							</a>
						</li>
						<li className="nav-item active">
							<a
								className="nav-link"
								target="blank"
								href="https://www.github.com/samarmohan/book-database"
							>
								GitHub<span className="sr-only">(current)</span>
							</a>
						</li>
					</ul>
				</div>
			</nav>
		</>
	);
};

export default NavBar;
