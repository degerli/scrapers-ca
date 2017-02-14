from utils import CanadianJurisdiction
from pupa.scrape import Organization


class Whitby(CanadianJurisdiction):
    classification = 'legislature'
    division_id = 'ocd-division/country:ca/csd:3518009'
    division_name = 'Whitby'
    name = 'Whitby Town Council'
    url = 'http://www.whitby.ca'

    def get_organizations(self):
        organization = Organization(self.name, classification=self.classification)

        organization.add_post(role='Mayor', label=self.division_name, division_id=self.division_id)
        for seat_number in range(1, 4):
            organization.add_post(role='Regional Councillor', label='Whitby (seat {})'.format(seat_number), division_id=self.division_id)
        for ward_number, ward_name in enumerate(('North', 'West', 'Centre', 'East'), 1):
            organization.add_post(role='Councillor', label='{} Ward'.format(ward_name), division_id='{}/ward:{}'.format(self.division_id, ward_number))

        yield organization
