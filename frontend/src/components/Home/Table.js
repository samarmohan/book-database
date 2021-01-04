import React from "react";

const Table = (props) => {
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
				{props.bookResponse.map((br) => (
					<tr key={br.Title}>
						<td>{br.Title}</td>
						<td>{br.Author}</td>
						<td>{br.Rating}</td>
						<td>{br.Name}</td>
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

export default Table;
