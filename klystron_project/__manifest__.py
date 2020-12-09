
{
    'name': 'Klystron Project',
    'version': '13',
    'summary': 'Project Custom Module',
    'description': """Option to generate project status report.""",
    'category': 'project',
    'author': 'Raghu',
    'depends': ['project','report_xlsx'],
    'data': [
            'views/project_views.xml',
            'data/ir_sequence_data.xml',
            'wizard/project_report_wizard_view.xml',
            'views/project_report.xml'
             ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
