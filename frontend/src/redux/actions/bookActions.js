import axios from "axios";
import {
	GET_BOOKS,
	GET_BOOK,
	ADD_BOOK,
	UPDATE_BOOK,
	DELETE_BOOK,
} from "../types";

export const getBooks = () => (dispatch) => {
	axios
		.get("https://glacial-forest-38809.herokuapp.com/api/books/")
		.then((res) => {
			dispatch({
				type: GET_BOOKS,
				payload: res.data,
			});
		})
		.catch((err) => console.log(err));
};
