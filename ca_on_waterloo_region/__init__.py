from __future__ import unicode_literals
from utils import CanadianJurisdiction
from pupa.scrape import Organization


class Waterloo(CanadianJurisdiction):
    classification = 'legislature'
    division_id = 'ocd-division/country:ca/cd:3530'
    division_name = 'Waterloo'
    name = 'Waterloo Regional Council'
    url = 'http://www.regionofwaterloo.ca'

    def get_organizations(self):
        organization = Organization(self.name, classification=self.classification)

        organization.add_post(role='Chair', label=self.division_name, division_id=self.division_id)
        organization.add_post(role='Regional Councillor', label='Cambridge', division_id='ocd-division/country:ca/csd:3530010')
        organization.add_post(role='Regional Councillor', label='Kitchener', division_id='ocd-division/country:ca/csd:3530013')
        organization.add_post(role='Regional Councillor', label='Waterloo', division_id='ocd-division/country:ca/csd:3530016')
        organization.add_post(role='Regional Councillor', label='North Dumfries', division_id='ocd-division/country:ca/csd:3530004')
        organization.add_post(role='Regional Councillor', label='Wellesley', division_id='ocd-division/country:ca/csd:3530027')
        organization.add_post(role='Regional Councillor', label='Wilmot', division_id='ocd-division/country:ca/csd:3530020')
        organization.add_post(role='Regional Councillor', label='Woolwich', division_id='ocd-division/country:ca/csd:3530035')
        for seat_number in range(1, 3):
            organization.add_post(role='Regional Councillor', label='Cambridge (seat {})'.format(seat_number), division_id='ocd-division/country:ca/csd:3530010')
        for seat_number in range(1, 5):
            organization.add_post(role='Regional Councillor', label='Kitchener (seat {})'.format(seat_number), division_id='ocd-division/country:ca/csd:3530013')
        for seat_number in range(1, 3):
            organization.add_post(role='Regional Councillor', label='Waterloo (seat {})'.format(seat_number), division_id='ocd-division/country:ca/csd:3530016')

        yield organization
