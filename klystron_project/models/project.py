# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class Project(models.Model):
	_inherit = 'project.project'

	date_start = fields.Date(string="Start Date")
	date_end = fields.Date(string="End Date")

	@api.multi
	@api.constrains('date_start','date_end')
	def constrains(self):
		if self.date_start > self.date_end:
			raise ValidationError('"Start Date" should be less than "End Date" date !..')

class Task(models.Model):
	_inherit = "project.task"

	plan_date_start = fields.Date(string="Planned Start Date")
	plan_date_end = fields.Date(string="Planned End Date")
	actual_date_start = fields.Date(string="Actual Start Date")
	actual_date_end = fields.Date(string="Actual End Date")
	sequence = fields.Char( 'Sequence No', readonly=True,
				default=lambda self: self.env['ir.sequence'].next_by_code('task.sequence'))

	@api.multi
	@api.constrains('plan_date_start','plan_date_end','actual_date_start','actual_date_end')
	def constrains(self):
		if self.plan_date_start > self.plan_date_end:
			raise ValidationError('"Planned Start Date" should be less than "Planned End Date" date !..')
		if self.actual_date_start > self.actual_date_end:
			raise ValidationError('"Actual Start Date" should be less than "Actual End Date" date !..')
