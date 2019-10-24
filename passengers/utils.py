def is_valid_arrayd(data_arr, edimension):
    """
    Validate array dimensions

    : param data_arr: List<List<any>>: array data.
    : param edimension: number : Expected dimesions.
    """
    for arr in data_arr:
        if len(arr) != edimension:
            raise ValueError(
                "Array should be {} dimension of numbers".format(edimension))

        for value in arr:
            if value == 0:
                raise ValueError("0 is not allowed on Array")
