import {
	GET_BOOKS,
	GET_BOOK,
	ADD_BOOK,
	UPDATE_BOOK,
	DELETE_BOOK,
} from "../types";

const initialState = {
	books: [],
};

export default (state = initialState, action) => {
	switch (action.type) {
		case GET_BOOKS:
			return {
				...state,
				books: action.payload,
			};
		default:
			return state;
	}
};
