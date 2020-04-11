export const isSuccessResponse = (response) => {
  // helper method to validate success response
  if (
    response &&
    response !== null &&
    response.hasOwnProperty("status") &&
    (response.status > 199 || response.status < 400)
  ) {
    return true;
  } else {
    return false;
  }
};

export const isNonEmptyArray = (array) => {
  // cheks if given input is valid array instance and not empty

  if (array && Array.isArray(array) && array.length) {
    return true;
  } else return false;
};
