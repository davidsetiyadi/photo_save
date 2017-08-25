from datetime import datetime, timedelta
import time
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import openerp.addons.decimal_precision as dp
from openerp import workflow



class photo_save_wizard(osv.osv_memory):
	_name = 'photo.save.wizard'
	_description = 'Photo Save'

	# _columns = {
	# 	'name': fields.char('Description'),
	# 	'holiday_status_id': fields.many2one('hr.holidays.status','Leaves type'),
	# 	'duration':fields.float('Duration'),
	# 	'notes':fields.text('Notes'),
	# }   
	# _defaults = {
		# 'date_start': lambda *a: time.strftime('%Y-%m-%d'),
		# 'date_end': lambda *a: time.strftime('%Y-%m-%d'),
	# }

	def button_generate(self, cr, uid, ids, context=None):
		"""
		 To get the date and print the report
		 @param self: The object pointer.
		 @param cr: A database cursor
		 @param uid: ID of the user currently logged in
		 @param context: A standard dictionary
		 @return : retrun report
		"""
		if context is None:
			context = {}
		employee_obj = self.pool.get('hr.employee')
		employee_obj.action_take_opencv(cr,uid,ids,context=context)
		return True