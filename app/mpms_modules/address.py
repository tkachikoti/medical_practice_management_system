class Address:
    def __init__(
            self, address_line_1, city, county, postcode, address_line_2=''):
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.county = county
        self.postcode = postcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)