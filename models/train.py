from odoo import models, fields, api
from datetime import timedelta, datetime, date

# class TrainCity(models.Model):
#     _name = "train.city"
#     _description = "Kota Kereta"

#     name = fields.Char(string = "Nama Kota", required = True)
#     code = fields.Char(string = "Kode Kota")

# class TrainStation(models.Model):
#     _name = "train.station"
#     _description = "Stasiun Kereta"

#     code = fields.Char(string = "Kode Stasiun")
#     name = fields.Char(string = "Nama Stasiun", required = True)
#     city_id = fields.Many2one('train.city', string = "Nama Kota", required = True, ondelete = "cascade")
#     address = fields.Text(string = "Alamat")

class TrainTrain(models.Model):
    _name = "train.train"
    _description = "Kereta"

    name = fields.Char(string = "Nama Kereta", required = True)
    code = fields.Char(string = "Kode Kereta")
    capacity = fields.Integer(string = "Kapasitas")
    state = fields.Selection([('ready', 'Ready'),('not_ready', 'Not Ready'),('maintenance', 'Maintenance')], string = "Status", default = "ready")
    active = fields.Boolean(string = "Aktif", readonly = True, compute = 'active_status')
    # schedule_line = fields.One2many('train.schedule', 'train_id', string = "Jadwal")

    @api.depends('state')
    def active_status(self):
        for train in self:
            if train.state == "ready":
                train.active = True
            else:
                train.active = False

# class TrainSchedule(models.Model):
#     _name = "train.schedule"
#     _description = "Jadwal Kereta"

#     code = fields.Char(string = "Kode Jadwal", readonly = True)
#     origin = fields.Many2one('train.station', string = "Stasiun Asal", ondelete = 'cascade')
#     destination = fields.Many2one('train.station', string = "Stasiun Tujuan", ondelete =' cascade')
#     schedule_time = fields.Date(string = "Waktu Berangkat")
#     duration = fields.Float(string = "Durasi", default = 1)
#     arrival_time = fields.Date(string = "Waktu Sampai", compute = "get_arrival_time", inverse = "set_arrival_time", store = True)
#     train_id = fields.Many2one('train.train', string = "Nama Kereta", required = True, ondelete = "cascade")
#     capacity = fields.Integer(string = "Kapasitas", related = 'train_id.capacity')

#     @api.depends('schedule_time', 'duration')
#     def get_arrival_time(self):
#         for schedule in self:
#             if not schedule.schedule_time:
#                 schedule.arrival_time = schedule.arrival_time
#                 continue
#             start = fields.Date.from_string(schedule.schedule_time)
#             schedule.arrival_time = start + timedelta(hours=schedule.duration)

#     def set_arrival_time(self):
#         for schedule in self:
#             if not (schedule.schedule_time and schedule.arrival_time):
#                 continue

#             schedule_time = fields.Datetime.from_string(schedule.schedule_time)
#             arrival_time = fields.Datetime.from_string(schedule.arrival_time)
#             schedule.duration = (arrival_time - schedule_time).hours + 1