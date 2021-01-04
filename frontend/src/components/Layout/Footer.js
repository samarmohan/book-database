import React from "react";

const Footer = () => {
	return (
		<>
			<footer style={footerStyles} className="m-3 footer text-muted">
				<div className="container">
					&copy; 2021 - Samar Mohan - Book Database v2.2.1
				</div>
			</footer>
		</>
	);
};

const footerStyles = {
	fontStyle: "italic",
};

export default Footer;
