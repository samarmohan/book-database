import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import { getBooks } from "../../redux/actions/bookActions";

const Books = () => {
	const books = useSelector((state) => state.books.books);
	const dispatch = useDispatch();

	useEffect(() => {
		dispatch(getBooks());
	}, []);

	return (
		<table className="table table-striped table-bordered table-hover table-dark">
			<thead>
				<tr>
					<th>Title</th>
					<th>Author</th>
					<th>Rating</th>
					<th>Submitted by</th>
					<th>Actions</th>
				</tr>
			</thead>
			<tbody>
				{books.map((eachBook) => (
					<tr key={eachBook.Title}>
						<td>{eachBook.Title}</td>
						<td>{eachBook.Author}</td>
						<td>{eachBook.Rating}</td>
						<td>{eachBook.Name}</td>
						<td>
							<a
								className="btn btn-danger btn-sm m-1"
								href="{{ br.Title }}/update"
								role="button"
							>
								Update
							</a>

							<a
								href="{{ br.Title }}/detail"
								className="btn btn-info btn-sm"
							>
								Details
							</a>
						</td>
					</tr>
				))}
			</tbody>
		</table>
	);
};

export default Books;
