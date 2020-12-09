# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ProjectReportButton(models.TransientModel):
	_name = 'wizard.project.report'

	name = fields.Many2one('project.project',string='Project',required=True)

	@api.multi
	def print_project_report_xls(self):
		data = {
			'ids': self.ids,
			'model': self._name,
		}
		return self.env.ref('klystron_project.project_xlsx').report_action(self, data=data)
