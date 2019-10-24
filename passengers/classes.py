class SeatsHandler(object):

    __slots__ = ("_data_seats", "_ttl_passenger", "_pass_counter",
                 "passenger_seats")

    def __init__(self, data_seats, ttl_passenger):
        self._data_seats = data_seats
        self._ttl_passenger = ttl_passenger
        self._pass_counter = 0
        self.passenger_seats = []

    @staticmethod
    def get_ttl_seats(data_seats):
        """
        Get total available seats from _data_sets
        """
        return sum([seat[0]*seat[1] for seat in data_seats])

    @classmethod
    def is_valid_passenger(cls, data_seats, ttl_passengers):
        """
        Raised error if ttl passenger greater than available seats
        """
        available_seats = cls.get_ttl_seats(data_seats)
        if ttl_passengers > available_seats:
            raise ValueError(
                "Available seats only for {} passenger".format(available_seats))
        return True

    def get_max_row(self):
        max_row = 0
        for arr in self._data_seats:
            if arr[0] > max_row:
                max_row = arr[0]

        return max_row

    def handle_aisle_seat(self):
        """
        Aisle seat / First seat Handler

        Create seats model, assign seat and add `None` to not exists column
        """

        for row_check in range(1, self.get_max_row()+1):
            row_data = []
            for idx, arr in enumerate(self._data_seats):
                if row_check > arr[0]:
                    # row_data.append([None for blank_seat in range(arr[1])])
                    row_data.append([])
                    continue

                ndata = 1 if arr[1] <= 1 else 2
                if idx in [0, len(self._data_seats) - 1]:
                    ndata -= 1

                row_data.append(
                    [(new_data + 1 if new_data + 1 <= self._ttl_passenger else "")
                     for new_data in range(self._pass_counter, self._pass_counter+ndata)])
                self._pass_counter += ndata

            self.passenger_seats.append(row_data)

        return ndata

    def handle_window_seat(self):
        """
        Window seat / outer seat Handler
        """
        for row_check in range(self.get_max_row()):
            # check only first and last index of array
            for outer in [0, -1]:
                if self._data_seats[outer][0] >= (row_check + 1) and self._data_seats[outer][1] >= 1:
                    self._pass_counter += 1
                    self.passenger_seats[row_check][outer]\
                        .insert(outer if not outer else len(self.passenger_seats[row_check][outer]),
                                self._pass_counter if self._pass_counter <= self._ttl_passenger else "")

    def handle_middle_seat(self):
        """
        Middle seat / inner seat Handler
        """
        for row_check in range(self.get_max_row()):
            for idx, arr in enumerate(self._data_seats):
                if (row_check+1) > arr[0] or arr[1] <= 2:
                    continue

                # proceed if row exists and colum greater than 2
                ndata = arr[1] - 2
                for nvalue in range(ndata):
                    self._pass_counter += 1
                    self.passenger_seats[row_check][idx].insert(
                        nvalue+1, self._pass_counter if self._pass_counter <= self._ttl_passenger else "")

    def run(self):
        """
        Assign seat for passenger

        Assignment Order:
            - Aisle Seats
            - Window Seats
            - Middle Seats

        """
        # reset variables
        self._pass_counter = 0
        self.passenger_seats = []

        # Seats Assingment [aisle, window, middle]
        for do_assign in [self.handle_aisle_seat, self.handle_window_seat, self.handle_middle_seat]:
            do_assign()

        return self.passenger_seats
