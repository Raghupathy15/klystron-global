from odoo.http import request
from odoo import models, api, fields
from datetime import date
from dateutil.relativedelta import relativedelta

class ProjectReportXls(models.AbstractModel):
	_name = 'report.klystron_project.project_xlsx'
	_inherit = 'report.report_xlsx.abstract'

	def generate_xlsx_report(self, workbook, data, lines):
		active_id = self.env.context.get('active_id')
		wizard = self.env['wizard.project.report'].browse(int(active_id))
		# Formats
		worksheet = workbook.add_worksheet("Task Report")
		format1 = workbook.add_format({'font_size': 9, 'bold': True, 'bg_color': '86C6CD','align':'center'})
		format2 = workbook.add_format({'font_size': 9, 'bold': True, 'bg_color': '86C6CD','align':'left'})
		format3 = workbook.add_format({'font_size': 9,'align':'left'})
		format4 = workbook.add_format({'num_format': 'dd-mm-yyyy','align':'center','font_size': 9})
		format5 =workbook.add_format({'font_size': 9,'align':'center'})
		format6 =workbook.add_format({'font_size': 9,'align':'right'})
		format7 = workbook.add_format({'font_size': 9, 'bg_color': '#FFFFFF'})
		format8 =workbook.add_format({'font_size': 9,'align':'center','bg_color': 'EC3936'})
		# Heading
		worksheet.merge_range('A1:H1', wizard.name.name, format1)
		worksheet.write('A2',"Activity Name", format2)
		worksheet.write('B2',"Planned Start Date", format2)
		worksheet.write('C2',"Planned End date", format2)
		worksheet.write('D2',"Duration in Days", format2)
		worksheet.write('E2',"Actual Start date", format2)
		worksheet.write('F2',"Actual End date", format2)
		worksheet.write('G2',"Duration in Days", format2)
		worksheet.write('H2',"Variance(Difference in planned and actual days)", format2)
		# data/Values
		row = 2
		column = 0
		task = self.env['project.task'].sudo().search([('project_id','=',wizard.name.id)])
		for data in task:
			if data:
				duration=data.plan_date_end-data.plan_date_start
				duration1=data.actual_date_end-data.actual_date_start
				worksheet.write(row, column,data.name, format3)
				if data.parent_id:
					worksheet.write(row, column,data.name, format6)
				if data.plan_date_start:
					worksheet.write(row, column+1,data.plan_date_start, format4)
				if data.plan_date_end:
					worksheet.write(row, column+2,data.plan_date_end, format4)
					worksheet.write(row, column+3,duration, format5)
				if data.actual_date_start:
					worksheet.write(row, column+4,data.actual_date_start, format4)
				if data.actual_date_end:
					worksheet.write(row, column+5,data.actual_date_end, format4)
					worksheet.write(row, column+6,duration1, format5)
				if data.plan_date_start and data.actual_date_start:
					variance = data.actual_date_start - data.plan_date_start
					if variance.days <= 9:
						worksheet.write(row, column+7,variance, format5)
					if variance.days >= 10:
						worksheet.write(row, column+7,variance, format8)
				row += 1