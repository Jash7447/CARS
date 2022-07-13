from odoo import api, fields, models


class CarCheckout(models.Model):
    _name = "car.checkout"
    _rec_name = "customer_name_1"

    @api.onchange('customer_name_1', 'booking_id')
    def car_checkout_populate(self):
        for rec in self:
            self.customer_email = rec.booking_id.cus_email
            self.customer_city = rec.booking_id.cus_city
            self.customer_phone = rec.booking_id.cus_phone
            self.customer_age = rec.booking_id.cus_age
            self.fair = rec.booking_id.total_cost
            self.start_dt1 = rec.booking_id.ride_start_dt
            self.time_slot = rec.booking_id.checkout_time_slots
            self.end_date1 = rec.booking_id.ride_end_date
            self.car2 = rec.booking_id.car1

    customer_name_1 = fields.Many2one("car.rental", string="Costumer name")
    customer_email = fields.Char(string="Email")
    customer_phone = fields.Char(string="Phone")
    customer_age = fields.Integer(string="Age")
    customer_city = fields.Selection(
        [('Ahmedabad', 'Ahmedabad'), ('Bangalore', 'Bangalore'), ('Mumbai', 'Mumbai'), ('Surat', 'Surat')],
        string="city",
        help="customer's city")
    start_dt1 = fields.Datetime(string="Check-out date")
    end_date1 = fields.Date(string="Check-in date")
    car2 = fields.Many2one("car.data", string="Car")
    fair = fields.Integer(string="fair", help="Total cost without tax.")
    time_slot = fields.Many2one("checkout.slots", string="Checkout time slot")
    driver = fields.Many2one("staff.data", domain=[("role", "=", "driver")])
    booking_id = fields.Many2one("book.ride", string="booking id", help="fetches id from book_ride")
    # booking_id = fields.Many2one("book.ride", string="fetches id from book_ride",
    #                              domain=[("cus_name", "=", customer_name_1)])
    checkout_status = fields.Selection(
        [('submitted', 'Submitted'), ('assigned', 'Assigned'), ('checked_in', "Checked In")], default='submitted')

    @api.model
    def create(self, values):
        print('create values >>', values)
        rtn = super(CarCheckout, self).create(values)
        # print('name>>>', values['customer_name'])
        return rtn

    def action_assigned(self):
        self.checkout_status = 'assigned'

    def action_check_in(self):
        self.checkout_status = 'checked_in'
