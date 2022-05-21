class Address:
    def __init__(
            self, address_line_1, city, county, postcode, address_line_2=''):
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.county = county
        self.postcode = postcode
    
    def __repr__(self):
        return (
            f'Address(address_line_1={self.address_line_1},'
            f'address_line_2={self.address_line_2}, city={self.city},'
            f'county={self.county}, postcode={self.postcode})'
        )